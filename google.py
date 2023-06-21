import logging

from search_engine_parser import GoogleSearch
from search_engine_parser import BingSearch
from search_engine_parser import YahooSearch
from search_engine_parser import DuckDuckGoSearch
from search_engine_parser import GithubSearch
from search_engine_parser import StackOverflowSearch

from .. import loader, utils

logger = logging.getLogger(__name__)



@loader.tds
class GoogleSearchMod(loader.Module):
    """Make a search"""
    strings = {"name": "Search",
               "no_term": "<b>Нічого не знайдено</b>",
               "error": "<b>Сталася дивна помилка, скоріш за все КАПЧА</b>",
               "no_results": "<b>Не вдалося знайти нічого про</b> <code>{}</code> <b>в Google</b>",
               "results": "<b>Це отримано з пошуку Google</b> <code>{}</code>:\n\n",
               "result": "<a href='{}'>{}</a>\n\n<code>{}</code>\n"}

    @loader.unrestricted
    @loader.ratelimit
    async def search_mode(self, message, CoreSearch):
        text = utils.get_args_raw(message.message)
        if not text:
            text = (await message.get_reply_message()).message
        if not text:
            await utils.answer(message, self.strings("no_term", message))
            return
        try:
            search = CoreSearch()
            results = await search.async_search(text, 1)
            if not results:
                await utils.answer(message, self.strings("no_results", message).format(text))
                return
            msg = ""
            all_results = zip(results["titles"], results["links"], results["descriptions"])
            for result in all_results:
                msg += self.strings("result", message).format(utils.escape_html(result[0]), utils.escape_html(result[1]),
                                                              utils.escape_html(result[2]))
            await utils.answer(message, self.strings("results", message).format(utils.escape_html(text)) + msg)
        except Exception:
            await utils.answer(message, self.strings("error", message))
            return

    async def googlecmd(self, message):
        await self.search_mode(message, GoogleSearch)

    async def bingcmd(self, message):
        await self.search_mode(message, BingSearch)

    async def duckcmd(self, message):
        await self.search_mode(message, DuckDuckGoSearch)

    async def yahocmd(self, message):
        await self.search_mode(message, YahooSearch)

    async def gitcmd(self, message):
        await self.search_mode(message, GithubSearch)

    async def stackcmd(self, message):
        await self.search_mode(message, StackOverflowSearch)
