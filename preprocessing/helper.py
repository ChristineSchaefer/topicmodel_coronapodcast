# ##imports
import codecs


# ##functions
def merge_lists(lemmas: list, bigrams: list, trigrams: list) -> list:
    """Function to merge list together.

            Parameters:
            ----------
                lemmas: list of lemmas
                bigrams: list of bigrams
                trigrams: list of trigrams

            Returns:
            -------
                list with all elements from parameter lists"""

    merge_list = list()

    for lemma in lemmas:
        merge_list.extend(lemma)
    for bigram in bigrams:
        merge_list.append(bigram)
    for trigram in trigrams:
        merge_list.append(trigram)
    return merge_list


def read_txt_file(path: str) -> list:
    """Function to read txt file.

            Parameters:
            ----------
                path: str
                    Receives the path to file as string.

            Returns:
            -------
                list with content of file"""

    strings = list()

    f = codecs.open(path, "r", encoding="utf-8")
    while True:
        # read next line
        line = f.readline()

        # if line is empty, you are done with all lines in the file
        if not line:
            break

        line = line.lower().strip()
        # add line to list
        strings.append(line)

    f.close()
    return strings
