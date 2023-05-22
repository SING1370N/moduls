from .. import loader
import operator, math


@loader.tds
class CalcMod(loader.Module):
    strings = {"name": "Calc",
              "no_term": "<b>Нічого не знайдено</b>"}
    
    @loader.owner
    async def calccmd(self, message):
        text = utils.get_args_raw(message.message)
        if not text:
            text = (await message.get_reply_message()).message
        if not text:
            await utils.answer(message, self.strings("no_term", message))
            return
        await message.edit("COMMAND: " + text)
