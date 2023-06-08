import ast
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class CalcMod(loader.Module):
    """Uses literal_eval"""
    strings = {
        "name": "Calculator",
        "no_term": "<b>Нічого не знайдено</b>"
               }

    async def calccmd(self, message):
        """Calculate"""
        try:
            args = utils.get_args(message)
            logger.debug(args)
            result = ast.literal_eval(" ".join(args))
            await utils.answer(message, f"Calc: {result}")
        except (ValueError, SyntaxError) as e:
            logger.error("Error solving math expression: %s", e)
            await utils.answer(message, "Помилка: некоректний вираз")
        except Exception as e:
            logger.error("Error solving math expression: %s", e)
            await utils.answer(message, "Помилка при обчисленні виразу")

