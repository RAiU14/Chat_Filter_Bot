from imports import *
from discord.ext import commands
from dotenv import load_dotenv

# Create a .env file and add your discord token as DISCORD_TOKEN for the bot to run. Package for dotevn have to be installed as well
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

now = datetime.datetime.now()
t1 = time.perf_counter()
messageid = []

client = commands.Bot(command_prefix="&")
client.remove_command('help')


async def athchk(ctx):
    return ctx.author == client.user


@client.event
async def on_ready():
    print(f'{client.user} is connected to Discord on the following guild:\n')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        print(f'{guild.name}(id: {guild.id})')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="Type &help or &commands"))  # .idle,.online,.dnd


@client.command(name='invite')
async def inv(ctx):
    if await athchk(ctx):
        return
    else:
        await ctx.reply(embed=discord.Embed(title="Invite me using this link!", url="https://discord.com/api/oauth2/authorize?client_id=936259816572198912&permissions=8&scope=bot", color=ctx.author.color))


# Word Filter starts from here

# Comamnds for JSON file handlings for adding/removing words in the filter list.
# Comman Call for checking if the word exist in the filter list.
@client.command(name='wfcheck')
async def wfcheck(ctx):
    if await athchk(ctx):
        return
    word = None
    args = ctx.message.content.split(' ')
    if len(args) > 1:
        word = args[-1]
    word_list_status = words.json_file_read_word(f'./Server_Files/{ctx.message.guild.id}.json', word)
    msg = await ctx.reply(embed=word_list_status)
    await msg.add_reaction(
        "🪄")  # This and the following reactions does not do anything as of now, the code is supposed to delete the msg.


# Command Call for adding a word to the list.
@client.command(name='wfadd')
async def wfadd(ctx):
    if await athchk(ctx):
        return
    else:
        if len(ctx.message.content.split(' ')) == 1:
            msg = await ctx.reply("Oops you forgot to mention what word to add! Try again")
        else:
            writing_status = words.json_file_write(f'./Server_Files/{ctx.message.guild.id}.json', {
                ctx.message.content.split(' ')[1]: words.word_generator(ctx.message.content.split(' ')[1])})
            msg = await ctx.reply(embed=writing_status)
        await msg.add_reaction("🪄")


# Command Call for deleting a word to the list.
@client.command(name='wfdelete')
async def wfdelete(ctx):
    if await athchk(ctx):
        return
    word = None
    args = ctx.message.content.split(' ')
    if len(args) > 1:
        word = args[-1]
    if not word:
        def check(message):  # Checking if the author was the same one who triggered the message and if it is in the same channel.
            return (message.author == ctx.message.author) and (message.channel == ctx.message.channel)
        confirmation_embed = discord.Embed(title="Confirmation", description="You are about to clear the complete list of this server", colour=discord.Colour.orange())
        confirmation_embed.add_field(name="To Confirm", value="Type `Yes`/`yes`/`Y`/`y`", inline=True)
        confirmation_embed.add_field(name="To Cancel", value="Type `No`/`no`/`N`/`n`", inline=True)
        confirmation_embed.set_footer(text="Default time out in 30 seconds!⏱️")
        msg = await ctx.message.channel.send(embed=confirmation_embed)
        await msg.add_reaction("🪄")
        try:
            user_response = await client.wait_for('message', check=check, timeout=30)
            if user_response.content in ('Yes', 'yes', 'y', 'Y'):
                delete_status = words.json_word_delete(f'./Server_Files/{ctx.message.guild.id}.json')
                msg = await ctx.message.channel.send(embed=delete_status)
            else:
                msg = await ctx.message.channel.send("That was close!")
        except asyncio.TimeoutError:
            msg = await ctx.message.channel.send("You missed the window!\nExiting Menu..")
    else:
        delete_status = words.json_word_delete(f'./Server_Files/{ctx.message.guild.id}.json', word)
        msg = await ctx.reply(embed=delete_status)
    await msg.add_reaction("🪄")


# Server based settings, starts from here.

# To add channel to ignore list.
@client.command(name='ichadd')
async def ichadd(ctx):
    if await athchk(ctx):
        return
    if len(ctx.message.content.split(' ')) == 1:
        channel_add_status = server_settings.add_ignore_channels(f'Server_Settings/{ctx.message.guild.id}.json', [ctx.message.channel])
    else:
        channel_add_status = server_settings.add_ignore_channels(f'Server_Settings/{ctx.message.guild.id}.json', ctx.message.channel_mentions)
    msg = await ctx.reply(embed=channel_add_status)
    await msg.add_reaction("🪄")


# Delete channels from ignore list
@client.command(name='ichdel')
async def ichdel(ctx):
    if await athchk(ctx):
        return
    if len(ctx.message.content.split(' ')) == 1:
        def check(message):  # Checking if the author was the same one who triggered the message and if it is in the same channel.
            return (message.author == ctx.message.author) and (message.channel == ctx.message.channel)
        confirmation_embed = discord.Embed(title="Confirmation", description="You are about to clear the complete ignore channel list of this server", colour=discord.Colour.orange())
        confirmation_embed.add_field(name="To Confirm", value="Type `Yes`/`yes`/`Y`/`y`", inline=True)
        confirmation_embed.add_field(name="To Cancel", value="Type `No`/`no`/`N`/`n`", inline=True)
        confirmation_embed.set_footer(text="Default time out in 30 seconds!⏱️")
        msg = await ctx.message.channel.send(embed=confirmation_embed)
        await msg.add_reaction("🪄")
        try:
            user_response = await client.wait_for('message', check=check, timeout=30)
            if user_response.content in ('Yes', 'yes', 'y', 'Y'):
                delete_status = server_settings.del_ingored_channel(f'Server_Settings/{ctx.message.guild.id}.json')
                msg = await ctx.message.channel.send(embed=delete_status)
            else:
                msg = await ctx.message.channel.send("That was close!")
        except asyncio.TimeoutError:
            msg = await ctx.message.channel.send("You missed the window!\nExiting Menu..")
    else:
        delete_status = server_settings.del_ingored_channel(f'Server_Settings/{ctx.message.guild.id}.json', ctx.message.channel_mentions)
        msg = await ctx.reply(embed=delete_status)
    await msg.add_reaction("🪄")


# Add role to ignore list.
@client.command(name='iradd')
async def iradd(ctx):
    if await athchk(ctx):
        return
    if len(ctx.message.content.split(' ')) == 1:
        msg = await ctx.channel.reply('Woah, I think you missed to mention the role/roles.')
    else:
        role_add_status = server_settings.add_ignore_roles(f'Server_Settings/{ctx.message.guild.id}.json', ctx.message.role_mentions)
        msg = await ctx.reply(embed=role_add_status)
    await msg.add_reaction("🪄")


# Delete role from ignore list
@client.command(name='irdel')
async def irdel(ctx):
    if await athchk(ctx):
        return
    if len(ctx.message.content.split(' ')) == 1:
        def check(message):  # Checking if the author was the same one who triggered the message and if it is in the same channel.
            return (message.author == ctx.message.author) and (message.channel == ctx.message.channel)
        confirmation_embed = discord.Embed(title="Confirmation", description="You are about to clear the complete ignore channel list of this server", colour=discord.Colour.orange())
        confirmation_embed.add_field(name="To Confirm", value="Type `Yes`/`yes`/`Y`/`y`", inline=True)
        confirmation_embed.add_field(name="To Cancel", value="Type `No`/`no`/`N`/`n`", inline=True)
        confirmation_embed.set_footer(text="Default time out in 30 seconds!⏱️")
        msg = await ctx.message.channel.send(embed=confirmation_embed)
        await msg.add_reaction("🪄")
        try:
            user_response = await client.wait_for('message', check=check, timeout=30)
            if user_response.content in ('Yes', 'yes', 'y', 'Y'):
                delete_status = server_settings.del_ingored_roles(f'Server_Settings/{ctx.message.guild.id}.json')
                msg = await ctx.message.channel.send(embed=delete_status)
            else:
                msg = await ctx.message.channel.send("That was close!")
        except asyncio.TimeoutError:
            msg = await ctx.message.channel.send("You missed the window!\nExiting Menu..")
    else:
        delete_status = server_settings.del_ingored_roles(f'Server_Settings/{ctx.message.guild.id}.json', ctx.message.channel_mentions)
        msg = await ctx.reply(embed=delete_status)
    await msg.add_reaction("🪄")


# View ignored roles/channels
@client.command(name='igview')
async def igview(ctx):
    if await athchk(ctx):
        return
    try:
        args = ctx.message.content.split(' ')[1]
        if len(ctx.message.content.split(' ')) == 1:
            msg = await ctx.reply("Oops you forgot to mention what word to add! Try again")
            await msg.add_reaction("🪄")
        else:
            if args == 'channel':
                channels = server_settings.view_ignored(f'Server_Settings/{ctx.message.guild.id}.json', 'channel')
                embed = discord.Embed(title='Ignored channels', description='Here is the list of all the ignored channels in this server!', colour=discord.Colour.blue())
                if not channels:
                    msg = await ctx.channel.send("I ran into some error! Try again maybe?")
                    await msg.add_reaction("🪄")
                for item in channels:
                    embed.add_field(name=client.get_channel(item), value=f"ID: {item}")
                await ctx.reply(embed=embed)
            elif args == 'role':
                roles = server_settings.view_ignored(f'Server_Settings/{ctx.message.guild.id}.json', 'role')
                embed = discord.Embed(title='Ignored roles', description='Here is the list of all the ignored role in this server!',                                       colour=discord.Colour.blue())
                if not roles:
                    msg = await ctx.channel.send("I ran into some error! Try again maybe?")
                    await msg.add_reaction("🪄")
                for item in roles:
                    embed.add_field(name=ctx.guild.get_role(item), value=f"ID: {item}")
                await ctx.reply(embed=embed)
            else:
                msg = await ctx.channel.send(f"I don't think I have details of those.")
                await msg.add_reaction("🪄")
    except Exception:
        msg = await ctx.channel.send("I ran into some error! Try again maybe?")
        await msg.add_reaction("🪄")


# @client.event() to call the reaction element and then get the payload from that message with reaction to make actions on that message.

# Event listener starts from here

# Used to check if sent message is a bot command or not.
def is_command(msg):
    bot_commands = ('&wfcheck', '&wfadd', '&wfdelete')
    if any(msg.startswith(i) for i in bot_commands):  # any can be used as a or operator
        return True
    else:
        return False


# This is used to make the bot read every messsage sent on the server.
@client.listen('on_message')
async def msg_check(message):
    server_id = message.channel.guild.id
    channel = message.channel
    author_roles = []
    for item in message.author.roles:  # getting all roles of author as object in form of list
        author_roles.append(item.id)
    try:
        with open(f"Server_Settings/{server_id}.json") as data_reading:
            ignore_data = json.load(data_reading)
            channel_ids = ignore_data['channel_id']
            role_ids = ignore_data['role_id']
        if message.channel.id in channel_ids:
            return
        for item in author_roles:
            if item in role_ids:
                return
        if is_command(message.content):
            return
        with open(f"Server_Files/{server_id}.json") as data_reading:  # To get banned word data
            server_data = json.load(data_reading)
        for key in server_data.keys():
            for item in server_data[key]:
                if item in message.content.split():  # Splitting the words in a message to check if the word is present in the message.
                    await message.delete()
                    msg = await channel.send(f'{message.author.mention}, That word is banned!')
                    await msg.add_reaction("🪄")
    except discord.Forbidden:  # If the bot does not have enough permissions to delete the message.
        msg = await channel.send("I do not have enough permission to delete messages!")
        await msg.add_reaction("🪄")
    except Exception:
        msg = await channel.send("I ran into some error! I was unable to delete that message!")
        await msg.add_reaction("🪄")


# Help command in the bot
@client.command(name='help')
async def helps(ctx):
    if await athchk(ctx):
        return
    hlp_cmd = None
    args = ctx.message.content.split(' ')
    try:
        if len(args) > 1:
            hlp_cmd = args[-1]
        if not hlp_cmd:
            hlps = help_commands.help_cmd()
            msg = await ctx.channel.send(embed=hlps)
        else:
            hlps = help_commands.help_cmd(hlp_cmd)
            msg = await ctx.channel.send(embed=hlps)
    except Exception:
        msg = await ctx.channel.send("I ran into some error! I was unable to delete that message!")
    await msg.add_reaction("🪄")

# To add:
# - Only admins/users with role permission of administrator or manage message can or should invoke most of the bot comamnds except viewing.
# - Feature to add/remove combination of special letter from JSON file
# - Add a generic ban word list option
#   - Option to add it or remove the generic ban word list
# - Add server logging feature
#   - Log a user's ban word usage (counter)
#   - Word usage counter (Think if you need this, make it optional logging feature else.)

client.run(TOKEN)
