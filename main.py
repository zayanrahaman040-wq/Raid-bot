import os
import discord
from discord.ext import commands
from discord import app_commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Online come {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Syncati {len(synced)} comandi slash")
    except Exception as e:
        print(f"Errore sync: {e}")

@bot.tree.command(name="raid-start", description="Cambia nome a tutti i canali e manda Ciao come state? raid!")
@app_commands.checks.has_permissions(manage_channels=True)
async def extra(interaction: discord.Interaction):
    await interaction.response.send_message("Sto partendo... raid in arrivo", ephemeral=True)

    contatore = 0
    for canale in interaction.guild.text_channels:
        try:
            await canale.edit(name="Raided-by-bot-exe")
            await canale.send("# ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?ciao come state?")
            contatore += 1
        except Exception as e:
            print(f"Salto {canale.name}: {e}")
            continue

    await interaction.followup.send(f"Fatto! Cambiati {contatore} canali ✅", ephemeral=True)

@bot.tree.command(name="ping", description="Vede se il bot è online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! Sono online come {bot.user}", ephemeral=True)

@extra.error
async def extra_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message("Non hai il permesso di gestire i canali", ephemeral=True)

bot.run(TOKEN)
