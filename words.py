# Fixed Random Word Generator
from imports import *

fieldname = ['Word', 'Similars']


# Function to read contents from JSON in the form of a dictionary.
def read_json_special_characters():
    with open('special_characters.json') as json_reading:
        return json.load(json_reading)


special_letters = read_json_special_characters()


# Try to make everythin in JSON format instead of CSV
# Checking if server based CSV file exists in the directory or not.
def file_existing_check(serverid):
    if not os.path.isdir("Server_Files"):
        os.mkdir("Server_Files")
    file_name = f"./Server_Files/{serverid}.csv"
    return file_name
# Try to get rid of this function


def combine1(tpl):
    t = ""
    for i in tpl:
        t += i
    return t


# Generate and return possible word combinations
def word_generator(word):
    temp = []
    for each_letter in word.lower():
        temp.append(special_letters[each_letter])
    generated_words = list(map(combine1, itertools.product(*temp)))
    return generated_words


# Main calling function for Writing/Appending contents to json file.
# Passing filename along with path from the runbot.py
def json_file_write(filename: str, data: dict):
    try:
        if os.path.isfile(filename):
            with open(filename) as reading_json:
                curr_data = json.load(reading_json)
            curr_data.update(data)
            with open(filename, 'w') as writing_json:
                json.dump(curr_data, writing_json, indent=4)  # indent is used to indent in the json file.
            embed = discord.Embed(title="Sucess!", description=f"Added {list(data.keys())[0]} to list successfully!",
                                  colour=discord.Color.green())
            return embed
        else:
            with open(filename, 'w') as writing_json:
                json.dump(data, writing_json, indent=4)
            embed = discord.Embed(title="Sucess!", description=f"Added {list(data.keys())[0]} to list successfully!",
                                  colour=discord.Color.green())
            return embed
    except Exception:
        embed = discord.Embed(title="Error!", description="Adding word to file failed! Try again maybe?",
                              color=discord.Color.red())
        return embed


# Main function to check if the word is existing in the filter list.
# Reading contents in the list
def json_file_read_word(filename, word=None):
    try:
        if word:
            if os.path.isfile(filename):
                with open(filename, 'r') as reading_json:
                    data = json.load(reading_json)
                    if word in data.keys():
                        embed = discord.Embed(title="It exists!", description=f"The {word} is already in the filter list!",
                                              colour=discord.Color.blue())
                        return embed
        else:
            if os.path.isfile(filename):
                with open(filename, 'r') as reading_json:
                    data = json.load(reading_json)
                    contents = list(data.keys())
                if contents:
                    embed = discord.Embed(title="Here's the contents of the list-", description=f"{contents}",
                                          colour=discord.Color.green())
                else:
                    embed = discord.Embed(title="Oh Noo~!", description=f"There's nothing but dust here 💨!",
                                          colour=discord.Color.red())
                return embed
    except Exception:
        embed = discord.Embed(title="Oops!", description="Some error occured, try again!",
                              color=discord.Color.red())
        return embed


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
                if item[0] != word:  # Used to check if first element of the list is equal to the word to be deleted.
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
# Remove a particular word from the list.
def word_delete_list(serverid, word):
    file_name = file_existing_check(serverid)
    # Rocker's suggestion - Convert into list take contents from file, and write it back again.
    status = False
    if file_name:
        status = word_delete(file_name, word)
    if status:
        embed = discord.Embed(title="Successful", description=f"{word}, is deleted from the list succesfully!",
                              colour=discord.Color.green())
        return embed
    else:
        embed = discord.Embed(title="Error!", description="Word deleting failed! Try again maybe?",
                              color=discord.Color.red())
        return embed


# Main function connecting from the bot command to -
# Remove all the words from the list.
def word_clear_list(serverid):
    file_name = file_existing_check(serverid)
    status = False
    if file_name:
        status = csv_clear(file_name)
    if status:
        embed = discord.Embed(title="Successful", description=f"The list is cleared now!",
                              colour=discord.Color.green())
        return embed
    else:
        embed = discord.Embed(title="Error!", description="Clearing failed! Try again maybe?",
                              color=discord.Color.red())
        return embed
