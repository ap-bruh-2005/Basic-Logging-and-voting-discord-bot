import discord
from discord.ext import commands
import pandas as pd
import csv
import os
import sys
from pytz import timezone
from datetime import datetime
from discord.utils import get


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
path = os.getcwd()

#tz is timezone.Please add the appropriate timezone
tz = "Asia/Kolkata"
list_of_ppl_who_need_access = []

try:
    with open('guild.txt', "r") as f:
        guild_id = f.readline()
except IOError:
    sys.exit("Please run the bot file in the same directory as the tokens.txt file")

try:
    with open('role.txt', "r") as f:
        role_id = f.readline()
except IOError:
    sys.exit("Please run the bot file in the same directory as the tokens.txt file")

try:
    with open('show_file_id.txt', "r") as f:
        id_for_file_acces = f.readline()
except IOError:
    sys.exit("Please run the bot file in the same directory as the tokens.txt file")

try:
    with open('token.txt', "r") as f:
        token = f.readline()
except IOError:
    sys.exit("Please run the bot file in the same directory as the tokens.txt file")


def ppl_who_can_do_stuff():
    list_of_ppl_who_need_access.clear()
    guild = bot.get_guild(int(guild_id))
    
    role = get(guild.roles, id=int(role_id))
    for member in guild.members:
        if role in member.roles:
            list_of_ppl_who_need_access.append(member.id)


if(os.path.isfile('./logging.csv') == False):
       d = pd.DataFrame(columns = ['time', 'message_author', 'message_content'])
       d.to_csv('logging.csv')

try:
    db = pd.read_csv(path + '/logging.csv')
except:
    sys.exit("Error occured regarding the file")




@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def log(ctx, *, arg ):
    author = ctx.author.id
    ppl_who_can_do_stuff()   
    if(author in list_of_ppl_who_need_access):
        # If statement to check if the log is too small(lesser than 4 words), remove if there is no word restriction
        if(len(arg) >= 4):
            with open('logging.csv', 'a') as f:
                init_db = csv.DictWriter(f, ['index','time','message_author', 'message_content'])
                init_db.writerow({'index': db.shape[0],'time': datetime.now(timezone(tz)).strftime('%Y-%m-%d %H:%M:%S.%f'),'message_author' : ctx.message.author.name , 'message_content': arg})
                await ctx.send("Recieved, thank you for sharing your report.")
        else:
            await ctx.send("Report too small or you haven't added spaces")
    else:
        await ctx.send("You dont hv the required roles")
        
        



@bot.command()
async def show_file(ctx):
    await ctx.send(file=discord.File(path + '/logging.csv'))


@bot.command()
async def bot_help(ctx):
    await ctx.send('Do !log <ur work> to log ur work and do !show_file to see the database. To create an anonymous vote do !anonymous_vote <issue>')


@bot.command()
async def anonymous_vote(ctx, arg):
    ppl_who_can_do_stuff()
    author = ctx.author.id
    if(author in list_of_ppl_who_need_access):
        issue = arg 
        if(os.path.isfile(f'./{issue}.csv') == False):
            d = pd.DataFrame(columns = ['content'])
            d.to_csv(f'{issue}.csv')
        ppl_who_can_do_stuff()
        for ppl in list_of_ppl_who_need_access:
            person = bot.get_user(int(ppl))
            await person.send(f"An anonymous vote regarding {issue} has started") 
            await person.send(f"The issue is : {issue}")
            await person.send("If you want to vote do !opinion issue and opinion for example :- !opinion getting_cards I would like one too")
    else:
        await ctx.send("You cannot send this command")

@bot.command()
async def opinion(ctx, *,arg):
    message = arg.split(" ")
    issue = message[0]
    opinion = ' '.join(message[1:])
    if(os.path.isfile(f'./{issue}.csv') == False):
       await ctx.send("No current issue like this present")
    else:
        with open(f'{issue}.csv', 'a') as f:
            init_db = csv.DictWriter(f, ['index','content'])
            init_db.writerow({'index': db.shape[0], 'content': opinion})
            await ctx.send("Thanks for giving your opinion ")

    
@bot.command()
async def show_issue_file(ctx, arg):
    if(ctx.author.id == int(id_for_file_acces)):
        try:
            await ctx.send(file=discord.File(path + f'/{arg}.csv'))
        except:
            await ctx.send("An unexpected error occured or no such file name")
    else:
        await ctx.send("You are not allowed to access the file")



bot.run(token)

 