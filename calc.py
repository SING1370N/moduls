from .. import loader
import random
import math
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Cacl"}
	@loader.owner
	async def calccmd(self, message):
				await message.edit("В процессі розробки.")

		
