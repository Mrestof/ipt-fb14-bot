from telegram import Update
from telegram.ext import CallbackContext
from utils.voice import transcribe
from utils.log import get_logger

logger = get_logger(__name__)


async def voice_messages(update: Update, context: CallbackContext) -> None:
    if update.edited_message is not None:
        return None
    logger.debug('got voice update')

    voice_file_id = update.message.voice.file_id

    # get the file object for the voice file
    voice_file = await context.bot.get_file(voice_file_id)
    #        print(dir(voice_file))

    # download the voice file to your local machine
    temp_file = f'data/input_file{voice_file_id}.ogg'
    await voice_file.download_to_drive(temp_file)
    await transcribe(temp_file, update, context)
