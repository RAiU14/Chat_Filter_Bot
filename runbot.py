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
    await client.change_presence(status=discord.Status.dnd,
                                 activity=discord.Activity(type=discord.ActivityType.listening,
                                                           name="Type &help or &commands"))  # .idle,.online,.dnd


@client.command(name='invite')
async def inv(ctx):
    if await athchk(ctx):
        return
    else:
        await ctx.reply(embed=discord.Embed(title="Invite me using this link!",
                                            url="https://discord.com/api/oauth2/authorize?client_id=936259816572198912&permissions=8&scope=bot",
                                            color=ctx.author.color))


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
    await msg.add_reaction("🪄")  # This and the following reactions does not do anything as of now, the code is supposed to delete the msg.


# Command Call for adding a word to the list.
@client.command(name='wfadd')
async def wfadd(ctx):
    if await athchk(ctx):
        return
    else:
        if len(ctx.message.content.split(' ')) == 1:
            msg = await ctx.reply("Oops you forgot to mention what word to add! Try again")
        else:
            writing_status = words.json_file_write(f'./Server_Files/{ctx.message.guild.id}.json', {ctx.message.content.split(' ')[1]: words.word_generator(ctx.message.content.split(' ')[1])})
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
        await ctx.message.channel.send("Are you sure you want to clear the list?\nYes/yes(Y/y) or No/no(N/n)?\nDefault Timeout in 30 seconds⏱️!")  # Make into embed later
        user_response = await client.wait_for('message', check=check, timeout=30)
        if user_response.content in ('Yes', 'yes', 'y', 'Y'):
            delete_status = words.json_word_delete(f'./Server_Files/{ctx.message.guild.id}.json')
            msg = await ctx.message.channel.send(embed=delete_status)
        else:
            msg = await ctx.message.channel.send("That was close!")
    else:
        delete_status = words.json_word_delete(f'./Server_Files/{ctx.message.guild.id}.json', word)
        msg = await ctx.reply(embed=delete_status)
    await msg.add_reaction("🪄")


def is_command(msg):
    bot_commands = ('&wfcheck', '&wfadd', '&wfdelete')
    if any(msg.startswith(i) for i in bot_commands):  # any can be used as a or operator
        return True
    else:
        return False

# @client.event() to call the reaction element and then get the payload from that message with reaction to make actions on that message.


# This is used to make the bot read every messsage sent on the server.
@client.listen('on_message')
async def msg_check(message):
    server_id = message.channel.guild.id
    channel = message.channel
    author = message.author
    msg = message.content.split()  # Splitting the words in a message to check if the word is present in the message.
    try:
        if is_command(message.content):
            return
        filename = f"Server_Files/{server_id}.json"
        with open(filename) as data_reading:
            server_data = json.load(data_reading)
        for key in server_data.keys():
            for item in server_data[key]:
                if item in msg:
                    await message.delete()
                    await channel.send(f'{author.mention}, That word is banned!')
    except discord.Forbidden:  # If the bot does not have enough permissions to delete the message.
        await channel.send("I do not have enough permission to delete messages!")
    except Exception:
        await channel.send("I ran into some error! I was unable to delete that message!")
client.run(TOKEN)
