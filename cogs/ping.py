import nextcord
from nextcord import Interaction
from nextcord.ext import commands


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @nextcord.slash_command(name = "ping", description="Returns the ping of the bot")
    async def ping(self, interaction: Interaction):
        await interaction.send(f"Pong! In {round(self.bot.latency * 1000)} ms")

def setup(bot):
    bot.add_cog(ping(bot))