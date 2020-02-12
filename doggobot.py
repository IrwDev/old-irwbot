import discord
from discord.ext import commands
import lyricsgenius
import time
import urllib
import pprint
import json

from googleapiclient.discovery import build
import pprint

bot = commands.Bot(command_prefix = ">>")


name = "doggobot.py 1.2 >> github.com/procopylua"
game = discord.Game(name=name)
stream = discord.Streaming(name = name,url = "https://www.twitch.tv/twitch/")

@bot.event                                                                                                              #Launching Doggy
async def on_ready(pass_context = True): # if bot ready(launched), then(then means (:) )
  print("-----------------------------")
  print("-EPIC DOGGO SCRIPT LAUNCHED--")
  print("---------version 1.2---------")
  print("-----------cheeto------------")
  #channel = await bot.fetch_channel("665206516042825768")
  #await channel.send('**---------Bot launched---------\n----------Prefix-[>>]----------**')
  await bot.change_presence(status=discord.Status.online, activity=stream)
  


@bot.command(pass_context = True)                                                                                       #Repeat
async def repeat(ctx,*,t):   
  await ctx.message.delete()
  await ctx.send(t)
  print(f'{ctx.author} Said {t}, and because this command was "repeat", bot repeated that.')

@bot.event
async def on_member_join(member):
      print(f'{member} has joined a server called.')

      
@bot.command(pass_context = True)                                                                                       #Ping
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'Pong.```css\n {round(bot.latency * 1000)}ms```')
    print(f'{ctx.author} checked ping of a bot. Its was {round(bot.latency * 1000)}ms.')

import random
hello = ["hi,","howdy,","nice to meet you,","hey,","hello,","what's up,","wyd,","qq,","q,","A MAN HAS FALLEN INTO THE RIVER IN LEGO CITY, THIS MAN WAS"]


@bot.command(pass_context=True)                                                                                       #Hi(first random test)
async def hi(ctx):
    await ctx.message.delete()
    await ctx.send(f'{random.choice(hello)} {ctx.author.mention}!')
    print(f'{ctx.author} greeted with a bot.')
  

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
    await ctx.message.delete()                  #haha 69 funny meme hahahahaha still laughing hahahaha funny poo hahaha
    embirgoose = discord.Embed(color=0xf5a742)
    embirgoose.set_image(url=random.choice(memes))
    await ctx.send(embed=embirgoose)
    print(f'{ctx.author} got a goosememe™.')

                                                                
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
          epicplus= epicplus * int(el)
    await ctx.send(f'{epicplus}, {random.choice(brained)}')
    print(f'{ctx.author} multiplied {t} and got {epicplus}')

    
@bot.command(pass_context = True)                                                                                       #Lyrics
async def lyrics(ctx,*,t):
    msga = await ctx.send(f"**Please wait, gettin' lyrics...**  :timer:")
    async with ctx.typing():
        genius = lyricsgenius.Genius("DlLkTctkbi8_eVJ5LUIssUw77yJmIO9Id_EcOmSkM18yutUALAbH5GWydQyuO4_w")
        song = genius.search_song(t)
        lyrics_embed = discord.Embed(color=0x8d42f5)
        lyrics_embed.add_field(name=song.title, value=list(song.lyrics))
        await msga.edit(embed = lyrics_embed)
 

@bot.command(pass_context = True)
async def shiba(ctx):
    shiba = [
        "https://i.imgur.com/fqMTE6t.jpg",                                                                                              #1
        "https://imgur.com/CkfRAO1",                                                                                                    #2
        "https://imgur.com/tdmiveA",                                                                                                    #3
        "https://imgur.com/F7fkgrS",                                                                                                    #4
        "https://i.imgur.com/ddmBfkc.jpg",                                                                                              #5
        "https://i.imgur.com/M9koilm.jpg",                                                                                              #6
        "https://i.imgur.com/OWMbXux.jpg",                                                                                              #7
        "http://imgur.com/gallery/3tRILTi",                                                                                             #8
        "https://i.imgur.com/Lo5hsmY.jpg",                                                                                              #9
        "https://i.imgur.com/rBex74U.jpg",                                                                                              #10
        "https://preview.redd.it/tlltufyfzbf41.jpg?width=640&crop=smart&auto=webp&s=cfaa09924f6c60650562d4ee1e734f69afe468ea",          #11
        "https://preview.redd.it/tw6u6i2kjff41.jpg?width=640&crop=smart&auto=webp&s=3dc95856e6726e5b25d2dc6a49eac620bf21b3d4",          #12
        "https://preview.redd.it/rd14l5x3wbf41.jpg?width=640&crop=smart&auto=webp&s=06dd9ec8c32deb0c43b50586cdc1c056e1737b47",          #13
        "https://preview.redd.it/l7e7o7sdj6f41.jpg?width=640&crop=smart&auto=webp&s=898abf2bc03df1aa02c554bb4275e4e864716d0e",          #14
        "https://preview.redd.it/qecogv326bf41.jpg?width=640&crop=smart&auto=webp&s=ae5560785bc60a0e10fd5411cb9f391ca57ffb52",          #15
        "https://preview.redd.it/b57earzrw5f41.jpg?width=640&crop=smart&auto=webp&s=64c4873149521c5e9f8e65dd0353dc3e51bfe8e2"           #16
        "https://preview.redd.it/ti10ipuek1g41.jpg?width=640&crop=smart&auto=webp&s=8545f95bd937f08d3ce84206f338a9874143a385",          #17
        "https://preview.redd.it/new4dtbzc1g41.jpg?width=640&crop=smart&auto=webp&s=bd517b83a1a3f24a3b072b8e05a565a1c6c7993a",          #18
        "https://preview.redd.it/v4yv9bmjzzf41.jpg?width=640&crop=smart&auto=webp&s=61367944f5378d4a94648c4ac3b6269b35c36c77",          #19
        "https://preview.redd.it/lfiy0iivczf41.jpg?width=640&crop=smart&auto=webp&s=3539ae8fcbc68e5263bb01ecfaf86c4692e580f3",          #20
        "https://preview.redd.it/cou5le0knyf41.jpg?width=640&crop=smart&auto=webp&s=1f815d977aa8f1ef3bd30f55c16c05622b806947",          #21
        "https://preview.redd.it/iwjsb8swskf41.jpg?width=640&crop=smart&auto=webp&s=a61a04bfaca3c5dc439cf54007a2726b5250ffa3",          #22
        "https://preview.redd.it/k840st92olf41.jpg?width=640&crop=smart&auto=webp&s=5b6d98c5130e81fdfe25d6fdcf4e01419d0a4a5a",          #23
        "https://preview.redd.it/zi48tc9uxtf41.jpg?width=640&crop=smart&auto=webp&s=9b4e0e6d98d28b54c86d358a300362a2a75d4da1",          #24
        "https://preview.redd.it/hrhztrbs7of41.jpg?width=640&crop=smart&auto=webp&s=50a737a15c907edc22db81a74074d4efc08f6d88",          #25
        "https://preview.redd.it/ge5fpxg0eff41.jpg?width=640&crop=smart&auto=webp&s=f7f1b1dff3cdbdb4dbd02dbab58e4eae348fb46d",          #26
        "https://preview.redd.it/sj0o22ho2lf41.jpg?width=640&crop=smart&auto=webp&s=d5703c494c8ad87ab378bcad513bfa539aace157",          #27
        "https://preview.redd.it/qfw2onc35kf41.jpg?width=640&crop=smart&auto=webp&s=b603376c0d78c8654be853b8ceb4dbddabbafaab"]          #28
   
    embed = discord.Embed(color=0x6cf542)
    embed.set_image(url=random.choice(shiba))
    await ctx.channel.send(embed=embed)
    
    print(f'{ctx.author} wants a pic of a shiba, so bot gave him one.')


@bot.command()
async def reaction(ctx):
    await ctx.message.add_reaction('🧡')
    await ctx.message.add_reaction('💛')
    await ctx.message.add_reaction('💚')
    await ctx.message.add_reaction('💙')
    print(f'{ctx.author} checked how does reaction works.')
    time.sleep(2.5)
    await ctx.message.delete()
                         

@bot.command()
async def gift(ctx):
    giftcode = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
    await ctx.send("discord.gift/"+"".join(random.choices(giftcode, k=16)))
    print(f'{ctx.author} Generated a fake gift.')

my_api_key = "AIzaSyDxYePngOLzf1fm-zJY-gG139cbdZw74BY"
my_cse_id = "002161540390636908943:d3dk1h9fjqy"

















# def google_search(search_term, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#    return res['items']
# 
# results = google_search(
#     'stackoverflow site:www.minecraft.net', my_api_key, my_cse_id, num=10)
# for result in results:
# (GOOGLE API)     pprint.pprint(result)      
                         

TOKEN = "Njc1NzE4MTEzNDU4NjUxMTQ2.Xj7N1A.e1AZh6nFPp2qGuaVK68XvbbZ5gY"
bot.run(TOKEN)

