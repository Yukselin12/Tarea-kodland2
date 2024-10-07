import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def ropa(ctx):
    datos = [
        "Hay tanta ropa tirada, no queremos eso entonces siempre intenta vender tu ropa a un precio aceptable, te recomendamos: https://www.mercadolibre.com" 
    ]
    await ctx.send(random.choice(datos))

@bot.command()
async def reciclaje(ctx):
    datos = [
        "El reciclaje es muy pero que muy importante para el planeta tierra por eso te recomendamos: https://www.ecoembes.com/es"
    ]
    await ctx.send(random.choice(datos))

@bot.command()
async def datos(ctx):
    datos = [
        "En https://elcomercio.pe/ Dieron la noticia de que la montaña de basura de pacifico a incrementado su tamaño Mas informacion en: https://elcomercio.pe/tecnologia/ciencias/la-isla-de-basura-en-el-oceano-pacifico-ya-es-mas-grande-que-francia-y-preocupa-a-la-humanidad-noticia/"
    ]
    await ctx.send(random.choice(datos))

bot.run("MTI4NTI2MDE4MDE5OTgzMzY4MQ.GYGW1V.QnI6kJ7opJaonAh76OOBGKQ0pLesjYopv9a0l4")