from imports import *


# Think about converting this to a JSON file. It will be easy to read and display contents.
def help_cmd(command=None):
    if not command:
        embed = discord.Embed(title="All the commands available", description="Here are all the commands available to use", colour=discord.Colour.blue())  # Can give `url='link'` after title.
        # embed.set_thumbnail()
        embed.add_field(name="wfcheck", value="Use this command view a single or all the text available in the list.\nUsage: `&wfcheck (word)` To check if a word exist in the list or not. This will give 'Yes' or 'No'\n`&wfcheck` This will view the entire list.", inline=False)
        embed.add_field(name="wfadd", value="Use this command add or insert a new word to the filter list.\nUsage:\n`&wfadd (word)` This will add a word to the filter list.\nNote that this will only work if you add a word, just using the command will result an error!", inline=False)
        embed.add_field(name="wfdelete", value="Use this delete an existing word from the filter list.\nUsage:\n`&wfdelete (word)` This will delete the mentioned word from the existing filter list.\nNote that this will only work if you add a word, just using the command will result an error!", inline=False)
        embed.add_field(name="invite", value="Use this command to get an invitation link to invite the bot to your server.", inline=False)
        embed.add_field(name="help", value="Use this command to available commands of the bot or along with the command name to view what that individual command does.", inline=False)
    else:
        if command == 'wfcheck':
            embed = discord.Embed(title="wfcheck", description="Use this command view a single or all the text available in the list.\nUsage: `&wfcheck (word)` To check if a word exist in the list or not. This will give 'Yes' or 'No'\n`&wfcheck` This will view the entire list.")
        elif command == 'wfadd':
            embed = discord.Embed(title="wfadd", description="Use this command add or insert a new word to the filter list.\nUsage:\n`&wfadd (word)` This will add a word to the filter list.\nNote that this will only work if you add a word, just using the command will result an error!")
        elif command == 'wfdelete':
            embed = discord.Embed(title="wfdelete", description="Use this delete an existing word from the filter list.\nUsage:\n`&wfdelete (word)` This will delete the mentioned word from the existing filter list.\nNote that this will only work if you add a word, just using the command will result an error!")
        elif command == 'invite':
            embed = discord.Embed(title="invite", description="Use this command to get an invitation link to invite the bot to your server.")
        else:
            embed = discord.Embed(title="What again?", description="I do not have any command like that!", colour=discord.Colour.red())
    return embed
