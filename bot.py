import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
	print('The Bot Is Ready!')
	print(bot.user.name)
	print(bot.user.id)
	
@bot.command()
async def sword():
	await bot.say('DIE!')

@bot.command()
async def nub():
	await bot.say('u are nub -_-''')	
			
bot.run('NTQwMTkzMjMxNTYwOTAwNjA4.DzNXNg.T_kBaIOzokaKinBIs_MCkowOxzc')
