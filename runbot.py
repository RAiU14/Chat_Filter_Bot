from imports import *
from discord.ext import commands
from dotenv import load_dotenv

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


@client.command(name='wfilter')
async def wfilter(ctx):
    if await athchk(ctx):
        return
    else:
        return


client.run(TOKEN)
