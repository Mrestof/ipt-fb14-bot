def get_makuha_paste() -> str:
    with open('data/makuha_paste.txt') as f:
        makuha_paste = f.readline()
    return makuha_paste
