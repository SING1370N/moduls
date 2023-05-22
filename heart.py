from .. import loader
import random
import math
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Heart"}
	@loader.owner
	async def heartcmd(self, message):
		for _ in range(2):
			for heart in ['❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '💘']:
				await message.edit(heart)
				await sleep(1)
				
	async def mooncmd(self, message):
		for _ in range(2):
			for moon in ['🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔', '🌕']:
				await message.edit(moon)
				await sleep(1)
				
	async def twomooncmd(self, message):
		for _ in range(4):
			for ms in ['🌚', '🌝']:
				await message.edit(ms)
				await sleep(1)
				
	async def fakeloadcmd(self, message):
		await message.edit('Loading...')
		sleep(1)
		number = 10
		await message.edit('0%')
		for ms in ['%  █', '%  ██', '%  ███', '%  ████', '%  █████', '%  ██████', '%  ███████', '%  ████████', '%  █████████', '% ██████████']:
				await message.edit(str(number) + ms)
				number = number + 10
				await sleep(round(random.uniform(0.3, 2.2), 2))
		await message.edit(' Ready! ')
				
		
