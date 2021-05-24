# Anti-Spam-Bot
An anti-spam/anti-raid bot for discord. It detects the number of messages being sent in a chat. Every time a message us sent, the bot stores the message in a .txt file and it's an async event so it'll be called personally for every time someone sends a message to the chat which is then counted. If it exceeds a certain threshold, the bot removes the user from the server.

## Setup ( Replit or Glitch )

[![Run on Repl.it](https://repl.it/badge/github/MSVFORYOU/Anti-Spam-Bot)](https://repl.it/github/MSVFORYOU/Anti-Spam-Bot)
[![Remix on Glitch](https://cdn.glitch.com/2703baf2-b643-4da7-ab91-7ee2a2d00b5b%2Fremix-button.svg)](https://glitch.com/edit/#!/import/github/MSVFORYOU/Anti-Spam-Bot)

- Install the required modules!
- Create a bot application at the [discord developer portal](https://discord.com/developers/applications) and add to your discord server.
- Install the required modules!
- Allow the "Server Member Intent" under the "Privileged Gateway Intents" in the [discord developer panel](https://discord.com/developers/applications). (THIS IS VERY IMPORTANT! The bot will not work propertly without and will not be able to find or kick server members.)

- Place your bot token and adjust the "[antispam.py](https://github.com/MSVFORYOU/Anti-Spam-Bot/anitspam.py)" to your liking.

- Then Run the Bot :)

## Setup ( IDE users as well as Termux users )

Get the discord package using;

- ```$ pkg install discord```

Clone the repository;

- ```$ git clone https://github.com/MSVFORYOU/Anti-Spam-Bot```

Change directories using;

- ```$ cd antispamdisc```

### If you're using IDE like pycharm or IDLE 

- Open the ```antispam.py``` file, scroll down to client.run("TOKEN_HERE") and paste your bot token in TOKEN_HERE. (more on how to get a discord token below)

### If you're using Termux

- Open ``antispam.py`` file using;

- ```$ nano antispam.py```

- Scroll down to client.run("TOKEN_HERE") and paste your bot token in TOKEN_HERE.(You'll need Hackers Keyboard for scrolling down - https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard&hl=en_IN&gl=US)


# ✨ Contributors :



<table>
  <tr>
     <td align="center"><a href="https://github.com/MSVFORYOU"><img src="https://avatars.githubusercontent.com/u/78690237?v=4" width="100px;" alt=""/><br /><sub><b>Owner</b></sub>
     
  </tr>
  
</table>
