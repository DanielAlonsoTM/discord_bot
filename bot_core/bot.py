import discord
from discord.ext import commands
from jproperties import Properties
from bot_core.commands.music import Music
from bot_core.commands.chat import Chat
from utils.directory_handler import check_directories_exist, get_current_path
# from bot_core.listeners.kick import listener_kick


def run_discord_bot():
    # Create temporary folder
    check_directories_exist()

    # Path where the script is running
    current_path = get_current_path()

    properties_path = str(f'{current_path}/resources/app-config.properties')

    # Get token value
    configs = Properties()
    with open(properties_path, 'rb')as config_file:
        configs.load(config_file)

    token_key = configs.get('TOKEN').data

    # Create bot and intents
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='.', intents=intents)

    @bot.event
    async def on_ready():
        print(f'Boot {bot.user} is now running')

        # Load Cogs
        await bot.add_cog(Chat(bot))
        await bot.add_cog(Music(bot))

    # listener_kick(bot)

    bot.run(token_key)
