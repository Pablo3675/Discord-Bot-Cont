import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f"¡Hola jóvenes eco-amigos! 🌍 ¿Están listos para hacer un cambio impactante en nuestro planeta? 💪🌱 Es hora de poner manos a la obra y cuidar nuestro hogar. 🏡❤️\n*Para conocer mi lista de comandos escribe $Help.*")

@bot.command()
async def objetivo(ctx):
    await ctx.send("Mi objetivo es motivar a los adolescentes a cuidar el medio ambiente conscientizando y dar ideas para reducir los desechos que se producen cada día en el mundo. ♻️")

@bot.command()
async def time(ctx):
    Time_D = ["Residuos orgánicos: 4 semanas 🍃", "Papel y Cartón: 1 año 📄", "Aluminio: 10 años 🥫", "Plástico: 150 años 🚯", "Vidrio: 4000 años 🍾", "Bolsas: 20 años 🛍️", "Sorbetes: 200 años 🥤", "Botellas de plástico: 450 años 🍶"]
    await ctx.send(random.choice(Time_D))

@bot.command()
async def consejo(ctx):
    consejo_list = [
                "Recicla cartón, papel y plástico. ♻️📦📄🥤", 
                "Reutiliza. 🔄", 
                "Apaga las luces cuando no las utilices. 💡", 
                "Reduce el uso de plástico. 🥤🚫🌍", 
                "Reutiliza los materiales para hacer manualidades. ✂️🎨", 
                "No tires basura en la calle. 🚯🌳", 
                "Cuida la naturaleza. 🌿❤️", 
                "Planta un árbol. 🌱🌳",
                "Motiva a tus amigos a unirse al cambio. 🤝💪"
            ]
    await ctx.send(random.choice(consejo_list))

@bot.command()
async def chiste(ctx):
    chistes_list = [
                "¿Por qué el árbol estaba siempre relajado?\nPorque tiene raíces profundas y una vida sin contaminantes. 🌳💚",
                "¿Cúal es el chiste favorito de un ecologista?\n¡Que todos los demás son demasiado contaminantes! 😄🌍",
                "¿Por qué el planeta siempre invita a los ecologistas a sus fiestas?\nPorque saben como dejar una huella verde en la pista de baile. 🌎🕺💚"
                "¿Por qué el oceano no está triste?\nPor que no se deja contaminar por pensamientos negativos. 🌊😊💙",
            ]
    await ctx.send(random.choice(chistes_list))


@bot.command()
async def game(ctx):
    await ctx.send("En este juego el que que consiga el desecho con menos tiempo de descomposición usando el comando **$time** gana 1 punto, el que llegue a 3 puntos gana la partida. 🕹️")
    

@bot.command()
async def Help(ctx):
    await ctx.send("Mi lista de comandos es:\n1- $hola\n2- $objetivo\n3- $time\n4- $consejo\n5- $chiste\n6- $game")


bot.run("TOKEN HERE")
