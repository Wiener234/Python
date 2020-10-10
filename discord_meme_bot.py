import discord
import random
from time import sleep
from datetime import datetime

client = discord.Client()

startmeme = ["!daily memes"]
keywords = ["!meme"]

time_10_00 = "10:00:00"
time_12_00 = "12:00:00"
time_15_30 = "15:30:00"
time_18_30 = "18:30:00"


@client.event
async def on_message(message):
    for j in range(len(keywords)):
        if keywords[j] in message.content:
            rand = random.randint(1, 7)
            if rand == 1:
                await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme1.png'))
                print("Meme send")
                sleep(1)
            if rand == 2:
                await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme2.png'))
                print("Meme send")
                sleep(1)
            if rand == 3:
                await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme3.png'))
                print("Meme send")
                sleep(1)
            if rand == 4:
                await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme4.png'))
                print("Meme send")
                sleep(1)
            if rand == 5:
                await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme5.png'))
                print("Meme send")
                sleep(1)
            if rand == 6:
                await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme6.png'))
                print("Meme send")
                sleep(1)


client.run("NzU5NzczNzc1ODcyNTI0Mjg5.X3CYeA.JE_4l8l_vDjVbg9p-VJCzaJEfZw")
