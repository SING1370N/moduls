import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class CalcMod(loader.Module):
    """Uses literal_eval"""
    strings = {
        "name": "Calculator",
        "no_term": "<b>Так а що рахувати?</b>"
               }

    async def calccmd(self, message):
        """Calculate"""
        try:
            text = utils.get_args_raw(message.message)
            if not text:
                text = (await message.get_reply_message()).message
            if not text:
                await utils.answer(message, self.strings("no_term", message))
                return
            logger.debug(text)
            result = eval(text)
            await utils.answer(message, f"Підрахунок: {result}")
        except (ValueError, SyntaxError) as e:
            logger.error("Error solving math expression: %s", e)
            await utils.answer(message, "Помилка: некоректний вираз")
        except Exception as e:
            logger.error("Error solving math expression: %s", e)
            await utils.answer(message, "Помилка при обчисленні виразу")

