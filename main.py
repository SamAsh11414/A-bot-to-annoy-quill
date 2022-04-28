import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Fuckuquill'):
        x = []
        for i in range(1, 4):
            x.append(await message.channel.send('<@184131251085508608>'))
        await message.channel.purge(limit=len(x)+1)
    if message.content.startswith('!Fuckucheesy'):
        x = []
        for i in range(1, 4):
            x.append(await message.channel.send('<@265290769097687040>'))
        await message.channel.purge(limit=len(x)+1)
    if message.content.startswith('!Fuckubreadboy'):
        x = []
        for i in range(1, 4):
            x.append(await message.channel.send('<@240209707724308481>'))
        await message.channel.purge(limit=len(x)+1)
    if message.content.startswith('!Fuckusam'):
        x = []
        for i in range(1, 4):
            x.append(await message.channel.send('<@472500911936372758>'))
        await message.channel.purge(limit=len(x)+1)
    if message.content.startswith('!Fuckumatt'):
        x = []
        for i in range(1, 4):
            x.append(await message.channel.send('<@78642338703867904>'))
        await message.channel.purge(limit=len(x)+1)
    if message.content.startswith('!Fuckupizza'):
        x = []
        for i in range(1, 4):
            x.append(await message.channel.send('<@689182024539701369>'))
        await message.channel.purge(limit=len(x)+1)

client.run('OTY5MDg0NDIxMzA1MTcxOTk4.YmoQMg.fEFdAk0IsgYsPx9uUgNqj5eWePw')