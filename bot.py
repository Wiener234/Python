import discord
client = discord.Client()

keywords = ["help"]

@client.event
async def on_message(message):
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for j in range(10):
                await message.channel.send("get spammed LOOSER")
client.run("NzU5MTMzMTIxMzE5OTI3ODU5.X25D0A.dADVrXkiW09LaC1NLXZVZcec0PE")