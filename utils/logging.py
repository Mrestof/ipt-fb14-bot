from utils.get_time import get_time


def chat_logging_text(update):
    title = str(update.message.chat.title)
    first_name = str(update.message.from_user.first_name)
    username = str(update.message.from_user.username)
    text = str(update.message.text)
    with open('data/secretlog.txt', 'a') as secret:
        secret.write(f'{get_time()}   {title} | {first_name} (@{username})\n{text}\n')


def chat_logging_photo(update):
    title = str(update.message.chat.title)
    first_name = str(update.message.from_user.first_name)
    username = str(update.message.from_user.username)
    photo_id = update.message.photo[0].file_id
    with open('data/secretlog.txt', 'a') as secret:
        secret.write(f'{get_time()}   {title} | {first_name} (@{username})\nphoto_id: {photo_id}\n')


def chat_logging_video(update):
    title = str(update.message.chat.title)
    first_name = str(update.message.from_user.first_name)
    username = str(update.message.from_user.username)
    video_id = update.message.video.file_id
    with open('data/secretlog.txt', 'a') as secret:
        secret.write(f'{get_time()}   {title} | {first_name} (@{username})\nvideo_id: {video_id}\n')


def chat_logging_audio(update):
    title = str(update.message.chat.title)
    first_name = str(update.message.from_user.first_name)
    username = str(update.message.from_user.username)
    audio_id = update.message.audio.file_id
    song = update.message.audio.title
    author = update.message.audio.performer
    with open('data/secretlog.txt', 'a') as secret:
        secret.write(f'{get_time()}   {title} | {first_name} (@{username})\n'
                     f'{author} - {song}\naudio_id: {audio_id}\n\n')
