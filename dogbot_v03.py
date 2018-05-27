import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready() :
    print ("Bot is ready")

@client.event
async def on_message(message) :
    input_text = message.content.lower()
    if input_text == "sit":
      await client.send_message(message.channel, "The dog obliges and sits after barking in content")
    if input_text == "quiet":
          await client.send_message(message.channel, "The dog looks up with precious eyes staring in silent")
    if ( input_text == "speak" ) or ( input_text == "bark" ):
                await client.send_message(message.channel, "The dog barks very loud, probably in happiness but it seems a little angry")
    if input_text == "high five":
                      await client.send_message(message.channel, "The dog reaches up and slaps your hand with more of a high 10")
    if input_text == "fetch":
                      await client.send_message(message.channel, "You toss the ball... a few seconds later the dog appears, ball in its mouth")
    if input_text == "who made you":
                          await client.send_message(message.channel, "The dog makes a grunting noise as it nudges its head towards @Swoosher.gov")
    if input_text == "shake":
                          await client.send_message(message.channel, "The dog looks up in honor, as it puts its paw on your hand")
    if input_text == "roll over":
                          await client.send_message(message.channel, "The dog starts a horizontal turn, then puts its whole body weight into it, landing back on its feet")
    if input_text == "suck off":
                              await client.send_message(message.channel, "The dog looks at the peanut butter on your... area, and starts to lick his lips")




client.run("NDUwMzUwMjA4NjUyNjczMDI0.Dex9Gw.v5NIH4A41yktiO2bVCPE3XlhWXI")
