import discord
from discord.ext import commands


mod = commands.Bot(command_prefix=".", self_bot=True)
token = "MTIyNjk4NDAyMTI2ODEwNzMzMg.GoLKib.-26XfLaCbmPPfTVzmK32dpH1bWIDsDbUqixbO0"
allowed_ids = {903383862539845632, 1226984021268107332, 1198306139847266476, 733958569589735425, 1030712547969617961}
pack_ids = []


@mod.event
async def on_message(msg):
  if msg.channel.id == 1338670621118304280:
    if msg.author.id == 1169446156825268225:
      if msg.content == "💀":
        await msg.pin()



         





mod.run(token)
