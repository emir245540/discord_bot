import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def carpma(ctx, sayi1, sayi2 ):
    await ctx.send(f"Sayıların Çarpımı: {int(sayi1) * int(sayi2)}")

@bot.command()
async def bolme(ctx, sayi1, sayi2 ):
    await ctx.send(f"Sayıların Bölümü: {int(sayi1) / int(sayi2)}")


bot.run("Enter The Token")
