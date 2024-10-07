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

@bot.command()
async def quieneres(ctx):
    await ctx.send("¿Quien soy? soy un reciclador que quiere mejorar el medio ambiente de todo el mundo y me apasiona me llamo mateo")

@bot.command()
async def Help(ctx):
    await ctx.send("ayuda. para cada comando que escribas lo tienes que empezar con $ Ejemplo $ayuda; puedes escribir los comandos siguientes: quieneres datos ropa y reciclaje")


bot.run("Token")
