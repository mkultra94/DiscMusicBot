# Prerequisites

## Make sure Python 3.8+ is installed

```python --version```



## Install the required libraries

```pip install -r requirements.txt```



# Generating a token for your bot
### Go to [Discord app development portal](https://discordapp.com/developers/applications)
#### 1. Create application
#### 2. Click on the 'bot' tab on the lefthand sidebar
#### 3. Click 'add bot'
#### 4. In the dialog box click 'yes do it'
#### 5. Toggle 'public bot' OFF
#### 6. Toggle 'Message Content Intent' and 'Server Members Intent' ON
#### 7. Click 'save changes'
#### 8. Click 'Copy' to copy the bot's token

# Configuring DiscMusicBot.py
#### 1. Open the DiscMusicBot.py file with notepad or any text editor
#### 2. Go to the last line, replace ```your_token_goes_here``` with the token copied from the previous step
#### 3. Save and close the file
#### 4. Back in the [discord developer page](https://discordapp.com/developers/applications), click on the 'OAuth2' tab on the lefthand sidebar
#### 5. Under the 'scopes' section check ```bot```
#### 6. Copy the OAuth2 url and paste into your browser address bar
#### 7. Choose the server you'd like to add the bot to
#### 8. Click authorize to add the bot


# Running the bot
### navigate to the directory where DiscMusicBot.py is stored
```cd path\to\your\bot``` 

### Run the DiscMusicBot.py file
```python DiscMusicBot.py```

# Discord server commands
### ```!join``` to have the bot join your current channel
### ```!play``` followed by a youtube or soundcloud link. also works with song+artist name like ```!play vintage culture - next to me```
### ```!skip``` to skip the current song
### ```!pause``` pauses the current song
### ```!resume``` to resume a paused song
### ```!leave``` to have the musicbot leave the channel


















Open the DiscMusicBot.py file with notepad or any text editor
Go to the last line and replace ```your_token_goes_here``` with token generated from the discord developer page (https://discordapp.com/developers/applications)

