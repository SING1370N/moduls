import logging

from search_engine_parser import GoogleSearch

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class GoogleSearchMod(loader.Module):
    """Make a Google search, right in your chat!"""
    strings = {"name": "Google Search",
               "no_term": "<b>Нічого не знайдено</b>",
               "no_results": "<b>Не вдалося знайти нічого про</b> <code>{}</code> <b>в Google</b>",
               "results": "<b>Це отримано з пошуку Google</b> <code>{}</code>:\n\n",
               "result": "<a href='{}'>{}</a>\n\n<code>{}</code>\n"}

    @loader.unrestricted
    @loader.ratelimit
    async def googlecmd(self, message):
        text = utils.get_args_raw(message.message)
        if not text:
            text = (await message.get_reply_message()).message
        if not text:
            await utils.answer(message, self.strings("no_term", message))
            return
        # TODO: add ability to specify page number.
        gsearch = GoogleSearch()
        gresults = await gsearch.async_search(text, 1)
        if not gresults:
            await utils.answer(message, self.strings("no_results", message).format(text))
            return
        msg = ""
        results = zip(gresults["titles"], gresults["links"], gresults["descriptions"])
        for result in results:
            msg += self.strings("result", message).format(utils.escape_html(result[0]), utils.escape_html(result[1]),
                                                          utils.escape_html(result[2]))
        await utils.answer(message, self.strings("results", message).format(utils.escape_html(text)) + msg)
