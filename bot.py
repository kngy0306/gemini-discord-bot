from os import getenv
from dotenv import load_dotenv
from discord import app_commands
import discord
import google.generativeai as genai

load_dotenv()

DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")
API_KEY = getenv("API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    new_activity = f"Gemini API"
    await client.change_presence(activity=discord.Game(new_activity))
    await tree.sync()
    print("Bot is ready!")

@tree.command(name="chat",description="AIに聞きたいことを入力してください！")
async def command_chat(interaction: discord.Interaction, message: str):
    response = model.generate_content(message)
    await interaction.response.send_message(response.text, ephemeral=True)


client.run(DISCORD_BOT_TOKEN)
