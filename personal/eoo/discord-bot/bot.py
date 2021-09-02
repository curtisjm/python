import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


# print(os.environ)
# print(os.environ.get("TOKEN"))
client.run("ODgyODMxODg4NTUxNjczODY2.YTBHRA.1MH2RaEc2G_4vWDdrbHN-v3J4dg")
# client.run(os.getenv("TOKEN"))
