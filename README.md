# Discord-spambot
A spam bot for discord

## For IDE users as well as Termux users ##

Get the discord package using;

$ pkg install discord

Clone the repository;

$ git clone https://github.com/Sitiaro/Discord-spambot

Change directories using;

$ cd Discord-spambot

## If you're using IDE like pycharm or IDLE ##

Open the spambot.py file, scroll down to client.run("TOKEN_HERE") and paste your bot token in TOKEN_HERE. (more on how to get a discord token below)

## If you're using Termux ##

Open spambot.py file using;

$ nano spambot.py

Scroll down to client.run("TOKEN_HERE") and paste your bot token in TOKEN_HERE.
(You'll need Hackers Keyboard for scrolling down - https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard&hl=en_IN&gl=US)

## How to get your bot's token? ##

Visit Discord's Developer Portal - https://discord.com/developers/docs/intro

Open the menu (usually present on the left side of the screen) and tap on 'Applications'.

![d1](https://user-images.githubusercontent.com/46511306/114572093-ddbf1800-9c7f-11eb-9e26-71ec516a4f16.jpg)

Once you're on the applications screen, click on 'New Application',

![d2](https://user-images.githubusercontent.com/46511306/114572676-5f16aa80-9c80-11eb-9dcc-dc61bc04d98e.jpg)

After you click on it, it'll prompt you to enter Application Name (ps. this isn't the bot name). Do so, and head over to the bot panel by clicking on 'Bot' on the left panel;

![d3](https://user-images.githubusercontent.com/46511306/114573222-db10f280-9c80-11eb-92bc-04a3e501c5ab.PNG)

Now that you're on the bot panel, click on add bot (it'll ask you for a name again, this one being your bot's name). You'll see a 'Token' toggle right below your bot's name, click on 'reveal token' under that and copy the token. Once you do so, head over to your terminal and paste that token in place of TOKEN_HERE in client.run('TOKEN_HERE')

DO NOT RUN IT, we've another thing to do, that being adding the bot to your server.

## Adding the bot to your server ##

To add the bot to your server, head over to the application panel again and click on 'OAuth2'. Scroll down to Scope and select 'bot'.

![d4](https://user-images.githubusercontent.com/46511306/114574183-b36e5a00-9c81-11eb-95f5-54b9ec3b628f.PNG)

Once you select that, scroll down to 'Bot permissions' and click 'Admin'. Now your bot is ready to spam a server! To add it to the server, copy the url that was generated when you selected the 'bot' option under 'Scope' and paste it in a new tab. You'll be able to add your bot to a server when you do that (follows standard adding-a-bot-to-a-server method).


![d5](https://user-images.githubusercontent.com/46511306/114574790-38f20a00-9c82-11eb-8cba-bf1fb4596598.PNG)


## Running the bot ##

To run the bot, go back to your IDE (pycharm/IDLE/Termux), and run spambot.py
This won't do anything on the terminal itself but you'll be able to see your bot online in the server.

![d6](https://user-images.githubusercontent.com/46511306/114575318-b9b10600-9c82-11eb-8763-2df81483f485.PNG)

## NOTE: It'll be python spambot.py for you to run the bot and not python main.py; pycharm creates main.py by default so I tend to work with that. ##
