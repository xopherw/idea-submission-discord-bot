import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='$')  # Select a prefix like '$', or '!', or '>'

@bot.command(name='idea') # You can change your command calling name here
async def isb(ctx, arg1, arg2, arg3 = ''):
    channel = bot.get_channel('YOUR-DESIRED-CHANNEL-ID-IN-INTEGER')
    name = ctx.author if(arg3 is '') else arg3
    myEmbed = discord.Embed(title=arg1, description=arg2, color=0x00ff00)
    myEmbed.set_author(name=name)
    await channel.send(embed=myEmbed)

bot.run("YOUR-TOKEN-HERE")
