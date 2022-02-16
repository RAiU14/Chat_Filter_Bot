from typing import Union
from imports import *


# Adds a channelid to a list of ignored channels into a JSON file.
def add_ignore_channels(filename: str, obj: Union[int, list]):
    channelid = []
    for item in obj:
        channelid.append(item.id)
    try:
        data = {'channel_id': [], 'role_id': []}
        if os.path.isfile(filename):
            with open(filename) as json_reading:
                data = json.load(json_reading)
        data['channel_id'].extend(channelid)  # Add more value to the list.
        data['channel_id'] = list(set(data['channel_id']))  # Removes duplicates.
        with open(filename, 'w') as json_writing:
            json.dump(data, json_writing, indent=4)
        embed = discord.Embed(title="Sucess!", description="Added the following channel to ignore list!", colour=discord.Color.green())
        for x in obj:
            embed.add_field(name=x.name, value=x.id)
        return embed
    except Exception:
        embed = discord.Embed(title="Oops!", description="Some error occured, try maybe?",
                              color=discord.Color.red())
        return embed


# Remove a channel id from the list of ignored channels present in the JSON file.
def del_ingored_channel(filename: str, obj: list = None):
    channelid = []
    data = {'channel_id': [], 'role_id': []}
    try:
        if obj is None:
            with open(filename) as json_reading:
                data = json.load(json_reading)
            data['channel_id'].clear()  # This is for removing everything in channel_id. [list.clear() will clear the complete list.]
            with open(filename, 'w') as json_writing:
                json.dump(data, json_writing, indent=4)
            embed = discord.Embed(title='Success!', description="The ignore channel list is now cleared.", colour=discord.Colour.green())
            return embed
        if len(obj) == 1:
            channelid = obj[0].id
        else:
            for item in obj:
                channelid.append(item.id)
        if os.path.isfile(filename):
            with open(filename) as json_reading:
                data = json.load(json_reading)
        if type(channelid) == int:
            data['channel_id'].remove(channelid)  # Used to remove only one value from the key's value.
        elif type(channelid) == list:
            data['channel_id'] = list(set(data['channel_id']) - set(channelid))  # This will delete value from the list.
        with open(filename, 'w') as json_writing:
            json.dump(data, json_writing, indent=4)
        embed = discord.Embed(title="Sucess!", description="Deleted the following channel from the ignore list!",
                              colour=discord.Color.green())
        for x in obj:
            embed.add_field(name=x.name, value=x.id)
        return embed
    except Exception:
        embed = discord.Embed(title="Oops!", description="Some error occured, try maybe?",
                              color=discord.Color.red())
        return embed


# Adds a list of ignored roles to JSON file.
def add_ignore_roles(filename: str, obj: list):
    roleid = []
    try:
        for item in obj:
            roleid.append(item.id)
        data = {'channel_id': [], 'role_id': []}
        if os.path.isfile(filename):
            with open(filename) as json_reading:
                data = json.load(json_reading)
        data['channel_id'].extend(roleid)
        data['channel_id'] = list(set(data['channel_id']))  # Removes duplicates.
        with open(filename, 'w') as json_writing:
            json.dump(data, json_writing, indent=4)
        embed = discord.Embed(title="Sucess!", description="Deleted the following channel from the ignore list!",
                              colour=discord.Color.green())
        for x in obj:
            embed.add_field(name=x.name, value=x.id)
        return embed
    except Exception:
        embed = discord.Embed(title="Oops!", description="Some error occured, try maybe?",
                              color=discord.Color.red())
        return embed


# Remove a role id from the list of ignored role present in the JSON file.
def del_ingored_roles(filename: str, obj: list):
    roleid = []
    if len(obj) == 1:
        roleid = obj[0].id
    else:
        for item in obj:
            roleid.append(item.id)
    data = {'channel_id': [], 'role_id': []}
    if os.path.isfile(filename):
        with open(filename) as json_reading:
            data = json.load(json_reading)
    if type(roleid) == int:
        data['channel_id'].remove(roleid)  # Used to remove only one value from the key's value.
    elif type(roleid) == list:
        data['channel_id'] = list(set(data['channel_id']) - set(roleid))  # This will delete value from the list.
    with open(filename, 'w') as json_writing:
        json.dump(data, json_writing, indent=4)
    embed = discord.Embed(title="Sucess!", description="Deleted the following channel from the ignore list!",
                          colour=discord.Color.green())
    for x in obj:
        embed.add_field(name=x.name, value=x.id)
    return embed
