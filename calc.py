import ast
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class CalcMod(loader.Module):
    """Uses speedtest.net"""
    strings = {"name": "Calculator"}

    async def calccmd(self, message):
        """Tests your internet speed"""
        args = utils.get_args(message)
        try:
            # Використовуємо функцію `ast.literal_eval` для безпечного виконання виразу
            result = ast.literal_eval(args)
        except (ValueError, SyntaxError) as e:
            logger.error("Error solving math expression: %s", e)
            await utils.answer(message, "Помилка: некоректний вираз") 
        except Exception as e:
            logger.error("Error solving math expression: %s", e)
            await utils.answer(message, "Помилка при обчисленні виразу")
        await utils.answer(message, str(result))
