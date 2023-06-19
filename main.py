import os

import nextcord
from nextcord.ext import commands


intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f"The bot is ready")
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="/help"))


#Cogs Loader
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


bot.run("MTEwMDE2Njg4ODI4NzM5MTg0NA.GbZvQE.zHDHZUAiAFs3C2sbb1FQHEe5LHVC1xUcK3HB8M")