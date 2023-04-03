from telegram import Update
from telegram.ext import CallbackContext
import speech_recognition as sr
import subprocess

async def transcribe(ogg_temp_file: str, update: Update, context: CallbackContext) -> None:

    voice_file_id = update.message.voice.file_id
    msg_id = update.message.message_id
    chat_id = update.message.chat.id

    # convert to .wav file format
    wav_temp_file = f'data/output_{voice_file_id}.wav'

    # Load the ogg file and convert to WAV format
    process = subprocess.run(['ffmpeg', '-i', ogg_temp_file, wav_temp_file])
    if process.returncode != 0:
        print("Error while converting .ogg file to .wav file")
        return

    # Initialize recognizer
    r = sr.Recognizer()

    # Open audio file and read data into audio variable
    with sr.AudioFile(wav_temp_file) as source:
        audio = r.record(source)

    try:
        rus_response = r.recognize_google(audio, language="ru-RU", show_all=True)
        uk_response = r.recognize_google(audio, language="uk-UA", show_all=True)
        rus_confidence = rus_response['alternative'][0]['confidence']
        uk_confidence = uk_response['alternative'][0]['confidence']

        if uk_confidence > 0.7:
            response = f'Бан. Текст в голосовухе:\n\"{rus_response["alternative"][0]["transcript"]}\"\n\nАльтернативна транскипція:\n\"{uk_response["alternative"][0]["transcript"]}\"'
        else:
            response = f'Бан. Текст в голосовухе:\n\"{rus_response["alternative"][0]["transcript"]}\"'

        await context.bot.send_message(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')

    except sr.RequestError as e:
        print(f'Could not request results from Google Speech Recognition service; {e}')

    process = subprocess.run(['rm', ogg_temp_file, wav_temp_file])
    if process.returncode != 0:
        print("Error while cleaning .ogg and .wav files")
        return





