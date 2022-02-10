# Fixed Random Word Generator

from imports import *

# Remember to make a directory called Server_Files so that the bot can write/refer contents from.


# Function to read contents from JSON in the form of a dictionary.
def read_json_special_characters():
    with open('special_characters.json') as json_reading:
        return json.load(json_reading)


special_letters = read_json_special_characters()


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


# Main function to check if the word exists in the list. Or display the entire list.
def json_file_read_word(filename: str, word=None):
    try:
        if not os.path.isfile(filename):
            embed = discord.Embed(title="Oh Noo~!", description=f"There's nothing but dust here 💨!",
                                  colour=discord.Color.red())
            return embed
        if word:
            if os.path.isfile(filename):
                with open(filename) as reading_json:
                    data = json.load(reading_json)
                    if word in data.keys():
                        embed = discord.Embed(title="It exists!", description=f"The {word} is already in the filter list!",
                                              colour=discord.Color.blue())
                        return embed
        else:
            if os.path.isfile(filename):
                with open(filename) as reading_json:
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


# Main calling function to delete a word from the list or to clear the entire list.
def json_word_delete(filename: str, word=None):
    try:
        if word:
            with open(filename) as jsonfile_reading:
                word_data = json.load(jsonfile_reading)
            if word not in word_data.keys():  # When the word does not exist.
                embed = discord.Embed(title='Wait a minute..', description='Are you sure that word exist in the list? Check once more!', colour=discord.Color.red())
                return embed
        with open(filename, 'w') as jsonfile_writing:
            if word:
                del word_data[word]  # Can use pop or del to delete a key and contents from the JSON file.
            else:
                with open(filename, 'w') as jsonfile_clearing:
                    json.dump({}, jsonfile_clearing, indent=4)  # json.clear() returns error since there should always be something in the json file. For this instance {} (Empty Dictionary)
                embed = discord.Embed(title="Sucess!", description=f"The list is now clear!", colour=discord.Color.green())
                return embed
            json.dump(word_data, jsonfile_writing, indent=4)
            embed = discord.Embed(title="Sucess!", description=f"Deleted {word} from list successfully!",
                                  colour=discord.Color.green())
            return embed
    except Exception:
        embed = discord.Embed(title="Oops!", description="Some error occured, try again!",
                              color=discord.Color.red())
        return embed
