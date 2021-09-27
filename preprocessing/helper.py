import codecs


def merge_lists(lemmas: list, bigrams: list, trigrams: list) -> list:
    merge_list = list()
    for lemma in lemmas:
        merge_list.extend(lemma)
    for bigram in bigrams:
        merge_list.append(bigram)
    for trigram in trigrams:
        merge_list.append(trigram)
    return merge_list


def read_txt_file(path: str) -> list:
    strings = list()

    f = codecs.open(path, "r", encoding="utf-8")
    while True:
        # read next line
        line = f.readline()

        # if line is empty, you are done with all lines in the file
        if not line:
            break

        line = line.lower().strip()
        strings.append(line)

    f.close()

    return strings
