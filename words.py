# Fixed Random Word Generator
import discord
import itertools
import csv
import os

# Make it a way where all the special_letters are saved in another csv file where beta testers can add/remove them on a later stage.
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
fieldname = ['Word', 'Similars']

# Try to set this path to another directory.


# Checking if server based CSV file exists or not.
def file_existing_check(serverid):
    file_name = serverid + "saved_word.csv"
    return file_name


def combine1(tpl):
    t = ""
    for i in tpl:
        t += i
    return t


# Generate possible word combinations
def word_generator(serverid, word):
    temp = []
    for each_letter in word.lower():
        temp.append(special_letters[each_letter])
    new_word = list(map(combine1, itertools.product(*temp)))
    write_status = file_write(serverid, word, new_word)  # Calling file writing function here
    return write_status


# Appending lowercase/uppercase word possibility to the list.
def append_word(serverid, exword):
    # Appending possible lower case and uppercase word to the file.
    filename = file_existing_check(serverid)
    with open(filename, 'a', encoding='UTF-8', newline='') as appendingcsvfile:
        csvwriter = csv.writer(appendingcsvfile)
        csvwriter.writerow([exword, [exword.lower(), exword.upper()]])


# Writing/Appending contents to new/existing file
def file_write(serverid, word, gen_word):
    filename = file_existing_check(serverid)
    try:
        if os.path.isfile(filename):
            # Appending new word
            with open(filename, 'a', encoding='UTF-8', newline="") as appendingcsvfile:
                csvwriter = csv.writer(appendingcsvfile)
                csvwriter.writerow([word, gen_word])
            append_word(serverid, word)
            write_status = True
            return write_status
        else:
            # Writing the new contents to the file if not already existing.
            with open(filename, 'w', encoding='UTF-8', newline="") as writingcsvfile:
                csvwriter = csv.writer(writingcsvfile)
                csvwriter.writerow(['Word', 'Similars'])
                csvwriter.writerow([word, gen_word])
            append_word(serverid, word)
            write_status = False
            return write_status
    except Exception:
        write_status = False
    return write_status


# Reading contents of the word
def file_read_word(serverid, word):
    filename = file_existing_check(serverid)
    try:
        if os.path.isfile(filename):
            with open(filename, 'r', encoding='UTF-8') as readingcsvfile:
                csvreader = csv.reader(readingcsvfile)
                for line in list(csvreader):
                    if word in line[0]:
                        status = True
                    else:
                        word_generator(serverid, word)
                        status = False
    except Exception:
        status = False
    return status


# Reading all the contents in the CSV file.
def file_read_all(serverid):
    filename = file_existing_check(serverid)
    contents = []
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='UTF-8') as readingcsvfile:
            csvreader = csv.reader(readingcsvfile)
            for line in list(csvreader):
                contents.append(line[0])
    return contents


# Delete a word within the file
def word_delete(file_name, word):
    word_list = []
    try:
        with open(file_name, 'r', newline='', encoding='UTF-8') as file_reading:
            csvreader = csv.reader(file_reading)
            for item in csvreader:
                word_list.append(item)
        with open(file_name, 'w', newline='', encoding='UTF-8') as file_writing:
            csvwriter = csv.writer(file_writing)
            for item in word_list:
                if item != word:
                    csvwriter.writerow(item)
                status = True
    except Exception:
        status = False
    return status


# Clear the complete list
def csv_clear(file_name):
    try:
        with open(file_name, 'w', newline='', encoding='UTF-8') as file_writing:
            csvwriter = csv.writer(file_writing)
            csvwriter.writerow('')
            status = True
    except Exception:
        status = False
    return status


# Main function connecting from the bot command to -
# Add word as well as it's combination to the list on CSV file
def word_add_to_list(serverid, word):
    get_filename = file_existing_check(serverid)
    if get_filename:
        status = word_generator(serverid, word)
    else:
        status = False
    if status:
        embed = discord.Embed(title="Sucess!", description=f"{status}", colour=discord.Color.green())
        return embed
    else:
        embed = discord.Embed(title="Error!", description="Adding word to file failed! Try again maybe?",
                              color=discord.Color.red())
        return embed


# Main function connecting from the bot command to -
# Check if word is present in the list if parameter is passed. If no parameters are passed, return all the contents in the csv file.
def word_check_list(serverid, word=None):
    file_name = file_existing_check(serverid)
    if word:
        if file_name:
            word_check_status = file_read_word(serverid, word)
            if word_check_status:
                embed = discord.Embed(title=f"{word} is already present:", description="This word is already present in the filter list.", colour=discord.Color.green())
                return embed
            else:
                embed = discord.Embed(title=f"{word} is not present:", description="This word is not present in the filter list!", colour=discord.Color.red())
            return embed
    else:
        words = file_read_all(serverid)  # words will have list value. Discord Embed needs string values.
        word_list = '\n'.join(words)
        embed = discord.Embed(title="All words in List:", description="All the available word in this server:",
                              colour=discord.Color.blue())
        embed.add_field(name="", value=word_list)
        # Look into embed word limit once.
        return embed


# Main function connecting from the bot command to -
# Remove a particular word from the list.
def word_delete_list(serverid, word):
    file_name = file_existing_check(serverid)
    # Rocker's suggestion - Convert into list take contents from file, and write it back again.
    status = False
    if file_name:
        status = word_delete(file_name, word)
    if status:
        embed = discord.Embed(title="Successful", description=f"{word}, is deleted from the list succesfully!", colour=discord.Color.green())
        return embed
    else:
        embed = discord.Embed(title="Error!", description="Word deleting failed! Try again maybe?", color=discord.Color.red())
        return embed


# Main function connecting from the bot command to -
# Remove a particular word from the list.
def delete_list(serverid):
    file_name = file_existing_check(serverid)
    status = False
    if file_name:
        csv_clear(file_name)
    if status:
        embed = discord.Embed(title="Successful", description=f"The list is cleared now!",
                              colour=discord.Color.green())
        return embed
    else:
        embed = discord.Embed(title="Error!", description="Clearing failed! Try again maybe?",
                              color=discord.Color.red())
        return embed
