import discord
from discord.ext import commands
import lyricsgenius
import time
import urllib
import json
import os
# from googleapiclient.discovery import build

bot = commands.Bot(command_prefix = ">>")


name = "doggobot.py 1.2 >> github.com/procopylua"
game = discord.Game(name=name)
stream = discord.Streaming(name = name,url = "https://www.twitch.tv/twitch/")

@bot.event                                                                                                              #Launching Doggy
async def on_ready(pass_context = True): # if bot ready(launched), then(then means (:) )
    print("+----------------------------+")
    print("+-EPIC DOGGO SCRIPT LAUNCHED-+")
    print("+----------Alpha 13----------+")
    print("+-----------cheeto-----------+")
    #channel = await bot.fetch_channel("665206516042825768")
    #await channel.send('**---------Bot launched---------\n----------Prefix-[>>]----------**')
    await bot.change_presence(status=discord.Status.online, activity=stream)
  


@bot.command(pass_context = True)                                                                                       #Repeat
async def repeat(ctx,*,t):   
    #  await ctx.message.delete()
    await ctx.send(t)
    print(f'{ctx.author} said `{t}`, and because the command was "repeat", bot has repeated that.')

@bot.event
async def on_member_join(member):
    print(f"{member} has joined a server called '{member.guild}'")

      
@bot.command(pass_context = True)                                                                                       #Ping
async def ping(ctx):
    #   await ctx.message.delete()
    await ctx.send(f'Pong.```css\n {round(bot.latency * 1000)}ms```')
    print(f'{ctx.author} checked the ping of the bot. Its was {round(bot.latency * 1000)}ms.')

import random
hello = ["hi,","howdy,","nice to meet you,","hey,","hello,","what's up,","wyd,","qq,","q,","A MAN HAS FALLEN INTO THE RIVER IN LEGO CITY, THIS MAN WAS"]


@bot.command(pass_context=True)                                                                                       #Hi(first random test)
async def hi(ctx):
    #   await ctx.message.delete()
    await ctx.send(f'{random.choice(hello)} {ctx.author.mention}!')
    print(f'{ctx.author} was greeted by the bot.')
  

memes = [ 
    "https://cdn.discordapp.com/attachments/622469613581631518/675798959662563348/Meme7.png",
    "https://cdn.discordapp.com/attachments/622469613581631518/675798962170626058/Meme1.png",
    "https://cdn.discordapp.com/attachments/622469613581631518/675798997943844879/Meme6.png",
    "https://cdn.discordapp.com/attachments/622469613581631518/675799002834534430/Meme3.png",
    "https://cdn.discordapp.com/attachments/622469613581631518/675799005552181256/Meme5.png",
    "https://cdn.discordapp.com/attachments/622469613581631518/675799026410455050/Meme4.png",
    "https://cdn.discordapp.com/attachments/622469613581631518/675799029531148308/Meme2.png" ]
@bot.command(pass_context = True)                                                                                       #Memes by the Goose
async def goosememe(ctx):
    #  await ctx.message.delete()                  #haha 69 funny meme hahahahaha still laughing hahahaha funny poo hahaha
    embirgoose = discord.Embed(color=0xf5a742)
    embirgoose.set_image(url=random.choice(memes))
    await ctx.send(embed=embirgoose)
    print(f'{ctx.author} has got a goosememe™.')

                                                                
brained = [
    "imma big brain",
    "dont abuse it!",
    "big brain, unlike you :neutral_face:",
    "can you do it?",
    "A+",
    "NGL that's was pretty easy",
    "gabe itch",
    "you should be ashamed, dude",
    "remember, i cant do it wrong",
    "easyyy",
    "you really should teach math more",
    "yeah, letters wont work",
    "even baby yoda can do this with 1 leg"]


@bot.command(pass_context = True)                                                                                       #Multiply
async def multiply(ctx,*,t):
    async with ctx.typing():
      t = t.split(" ")
      f = 1
      for el in t:
          if f == 1:
              epicplus = int(el) 
              f = 0
          else:
              epicplus = epicplus * int(el)
    await ctx.send(f'{epicplus}, {random.choice(brained)}')
    print(f'{ctx.author} multiplied {t} and got {epicplus}')

    
@bot.command(pass_context = True)                                                                                       #Lyrics
async def lyrics(ctx,*,t):
    await ctx.send(f"**Please wait, gettin' lyrics...**  :timer:")
    async with ctx.typing():
        genius = lyricsgenius.Genius("DlLkTctkbi8_eVJ5LUIssUw77yJmIO9Id_EcOmSkM18yutUALAbH5GWydQyuO4_w")
        song = genius.search_song(t)
        if len(song.title) and len(song.lyrics) >= 1024:
            # put a file path down there, refer to lines 128 and 129
            songlyr = "C:\\Users\\Голоушкины\\Documents\\Github\\Doggy-bot\\lyrics.txt"
            await ctx.send("Your song lyrics are more than 1024 characters! Creating a text file...")
            file = open(songlyr,'w')
            file.write(song.artist+" - "+song.title+"\n-------------------------\n"+song.lyrics)
            file.close()
            file = open(songlyr,'r')
            await ctx.send(file=discord.File("C:\\Users\\Голоушкины\\Documents\\Github\\Doggy-bot\\lyrics.txt"))
            file.close()
        else:
            await ctx.send("**"+song.title+"\n-------------------------\n"+song.lyrics+"**")
 

@bot.command(pass_context = True)
async def shiba(ctx):
    # Calamity: C:\\Users\\Голоушкины\\Documents\\GitHub\\Doggy-bot\\ShibaPics
    # Irwing: C:\\Users\\Irwing\\Desktop\\stuffies\\Other code\\py\\doggobots\\doggy-bot(original)\\doggobot\\ShibaPics
    dogpic = random.choice(os.listdir("C:\\Users\\Голоушкины\\Documents\\GitHub\\Doggy-bot\\ShibaPics"))
    await ctx.channel.send(file=discord.File("C:\\Users\\Голоушкины\\Documents\\GitHub\\Doggy-bot\\ShibaPics\\%s" % dogpic))   
    print(f'{ctx.author} wants a pic of a shiba, so bot gave him one called {dogpic}')


@bot.command()
async def reaction(ctx):
    await ctx.message.add_reaction('🧡')
    await ctx.message.add_reaction('💛')
    await ctx.message.add_reaction('💚')
    await ctx.message.add_reaction('💙')
    print(f'{ctx.author} checked how does reaction work.')
    time.sleep(2.5)
    await ctx.message.delete()
                         

@bot.command()
async def fakegift(ctx):
    giftcode = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
    await ctx.send("discord.gift/"+"".join(random.choices(giftcode, k=16)))
    print(f'{ctx.author} has generated a fake gift')
                         

@bot.command()
async def epicgamer(ctx,*,t:discord.Member = None):
    gamerpercent = random.choice(range(0, 100))
    if t == None: t = ctx.author
    if t == ctx.author:
        await ctx.send(f"You are an EPIC GAMER on {gamerpercent}%!")
    if t != ctx.author:
        await ctx.send(f'{t.mention} is an EPIC GAMER on {gamerpercent}%!')
    if gamerpercent == 100:
        await ctx.send("NOW THAT'S EPIC!")
    if gamerpercent == 0:
        await ctx.send("ok boomer")
    if gamerpercent == 69:
        await ctx.send("Nice")
    if gamerpercent >= 90:
        await ctx.send("Nearly epic!")
    print(f"{ctx.author} checked someone's EPIC GAMER percentage, it was {gamerpercent}%")

TOKEN = "Njc1NzE4MTEzNDU4NjUxMTQ2.Xj7N1A.e1AZh6nFPp2qGuaVK68XvbbZ5gY"
bot.run(TOKEN)
