import ast
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class CalcMod(loader.Module):
    """Uses literal_eval"""
    strings = {"name": "Calculator"}

    async def calccmd(self, message):
        """Calculate"""
        try:
            args = utils.get_args(message)
            print(args)
            # Використовуємо функцію `ast.literal_eval` для безпечного виконання виразу
            result = ast.literal_eval(" ".join(args))
            await utils.answer(message, f"Calc: {result}")
        except (ValueError, SyntaxError) as e:
            logger.error("Error solving math expression: %s", e)
            await utils.answer(message, "Помилка: некоректний вираз")
        except Exception as e:
            logger.error("Error solving math expression: %s", e)
            await utils.answer(message, "Помилка при обчисленні виразу")
