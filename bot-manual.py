### Manual for Bot | Created by Rak
# created for save some time for writing a discord bot
# to use - u have to install discord.py
# requires Python 3.6.x or higher | recomend Python 3.7.x
# - installing discord.py => pip install discord.py
# to laucnh the script, type in CMD/PoweShell/BASH => python name_of_the_script.py
## Have a good time with coding

token = "" # token for your discord bot, can get on => https://discord.com/developers/applications | Just log in with your discord account 
botPrefix = "." # prefix for your Bot commands, "." by default

## None discord.py libraries ##
import os; rm = lambda: os.system("") # *windows - cls | linux - clear*  clearing the terminal, to call it, just type => rm()
import random as Random

## discord.py libraries and extra ##
import discord
from discord.ext import commands
from discord.utils import get
from discord import Game

## Global Variables ##

bot =commands.Bot(command_prefix= f"{botPrefix}") # prefix for commands
bot.remove_command("help") # removing old help command, cause you will have another
botName = "" # bot name which is going to be shown in terminal
botStatus = "" # bot status which is going to be shown when it's onlines
testMsg = "Hello World!" # test msg which appears on test command
helpWindowTitle = "Help" ## Help Window Titel | Change it to whatever you want to be on help window

## Terminal designe
developer = "Rak" # change it to your name
systemOutput = "*" # only for design terminal; "*" by default
discordServer = "Test Server" # change it to your Discord server name
terminalOnStartMsg = f"#Created by {developer}\n#For {discordServer}\n\n# {botName} is now Online! #" # message in Bot Terminal on star, change it to whatever you want

## End of Global Variables ##


## Functions/Methods ##
## End of Functions/Methods ##


## Intro on start (Terminal) and Bot Status
@bot.event
async def on_ready():
    print(terminalOnStartMsg)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(botStatus))


## Bot Commands ##

@bot.command(pass_context =True)
async def help(ds):

    embed = discord.Embed(
        colour = discord.Colour.blue() ## change color of help window
    )
    embed.set_author(name=helpWindowTitle) 
    
    ## Copy this and type into command name and info about command => embed.add_field(name="``` ```", value="", inline=inlineSet)

    inlineSet = False # Do you want commands at same the line? Set True; If you want it as a list - set False 

    ## Commands list in help box
    embed.add_field(name="```.test ```", value="Checking if bot is online", inline=inlineSet) ## ``` ``` these things makes your help window looks better

    await ds.send(embed=embed)

@bot.command(pass_context =True)
async def test(ds): #ds for discord
    await ds.send(f"{testMsg}") # Answers you with a test message


## End of Bot Commands ##


## Bot launch ##
if __name__ == "__main__":
    try:
        rm() # cleaning console before terminal starts
        bot.run(token) # bot goes online with your token
    except KeyboardInterrupt:
        print(f"[{systemOutput}]: 'CTRL-C' is detected! Exiting...") # If you hit ctrl-c in terminal, it will say to you what u did and yee, pretty worthless...

## Thx for using my manual!
