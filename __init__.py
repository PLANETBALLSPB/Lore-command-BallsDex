from typing import TYPE_CHECKING

from ballsdex.packages.lore.cog import Lore

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

async def setup(bot: "BallsDexBot"):
    await bot.add_cog(Lore(bot))
