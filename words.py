# Fixed Random Word Generator
import itertools
import csv
import os

special_letters = {'a': ['A', 'a', 'ā', 'æ', 'ã', 'å', 'ā', 'à', 'á', 'â', 'ä', 'Ā', 'Ã', 'Å', 'Ā', 'À', 'Á', 'Â', 'Ä'],
                   'b': ['B', 'b'], 'c': ['C', 'c', 'Ç', 'ç'],
                   'd': ['D', 'd', 'Ḍ', 'ḍ'], 'e': ['E', 'e', 'ē', 'ê', 'é', 'è', 'ë', 'Ê', 'É', 'È', 'Ë', 'Ē'],
                   'f': ['F', 'f'], 'g': ['G', 'g'], 'h': ['H', 'h'],
                   'i': ['i', 'ī', 'î', 'ï', 'í', 'ì', 'I', 'Ī', 'Î', 'Ï', 'Í', 'Ì'], 'j': ['j', 'J'], 'k': ['k', 'K'],
                   'l': ['L', 'l', 'Ł', 'ł'], 'm': ['M', 'm'],
                   'n': ['n', 'ń', 'ñ', 'Ń', 'Ñ', 'N'],
                   'o': ['o', 'õ', 'ō', 'œ', 'ø', 'ò', 'ö', 'ó', 'ô', 'O', 'Œ', 'Ø', 'Ō', 'Ö', 'Õ', 'Ô', 'Ó', 'Ò'],
                   'p': ['p', 'P'], 'q': ['q', 'Q'], 'r': ['r', 'R'], 's': ['s', 'Ś', 'Š', 'ś', 'š', 'ß', 'S'],
                   't': ['t', 'T'],
                   'u': ['u', 'ū', 'û', 'ü', 'ú', 'ù', 'U', 'Ū', 'Û', 'Ü', 'Ú', 'Ù'], 'v': ['v', 'V'], 'w': ['w', 'W'],
                   'x': ['x', 'X'], 'y': ['y', 'Y', 'Ÿ', 'ÿ'],
                   'z': ['z', 'Z', 'ż', 'ź', 'ž', 'Ż', 'Ź', 'Ž']}
filename = "saved_word.csv"
fieldname = ['Word', 'Similars']


def file_name_existing_check(serverid):
    file_name = serverid+"saved_word.csv"
    file_present = False
    if os.path.isfile(filename):
        file_present = True
    if file_present:
        return file_name
    else:
        return False


def combine1(tpl):
    t = ""
    for i in tpl:
        t += i
    return t


def fwrite(word, gen_word):
    file_present = False
    if os.path.isfile(filename):
        file_present = True
    if file_present:
        with open(filename, 'a', encoding='UTF-8', newline="") as appendingcsvfile:
            csvwriter = csv.writer(appendingcsvfile)
            csvwriter.writerow([word, gen_word])
    else:
        with open(filename, 'w', encoding='UTF-8', newline="") as writingcsvfile:
            csvwriter = csv.writer(writingcsvfile)
            csvwriter.writerow(['Word', 'Similars'])
            csvwriter.writerow([word, gen_word])


def file_read_word(word):
    file_present = False
    if os.path.isfile(filename):
        file_present = True
    if file_present:
        with open(filename, 'r', encoding='UTF-8') as readingcsvfile:
            csvreader = csv.reader(readingcsvfile)
            for line in list(csvreader):
                if word in line[0]:
                    status = "Existing Word!"
                else:
                    wgen(word)
                    status = "Word does not exist, will be created instead!"
    return status


def file_read_all():
    file_present = False
    contents = []
    if os.path.isfile(filename):
        file_present = True
    if file_present:
        with open(filename, 'r', encoding='UTF-8') as readingcsvfile:
            csvreader = csv.reader(readingcsvfile)
            for line in list(csvreader):
                contents += line[0]
    return contents


def wgen(word):
    temp = []
    for each_letter in word.lower():
        temp.append(special_letters[each_letter])
    new_word = list(map(combine1, itertools.product(*temp)))
    fwrite(word, new_word)


def word_filter_list_check(serverid, word=None):
    file_name = file_name_existing_check(serverid)
    if word:
        if file_name:
            file_read_word(word)
    else:
        file_read_all()
    return


wgen("two")
