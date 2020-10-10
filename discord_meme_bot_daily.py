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
    for i in range(len(startmeme)):
        if startmeme[i] in message.content:
            await message.channel.send("memes will be send")
            print("memes will be send on the given dates")
            while True:
                real_time = datetime.now().strftime('%H:%M:%S')

                if real_time == time_10_00:
                    rand = random.randint(1, 7)
                    if rand == 1:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme1.png'))
                        print("10:00:00")
                        sleep(1)
                    if rand == 2:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme2.png'))
                        print("10:00:00")
                        sleep(1)
                    if rand == 3:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme3.png'))
                        print("10:00:00")
                        sleep(1)
                    if rand == 4:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme4.png'))
                        print("10:00:00")
                        sleep(1)
                    if rand == 5:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme5.png'))
                        print("10:00:00")
                        sleep(1)
                    if rand == 6:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme6.png'))
                        print("10:00:00")
                        sleep(1)

                if real_time == time_12_00:
                    rand = random.randint(1, 7)
                    if rand == 1:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme1.png'))
                        print("12:00:00")
                        sleep(1)
                    if rand == 2:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme2.png'))
                        print("12:00:00")
                        sleep(1)
                    if rand == 3:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme3.png'))
                        print("12:00:00")
                        sleep(1)
                    if rand == 4:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme4.png'))
                        print("12:00:00")
                        sleep(1)
                    if rand == 5:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme5.png'))
                        sleep(1)
                    if rand == 6:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme6.png'))
                        print("12:00:00")
                        sleep(1)

                if real_time == time_15_30:
                    rand = random.randint(1, 7)
                    if rand == 1:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme1.png'))
                        print("15:30:00")
                        sleep(1)
                    if rand == 2:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme2.png'))
                        print("15:30:00")
                        sleep(1)
                    if rand == 3:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme3.png'))
                        print("15:30:00")
                        sleep(1)
                    if rand == 4:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme4.png'))
                        print("15:30:00")
                        sleep(1)
                    if rand == 5:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme5.png'))
                        print("15:30:00")
                        sleep(1)
                    if rand == 6:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme6.png'))
                        print("15:30:00")
                        sleep(1)

                if real_time == time_18_30:
                    rand = random.randint(1, 7)
                    if rand == 1:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme1.png'))
                        print("18:30:00")
                        sleep(1)
                    if rand == 2:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme2.png'))
                        print("18:30:00")
                        sleep(1)
                    if rand == 3:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme3.png'))
                        print("18:30:00")
                        sleep(1)
                    if rand == 4:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme4.png'))
                        print("18:30:00")
                        sleep(1)
                    if rand == 5:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme5.png'))
                        print("18:30:00")
                        sleep(1)
                    if rand == 6:
                        await message.author.send(file=discord.File('E:/Pyton Programme/Meme/Meme6.png'))
                        print("18:30:00")
                        sleep(1)


client.run("NzYxNjExNjc5NDMxMjYyMjI4.X3dIJg.9fa6VF_dz_v74kWgpELGmkzb81A")