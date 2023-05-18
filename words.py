def generate_words_set():
    with open("./words.txt", "r") as f:
        return set(l.rstrip() for l in f)
