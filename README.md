Prerequisites

Make sure Python 3.8+ is installed.

```python --version```



Install the required libraries:

```pip install -r requirements.txt```



Generating a token for your bot:
Go to ```https://discordapp.com/developers/applications```
Create application
Click on the 'bot' tab on the lefthand sidebar
Click 'add bot'
In the dialog box click 'yes do it'
Toggle 'public bot' OFF
Togge 'Message Content Intent' and 'Server Members Intent' ON
Click 'save changes'
Click 'Copy' to copy the bot's token

Open the DiscMusicBot.py file with notepad or any text editor
Go to the last line, replace ```your_token_goes_here``` with the token copied from the previous step
Save and close the file

Back in the discord developer page, click on the 'OAuth2' tab on the lefthand sidebar
Under the 'scopes' section check ```bot```
Copy the OAuth2 url and paste into your browser address bar
Choose the server you'd like to add the bot to
Click authorize to add the bot


Running the bot:
navigate to the directory where DiscMusicBot.py is stored
```cd path\to\your\bot``` 

Run the DiscMusicBot.py file
```python DiscMusicBot.py```

Discord server commands:
```!join``` to have the bot join your current channel
```!play``` followed by a youtube or soundcloud link. also works with song+artist name like ```!play vintage culture - next to me```
```!skip``` to skip the current song
```!pause``` pauses the current song
```!resume``` to resume a paused song
```!leave``` to have the musicbot leave the channel


















Open the DiscMusicBot.py file with notepad or any text editor
Go to the last line and replace ```your_token_goes_here``` with token generated from the discord developer page (https://discordapp.com/developers/applications)

