import markovify


# TODO: initialise text_model on bot start instead of on every command call
def markov_sentence(path) -> str:
    with open(path, 'r', encoding="utf8") as f:
        text_model = markovify.Text(f)
        sentence = None
        while sentence is None:
            sentence = text_model.make_sentence()
        return sentence

