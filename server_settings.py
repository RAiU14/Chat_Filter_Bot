import json
import os

from imports import *


# Adds a channelid to a list of ignored channels into a JSON file.
def add_ignore_channels(filename: str, channelid: dict):
    if os.path.isfile(filename):  # File Exist, so add new channel to the dictionary.
        with open(filename) as json_reading:
            curr_data = json.load(json_reading)
        curr_data['channel_id'].append(channelid)  # Something like this works to add more item to the dictionary as a list. This resulted in some error.
        with open(filename, 'w') as json_writing:
            json.dump(curr_data, json_writing, indent=4)
    else:
        with open(filename, 'w') as json_reading:
            json.dump(channelid, json_reading, indent=4)
    return


# Remove a channel id from the list of ignored channels present in the JSON file.
def del_ingored_channel(filename: str, channelid: dict):
    if os.path.isfile(filename):
        with open(filename) as json_reading:
            curr_data = json.load(json_reading)
    return


# Adds a list of ignored roles to JSON file.
def add_ignore_roles(filename: str, roleid):
    with open(f'Server_Settings/{filename}.json', 'w') as json_writing:
        json.dump(roleid, json_writing, indent=4)
    return
