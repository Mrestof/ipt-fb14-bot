from markovify import Text as MText
from random import randint

# TODO: refactor:
#   - [ ] general
#   - [ ] get rid of dicts, maybe make it into class
#     (reasoning: access by strings is too much error prone)
#   - [x] unify for auf and others


MODELNAME_TO_FILENAME: dict[str, str] = {
    'khashcha': 'data/users_messages/1472956766',
    'makuha': 'data/users_messages/658890395',
    'bolgov': 'data/users_messages/619857691',
    'razum': 'data/users_messages/588535976',
    'semen': 'data/users_messages/1399469085',
    'auf': 'data/pacan.txt',
}
_text_models = dict[str, MText]()


def _check_and_generate_model(model_name: str) -> None:
    # if model is in place, exit
    if _text_models.get(model_name) is not None:
        return
    # else: generate the model
    try:
        with open(MODELNAME_TO_FILENAME[model_name], 'r', encoding="utf8") as f:
            model = MText(f)
        _text_models[model_name] = model
    except FileNotFoundError as e:
        print(f'There was an error: {e}')


def generate_markov_sentence(model_name: str) -> str:
    _check_and_generate_model(model_name)
    model = _text_models[model_name]
    sentence = None
    while sentence is None:
        sentence = model.make_sentence(min_words=randint(5, 40))
    return sentence
