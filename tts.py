from gtts import gTTS
from io import BytesIO
from .. import loader, utils


@loader.tds
class TTSMod(loader.Module):
    strings = {"name": "Text to speech",
               "tts_lang_cfg": "Тут установіть код мови",
               "tts_needs_text": "<code>Мені потрібен текст для перекладу!</code>"}

    def __init__(self):
        self.config = loader.ModuleConfig("TTS_LANG", "en", lambda m: self.strings("tts_lang_cfg", m))

    @loader.unrestricted
    @loader.ratelimit
    async def ttscmd(self, message):
        """Convert text to speech with Google APIs"""
        text = utils.get_args_raw(message.message)
        if len(text) == 0:
            if message.is_reply:
                text = (await message.get_reply_message()).message
            else:
                await utils.answer(message, self.strings("tts_needs_text", message))
                return

        tts = await utils.run_sync(gTTS, text, lang=self.config["TTS_LANG"])
        voice = BytesIO()
        await utils.run_sync(tts.write_to_fp, voice)
        voice.seek(0)
        voice.name = "voice.mp3"

        await utils.answer(message, voice, voice_note=True)
