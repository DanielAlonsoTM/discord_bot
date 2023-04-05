import discord
from discord.ext import commands
from jproperties import Properties
from bot_core.commands.music import Music
from bot_core.commands.chat import Chat
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

        # Load Cogs
        await bot.add_cog(Chat(bot))
        await bot.add_cog(Music(bot))

    # listener_kick(bot)

    bot.run(token_key)
