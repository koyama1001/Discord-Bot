# インストールした discord.py を読み込む
import discord
from discord.ext import tasks
from discord.utils import get
from datetime import datetime 
import random
import os
import traceback

# 自分のBotのアクセストークンに置き換えてください
token = ''
CHANNEL_ID =  #チャンネルID




# 接続に必要なオブジェクトを生成
client = discord.Client()

random_Item=[]#ここに複数単語を入れるとランダムに受け取ってくれる
random_Voice=['このゲームがくそゲーだった理由は俺が相手だったからだ','義理の妹なんざ萌えるだけだろうがあ！','牛丼つゆだけ','まるで将棋だな。','おもしれー女','チー牛','野球拳をしたら全裸になるのが常識だろう？','バレなきゃ犯罪じゃないんですよ','黒髪は正義です。反省はしていません',
'生殺与奪の権を他人に握らせるな！','お前はもう 死んでいる']#ここに複数単語を入れるとランダムに受け取ってくれる
random_Daice=['大吉', '中吉','吉', '末吉','小吉','凶', '大凶']#ここに複数単語を入れるとランダムに受け取ってくれる
 
async def reply(message):
   reply = f'{message.author.mention} おはよう' # 返信メッセージの作成
   await message.channel.send(reply)
   


#ログインイベント
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print("Logged in as: " + client.user.name + "\n")
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
   

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
    elif message.content.startswith('おみくじ'):
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢] ", value=random.choice((random_Daice)), inline=False)
        embed.add_field(name="[今日のラッキーアイテム]",value=random.choice((random_Item)),inline=False)
        embed.add_field(name="[今日の名言]",value=random.choice((random_Voice)),inline=False)
        await message.channel.send(embed=embed)

    elif client.user in message.mentions: # 話しかけられたかの判定
        await reply(message)


 

client.run(token)

#ループ処理実行
  
# Botの起動とDiscordサーバーへの接続
