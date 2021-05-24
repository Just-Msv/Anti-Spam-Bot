#importing modules
from discord.ext import commands
import asyncio

#initiating the bot
client = commands.Bot(command_prefix="$")

#implementation
@client.event
async def on_ready():
  print('Bot ready')
  print('MADE BY MSV')  #DONT REMOVE THIS
  while True:
    print('Bot is Watching')
    await asyncio.sleep(10)
    with open('spamdet.txt','r+') as file:
      file.truncate(0)
#detection
@client.event
async def on_message_recieved(message):
  nc = 0
  with open('spamdet.txt','r+') as file:
    for lines in file:
      if lines.strip('\n') == str(message.author.id):
        nc+=1
    file.writelines(f"{str(message.author.id)}\n")
    #this if for the number of messages being send in sucession; you can change it according to your need
    if nc > 5:
      await message.guild.kick(message.author, reason='spam')
      await asyncio.sleep(1)
      await message.guild.unban(message.author)
      print('Poof')
    
client.run("REPLACE_TOKEN")
