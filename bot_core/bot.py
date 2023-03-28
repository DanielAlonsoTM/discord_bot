import discord
from discord.ext import commands
from jproperties import Properties
from bot_core.commands.music import commands_music
from bot_core.commands.chat import commands_chat
# from bot_core.listeners.kick import listener_kick


def run_discord_bot():
    # Get token value
    configs = Properties()
    with open('resources/app-config.properties', 'rb')as config_file:
        configs.load(config_file)

    token_key = configs.get('TOKEN').data

    # Create bot and intents
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='.', intents=intents)

    @bot.event
    async def on_ready():
        print(f'Boot {bot.user} is now running')

    # listener_kick(bot)
    commands_chat(bot)
    commands_music(bot)

    bot.run(token_key)
