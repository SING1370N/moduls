from .. import loader, utils
import random


@loader.tds
class YesNoMod(loader.Module):
    strings = {"name": "YesNo",
               "yes_words_cfg_doc": "Yes words",
               "no_words_cfg_doc": "No words"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            "YES_WORDS", ["Так", "Ес", " Звісно"], lambda m: self.strings("yes_words_cfg_doc", m),
            "NO_WORDS", ["Ні", "Ноу", "Ніяк"], lambda m: self.strings("no_words_cfg_doc", m))

    @loader.unrestricted
    async def yesnocmd(self, message):
        yes = self.config["YES_WORDS"]
        no = self.config["NO_WORDS"]
        if random.getrandbits(1):
            response = random.choice(yes)
        else:
            response = random.choice(no)
        await utils.answer(message, response)
