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

@bot.command()
async def comoropa(ctx):
    await ctx.send("Como reciclar ropa: La producción de materias primas: las prendas se producen a partir de materias primas como el poliéster, el algodón, la seda o la lana. Algunas de ellas se derivan de recursos no renovables, como el petróleo, para producir fibras sintéticas, mientras que otras se derivan de materiales vegetales o animales y, por tanto, requieren mucha agua y productos químicos. La fabricación de la ropa: debido a las sustancias que contiene, el tinte es tóxico no sólo para los trabajadores que fabrican la ropa, sino también para los consumidores y el ecosistema acuático que contamina. El transporte de la ropa: generalmente se fabrica en países en vías de desarrollo, donde los costes de producción y los sueldos son más bajos, y la ropa se transporta a España por aire o por mar. Sin embargo, el avión es el medio de transporte más contaminante. El mantenimiento de la ropa: el consumo excesivo de agua, al lavar la ropa se desprenden un gran número de micropartículas contaminantes. El reciclaje de la ropa usada: se trata de un paso crucial. Clasificar su armario y reciclar ciertas prendas usadas ayuda a prolongar la vida útil del textil, y así evitar pasos innecesarios como la producción de materias primas, la fabricación de productos o incluso el transporte.                                                                                           Paginas recomendadas: https://www.ecoembes.com/es /                         https://www.reciclaconsciente.pe/")      
   
bot.run("token")
