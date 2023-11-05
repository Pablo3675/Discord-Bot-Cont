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
    await ctx.send(f"Hola, soy un bot para combatir la contaminación!\n*Para conocer mi lista de comandos escribe $Help.*")

@bot.command()
async def objetivo(ctx):
    await ctx.send("Mi objetivo es motivar a los adolescentes a cuidar el medio ambiente conscientizando y dar ideas para reducir los desechos que se producen cada día.")

@bot.command()
async def time(ctx):
    Time_D = ["Residuos orgánicos: 4 semanas", "Papel y Cartón: 1 año", "Aluminio: 10 años", "Plástico: 150 años", "Vidrio: 4000 años", "Bolsas: 20 años", "Sorbetes: 200 años", "Botellas de plástico: 450 años"]
    await ctx.send(random.choice(Time_D))

@bot.command()
async def consejo(ctx):
    consejo_list = ["Recicla cartón, papel y plástico", "Reutiliza", "Apaga las luces cuando no las utilices", "Reduce el uso de plástico", "Reutiliza los materiales para hacer manualidades", "No tires basura en la calle", "Cuida la naturaleza", "Planta un árbol"]
    await ctx.send(random.choice(consejo_list))

@bot.command()
async def game(ctx):
    await ctx.send("En este juego el que que consiga el desecho con menos tiempo de descomposición usando el comando **$time** gana 1 punto, el que llegue a 3 puntos gana la partida.")
    

@bot.command()
async def Help(ctx):
    await ctx.send("Mi lista de comandos es:\n1- $hola\n2- $objetivo\n3- $time\n4- $consejo\n5- $game")


bot.run("TOKEN HERE")
