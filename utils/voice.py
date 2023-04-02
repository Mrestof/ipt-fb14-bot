from telegram import Update
from telegram.ext import CallbackContext
import speech_recognition as sr
import subprocess

async def transcribe(temp_file: str, update: Update, context: CallbackContext) -> None:

    voice_file_id = update.message.voice.file_id
    msg_id = update.message.message_id
    chat_id = update.message.chat.id

    # convert to .wav file format
    dest_temp_file = 'data/output{voice_file_id}.wav'

    process = subprocess.run(['ffmpeg', '-i', temp_file, dest_temp_file])
    if process.returncode != 0:
        print("Couldn't convert to wav format")
        return

    # Initialize recognizer
    r = sr.Recognizer()

    # Open audio file and read data into audio variable
    with sr.AudioFile(dest_temp_file) as source:
        audio = r.record(source)

    try:
        response = f'Бан. Текст в голосовухе:\n "{r.recognize_google(audio, language="ru-RU")}"'
        await context.bot.send_message(chat_id=chat_id, text=response, reply_to_message_id=msg_id)
#        print('Український варіант: ' + r.recognize_google(audio, language='uk-UA'))
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
    except sr.RequestError as e:
        print(f'Could not request results from Google Speech Recognition service; {e}')

    process = subprocess.run(['rm', temp_file, dest_temp_file])
    if process.returncode != 0:
        print("Error while cleaning *.ogg and *.wav files")
        return





