from check import *
import asyncio
import disnake
from disnake.ext import commands
from disnake.ui import Select, Button

auto = False
bot = commands.Bot(command_prefix="^", intents=disnake.Intents.all(), help_command=None)

async def auto_check_task(ctx, delay):
    while auto:

        if up():        
            await ctx.send("you node restart in " + str(delay) + " seconds.")
            await asyncio.sleep(delay)
        else:
            await ctx.send("somthing wrong")    
@bot.command()
async def auto_start(ctx, delay=600):
    global auto
    await ctx.send("Auto check started.")
    auto = True
    await auto_check_task(ctx, delay)

@bot.command()
async def auto_stop(ctx):
    global auto
    auto = False
    await ctx.send("Auto check stopped.")

bot.run()
