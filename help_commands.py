from imports import *


# Think about converting this to a JSON file. It will be easy to read and display contents.
def help_cmd(command=None):
    if not command:
        print(command)
        embed = discord.Embed(title="All the commands available", description="Here are all the commands available to use", colour=discord.Colour.blue())  # Can give `url='link'` after title.
        # embed.set_thumbnail()
        embed.add_field(name="wfcheck", value="Use this command view a single or all the text available in the list.\nUsage: `&wfcheck (word)` To check if a word exist in the list or not. This will give 'Yes' or 'No'\n`&wfcheck` This will view the entire list.", inline=False)
        embed.add_field(name="wfadd", value="Use this command add or insert a new word to the filter list.\nUsage:\n`&wfadd (word)` This will add a word to the filter list.\nNote that this will only work if you add a word, just using the command will result an error!", inline=False)
        embed.add_field(name="wfdelete", value="Use this delete an existing word from the filter list.\nUsage:\n`&wfdelete (word)` This will delete the mentioned word from the existing filter list.\nNote: If you use only the command trigger filter clearing and a confirmation!", inline=False)
        embed.add_field(name="ichadd", value="Use this to add a channel to the ignore list. The bot will not delete banned words of these ignored channels.\nUsage:\n`&ichadd (mention a channel or a list of channnels)` This will add the mentioned channel or channels to the ignore list.\nNote: If you do not mention any channel, then the current channel will be added to the ignore list.\nPlease keep in mind that you will have to mention a channel and not write the channel name.", inline=False)
        embed.add_field(name="ichdel", value="Use this to delete a channel from the ignore list.\nUsage:\n`&ichdel (mention a channel or a list of channels)` This will delete the mentioned channel or channels from the ignore list.\nNote: If you do not mention any channel, then the current channel will be deleted from the ignore list.\nPlease keep in mind that you will have to mention a channel and not write the channel name.", inline=False)
        embed.add_field(name="iradd", value="Use this to add a role to the ignore list. The bot will not delete banned words sent by the user having ignored roles.\nUsage:\n`&iradd (mention a role or a list of roles)` This will add the mentioned role or a list roles to the ignore list.\nNote: If you do not mention any channel, then it would result in an error and you will have to trigger the command again.\nPlease keep in mind that you will have to mention a role and not write the role name.", inline=False)
        embed.add_field(name="irdel", value="Use this to delete a role from the ignore list.\nUsage:\n`&ichdel (mention a role or a list of roles)` This will delete the mentioned role or a list of roles from the ignore list.\nNote: If you do not mention any role, then it would result in an error and you will have to trigger the command again.\nPlease keep in mind that you will have to mention a role and not write the role name.", inline=False)
        embed.add_field(name="igview", value="Use tis command to view the ignore list.\nUsage: `&igview (channel/role)` To view the contents present in the ignore list [channels or roles] made for the server settings.", inline=False)
        embed.add_field(name="invite", value="Use this command to get an invitation link to invite the bot to your server.", inline=False)
        embed.add_field(name="help", value="Use this command to available commands of the bot or along with the command name to view what that individual command does.", inline=False)
        # embed.set_footer()
    else:
        if command == 'wfcheck':
            embed = discord.Embed(title="wfcheck", description="Use this command view a single or all the text available in the list.\nUsage: `&wfcheck (word)` To check if a word exist in the list or not. This will give 'Yes' or 'No'\n`&wfcheck` This will view the entire list.")
        elif command == 'wfadd':
            embed = discord.Embed(title="wfadd", description="Use this command add or insert a new word to the filter list.\nUsage:\n`&wfadd (word)` This will add a word to the filter list.\nNote that this will only work if you add a word, just using the command will result an error!")
        elif command == 'wfdelete':
            embed = discord.Embed(title="wfdelete", description="Use this delete an existing word from the filter list.\nUsage:\n`&wfdelete (word)` This will delete the mentioned word from the existing filter list.\nNote that this will only work if you add a word, just using the command will result an error!")
        elif command == 'ichadd':
            embed = discord.Embed(title="ichadd", description="Use this to add a channel to the ignore list. The bot will not delete banned words of these ignored channels.\nUsage:\n`&ichadd (mention a channel or a list of channnels)` This will add the mentioned channel or channels to the ignore list.\nNote: If you do not mention any channel, then the current channel will be added to the ignore list.\nPlease keep in mind that you will have to mention a channel and not write the channel name.")
        elif command == 'ichdel':
            embed = discord.Embed(title="ichdel", description="Use this to delete a channel from the ignore list.\nUsage:\n`&ichdel (mention a channel or a list of channels)` This will delete the mentioned channel or channels from the ignore list.\nNote: If you do not mention any channel, then the current channel will be deleted from the ignore list.\nPlease keep in mind that you will have to mention a channel and not write the channel name.")
        elif command == 'iradd':
            embed = discord.Embed(title="iradd", description="Use this to add a role to the ignore list. The bot will not delete banned words sent by the user having ignored roles.\nUsage:\n`&iradd (mention a role or a list of roles)` This will add the mentioned role or a list roles to the ignore list.\nNote: If you do not mention any channel, then it would result in an error and you will have to trigger the command again.\nPlease keep in mind that you will have to mention a role and not write the role name.")
        elif command == 'irdel':
            embed = discord.Embed(title="irdel", description="Use this to delete a role from the ignore list.\nUsage:\n`&ichdel (mention a role or a list of roles)` This will delete the mentioned role or a list of roles from the ignore list.\nNote: If you do not mention any role, then it would result in an error and you will have to trigger the command again.\nPlease keep in mind that you will have to mention a role and not write the role name.")
        elif command == 'igview':
            embed = discord.Embed(title="igview", description="Use tis command to view the ignore list.\nUsage: `&igview (channel/role)` To view the contents present in the ignore list [channels or roles] made for the server settings.")
        elif command == 'invite':
            embed = discord.Embed(title="invite", description="Use this command to get an invitation link to invite the bot to your server.")
        else:
            embed = discord.Embed(title="Wait a minute!?", description="I do not have any command like that!", colour=discord.Colour.red())
    return embed
