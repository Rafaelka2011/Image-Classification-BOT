import discord
from discord.ext import commands

from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents = discord.Intents.default())

@bot.event
async def on_ready():
    print(f'I {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send('Вы забыли загрузить картинку')

bot.run('MTIwMTA3ODk2NTk2MDQ0NTk5Mg.GZtvLu.vuofn3wdnGxzGXt4WoofQao0xqRzCVcdIdwJus')