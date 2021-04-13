import discord
client = discord.Client()
trigger = 'spam'
length = len(trigger)

@client.event
async def on_message(message):
    for i in range(length):
        if trigger[i] in message.content:
            for j in range(10):
                await message.channel.send("Spam test")

client.run("TOKEN_HERE")
