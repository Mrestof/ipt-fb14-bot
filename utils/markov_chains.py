import markovify

# TODO: unify for auf and others
# TODO: make it into class URGENT
try:
    with open('data/users_messages/658890395', 'r', encoding="utf8") as f:
        text_model_makuha = markovify.Text(f)
    with open('data/users_messages/619857691', 'r', encoding="utf8") as f:
        text_model_bolgov = markovify.Text(f)
    with open('data/users_messages/1472956766', 'r', encoding="utf8") as f:
        text_model_khashcha = markovify.Text(f)
    with open('data/users_messages/588535976', 'r', encoding="utf8") as f:
        text_model_razum = markovify.Text(f)
    with open('data/users_messages/1399469085', 'r', encoding="utf8") as f:
        text_model_semen = markovify.Text(f)
except FileNotFoundError as e:
    print(f'There was an error: {e}')


def markov_sentence(path) -> str:
    with open(path, 'r', encoding="utf8") as f:
        text_model = markovify.Text(f)
        sentence = None
        while sentence is None:
            sentence = text_model.make_sentence()
        return sentence


def markov_user(user):
    sentence = None
    while sentence is None:
        if user == 'makuha':
            sentence = text_model_makuha.make_sentence()
        elif user == 'bolgov':
            sentence = text_model_bolgov.make_sentence()
        elif user == 'khashcha':
            sentence = text_model_khashcha.make_sentence()
        elif user == 'razum':
            sentence = text_model_razum.make_sentence()
        elif user == 'semen':
            sentence = text_model_semen.make_sentence()
    return sentence
