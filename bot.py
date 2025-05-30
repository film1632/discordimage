import discord
import requests

TOKEN = '-'
ZAPIER_OR_MAKE_WEBHOOK = 'https://hook.eu2.make.com/g84t9wcjwzs1khnpw992e8kt3mdjl2xb'
ALLOWED_CHANNEL_ID = 1377870443989569628  # ✅ ใส่ ID ช่องที่ให้ฟังเฉพาะ

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id != ALLOWED_CHANNEL_ID:
        return

    for attachment in message.attachments:
        if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f'📷 รูปภาพจาก {message.channel.name}: {attachment.url}')
            requests.post(ZAPIER_OR_MAKE_WEBHOOK, json={
                'username': message.author.name,
                'image_url': attachment.url
            })

client.run(TOKEN)
