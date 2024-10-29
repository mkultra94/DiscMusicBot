import discord
from discord.ext import commands
import yt_dlp
import asyncio

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

# Global variable to manage voice client state
voice_client = None
song_queue = asyncio.Queue()  # Queue to store songs for playback

# Function to extract audio source from a URL or song title
def get_audio_source(url_or_search):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'default_search': 'ytsearch',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url_or_search, download=False)
        url = info['url'] if 'url' in info else info['entries'][0]['url']
        return discord.FFmpegPCMAudio(url, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")

@bot.event
async def on_ready():
    print(f'Bot is ready and logged in as {bot.user}')

@bot.command(name='join')
async def join(ctx):
    global voice_client
    if ctx.author.voice:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
        await ctx.send(f'Joined {voice_channel}')
    else:
        await ctx.send("You're not in a voice channel!")

@bot.command(name='play')
async def play(ctx, *, url_or_search: str):
    global voice_client

    if not voice_client or not voice_client.is_connected():
        if ctx.author.voice:
            voice_client = await ctx.author.voice.channel.connect()
        else:
            await ctx.send("You're not in a voice channel!")
            return

    audio_source = get_audio_source(url_or_search)
    if audio_source:
        await song_queue.put(audio_source)
        if not voice_client.is_playing():
            await play_next_song(ctx)
    else:
        await ctx.send("Could not find the song.")

async def play_next_song(ctx):
    global voice_client

    if not song_queue.empty():
        audio_source = await song_queue.get()
        voice_client.play(audio_source, after=lambda e: asyncio.run_coroutine_threadsafe(play_next_song(ctx), bot.loop))

@bot.command(name='pause')
async def pause(ctx):
    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await ctx.send("Paused the song.")
    else:
        await ctx.send("No song is currently playing.")

@bot.command(name='resume')
async def resume(ctx):
    if voice_client and voice_client.is_paused():
        voice_client.resume()
        await ctx.send("Resumed the song.")
    else:
        await ctx.send("No song is paused.")

@bot.command(name='skip')
async def skip(ctx):
    if voice_client and voice_client.is_playing():
        voice_client.stop()
        await ctx.send("Skipped the song.")
        await play_next_song(ctx)
    else:
        await ctx.send("No song is currently playing.")

@bot.command(name='leave')
async def leave(ctx):
    global voice_client
    if voice_client:
        await voice_client.disconnect()
        await ctx.send("Disconnected from the voice channel.")
        voice_client = None
    else:
        await ctx.send("I'm not connected to a voice channel.")

# Run the bot with your token
bot.run("your_token_goes_here")
