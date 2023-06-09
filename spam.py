from .. import loader, utils
import logging
import asyncio


logger = logging.getLogger(__name__)


@loader.tds
class SpamMod(loader.Module):
    """Annoys people really effectively"""
    strings = {"name": "Spam",
               "need_spam": "<b>Мені потрібно щось спамити</b>",
               "spam_urself": "<b>Самі розсилайте спам</b>",
               "nice_number": "<b>Гарне число</b>",
               "much_spam": "<b>Ха-ха, багато спаму</b>"}

    async def spamcmd(self, message):
        """.spam <count> <message>"""
        use_reply = False
        args = utils.get_args(message)
        logger.debug(args)
        if len(args) == 0:
            await utils.answer(message, self.strings("need_spam", message))
            return
        if len(args) == 1:
            if message.is_reply:
                use_reply = True
            else:
                await utils.answer(message, self.strings("spam_urself", message))
                return
        count = args[0]
        spam = (await message.get_reply_message()) if use_reply else message
        spam.message = " ".join(args[1:])
        try:
            count = int(count)
        except ValueError:
            await utils.answer(message, self.strings("nice_number", message))
            return
        if count < 1:
            await utils.answer(message, self.strings("much_spam", message))
            return
        await message.delete()
        if count > 20:
            # Be kind to other people
            sleepy = 2
        else:
            sleepy = 0
        i = 0
        size = 1 if sleepy else 100
        while i < count:
            await asyncio.gather(*[message.respond(spam) for x in range(min(count, size))])
            await asyncio.sleep(sleepy)
            i += size
        await self.allmodules.log("spam", group=message.to_id, data=spam.message + " (" + str(count) + ")")
