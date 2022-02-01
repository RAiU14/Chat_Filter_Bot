# Fixed Random Word Generator
import discord
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


# Checking if server based CSV file exists or not.
def file_existing_check(serverid):
    file_name = serverid + "saved_word.csv"
    return file_name


def combine1(tpl):
    t = ""
    for i in tpl:
        t += i
    return t


# Appending lowercase/uppercase word possibility to the list.
def append_word(exword):

    # Appending possible lower case and uppercase word to the file.
    with open(filename, 'a', encoding='UTF-8', newline='') as appendingcsvfile:
        csvwriter = csv.writer(appendingcsvfile)
        csvwriter.writerow([exword, [exword.lower(), exword.upper()]])


# Writing/Appending contents to new/existing file
def file_write(word, gen_word):
    file_present = False
    if os.path.isfile(filename):
        file_present = True
    if file_present:
        # Appending new word
        with open(filename, 'a', encoding='UTF-8', newline="") as appendingcsvfile:
            csvwriter = csv.writer(appendingcsvfile)
            csvwriter.writerow([word, gen_word])
        append_word(word)
        write_status = "Word added successfully!"
        return write_status
    else:
        # Writing the new contents to the file if not already existing.
        with open(filename, 'w', encoding='UTF-8', newline="") as writingcsvfile:
            csvwriter = csv.writer(writingcsvfile)
            csvwriter.writerow(['Word', 'Similars'])
            csvwriter.writerow([word, gen_word])
        append_word(word)
        write_status = "No existing list in this server. New file created and word have been added!"
        return write_status


# Reading contents of the word
def file_read_word(word):
    file_present = False
    if os.path.isfile(filename):
        file_present = True
    if file_present:
        with open(filename, 'r', encoding='UTF-8') as readingcsvfile:
            csvreader = csv.reader(readingcsvfile)
            for line in list(csvreader):
                if word in line[0]:
                    status = True
                else:
                    word_generator(word)
                    status = False
    return status


# Reading all the contents in the CSV file.
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


# Generate possible word combinations
def word_generator(word):
    temp = []
    for each_letter in word.lower():
        temp.append(special_letters[each_letter])
    new_word = list(map(combine1, itertools.product(*temp)))
    write_status = file_write(word, new_word)  # Calling file writing function here
    return write_status


# Main function connecting from the bot command to -
# Add word as well as it's combination to the list on CSV file
def word_add_to_list(serverid, word):
    get_filename = file_existing_check(serverid)
    if get_filename:
        status = word_generator(word)
    else:
        status = False
    if status:
        embed = discord.Embed(title="Sucess!", description=f"{status}", colour=discord.Color.green())
        return embed
    else:
        print("Error occured while writing to file!")


# Main function connecting from the bot command to -
# Check if word is present in the list if parameter is passed. If no parameters are passed, return all the contents in the csv file.
def word_check_list(serverid, word=None):
    file_name = file_name_existing_check(serverid)
    if word:
        if file_name:
            word_check_status = file_read_word(word)
            if word_check_status:
                embed = discord.Embed(title=f"{word} is already present:", description="This word is already present in the filter list.", colour=discord.Color.green())
                return embed
            else:
                embed = discord.Embed(title=f"{word} is not present:", description="This word is not present in the filter list!", colour=discord.Color.red())
            return embed
    else:
        word_list = ''
        words = file_read_all()  # words will have list value. Discord Embed needs string values.
        for item in words:
            word_list += item
        embed = discord.Embed(title="Available in List:", description="All the available word in this server:",
                              colour=discord.Color.blue())
        embed.add_field(name="", value=word_list)
        return embed
