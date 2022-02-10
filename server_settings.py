from imports import *


# Adds a list of ignored channels to JSON file.
def ignore_channels(filename, channelid):
    with open(f'Server_Settings/{filename}.json', 'w') as json_writing:
        json.dump(channelid, json_writing, indent=4)
    return


# Adds a list of ignored roles to JSON file.
def ignore_roles(filename, roleid):
    with open(f'Server_Settings/{filename}.json', 'w') as json_writing:
        json.dump(roleid, json_writing, indent=4)
    return
