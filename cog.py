import discord
from discord.ext import commands
from discord import app_commands
import random

class Lore(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="lore", description="Obtén una descripción del Lore")
    async def lore(self, interaction: discord.Interaction):
        lores = [
            f"Ejemplo 1.",
            f"Ejemplo 2.",
            f"Ejemplo 3.",
            f"Ejemplo 4."
        ]

        embed = discord.Embed(
            title="Lore",
            description=random.choice(lores),
            color=discord.Color.blue()
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)  # Solo el ejecutor ve el mensaje

async def setup(bot: commands.Bot):
    await bot.add_cog(Lore(bot))


