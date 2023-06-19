import nextcord
from nextcord import Interaction
from nextcord.ext import commands

import random

class palla8(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @nextcord.slash_command(name = "palla8", description="Ask something to the magic ball!")
    async def palla8(self, interaction: Interaction, Question:str):
        responses = ["Per quanto posso vedere, sì",
                    "È certo",
                    "È decisamente così",
                    "Molto probabilmente",
                    "Le prospettive sono buone",
                    "I segni indicano di sì",
                    "Senza alcun dubbio",
                    "Sì",
                    "Sì, senza dubbio",
                    "Ci puoi contare",
                    "È difficile rispondere, prova di nuovo",
                    "Rifai la domanda più tardi",
                    "Meglio non risponderti adesso",
                    "Non posso predirlo ora",
                    "Concentrati e rifai la domanda",
                    "Non ci contare",
                    "La mia risposta è no",
                    "Le mie fonti dicono di no",
                    "Le prospettive non sono buone",
                    "Molto incerto!"]
        embed = nextcord.Embed(title = "Palla 8 - " + interaction.author, color = nextcord.Colour.green())
        embed.add_field(name = "Domanda:", value = Question, inline = True)
        embed.add_field(name = "Risposta:", value = random.choice(responses), inline = True)
        embed.set_footer(icon_url = "https://i.imgur.com/ABk4OMo.png", text = "𝗝𝘂𝘀𝘁 𝗮 𝗡𝗼𝗿𝗺𝗮𝗹 𝗕𝗼𝘁 ©𝟮𝟬𝟮𝟬 - 𝗚𝗮𝗯𝗿𝘆 & 𝗔𝗶𝗺𝗲")
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(palla8(bot))