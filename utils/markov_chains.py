from markovify import Text as MText
from random import randint
import pickle
from utils.log import get_logger

logger = get_logger(__name__)


MODELNAME_TO_FILENAME: dict[str, str] = {
    'khashcha': 'data/users_messages/1472956766',
    'makuha': 'data/users_messages/658890395',
    'bolgov': 'data/users_messages/619857691',
    'razum': 'data/users_messages/588535976',
    'semen': 'data/users_messages/1399469085',
    'auf': 'data/pacan.txt',
}


def _dump_model(model_name: str, model: MText) -> None:
    logger.debug('start func, model_name=%s', model_name)

    filename = f'{MODELNAME_TO_FILENAME[model_name]}.pickle'
    try:
        with open(filename, 'wb') as pickle_f:
            pickle.dump(model, pickle_f)
    except FileNotFoundError as e:
        logger.error(f'Could not dump an object to a file; Error: {e}')


def _generate_model(model_name: str) -> MText:
    logger.debug('start func, model_name=%s', model_name)

    try:
        model = None
        with open(MODELNAME_TO_FILENAME[model_name], 'r', encoding="utf8") as f:
            model = MText(f)
            _dump_model(model_name, model)
        return model

    except FileNotFoundError as e:
        logger.error(f'No model:{model_name} exists; {e}')


def _check_and_generate_model(model_name: str) -> MText:
    logger.debug('start func, model_name=%s', model_name)

    try:
        filename = f'{MODELNAME_TO_FILENAME[model_name]}.pickle'
        with open(filename, 'rb') as pickle_f:
            return pickle.load(pickle_f)
    except FileNotFoundError:
        logger.info(f'{filename} was not found, creating a model')
        return _generate_model(model_name)


def generate_markov_sentence(model_name: str) -> str:
    logger.debug('start func, model_name=%s', model_name)

    model = _check_and_generate_model(model_name)
    sentence = None
    while sentence is None:
        sentence = model.make_sentence(min_words=randint(5, 40))
    return sentence
