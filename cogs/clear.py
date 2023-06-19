import nextcord
from nextcord import Interaction
from nextcord.ext import commands


class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @nextcord.slash_command(name = "clear", description="Clear up some messages!")
    async def clear(self, interaction: Interaction, Quantity:int):
        await interaction.channel.purge(limit = Quantity)
        await interaction.send(f"Cleared {Quantity} messages!", delete_after= 3)

def setup(bot):
    bot.add_cog(clear(bot))