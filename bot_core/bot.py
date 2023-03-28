import discord
from discord.ext import commands
from jproperties import Properties
from bot_core.commands.music import commands_music
from bot_core.commands.chat import commands_chat


# async def send_message(message: str, user_message: str, is_private: bool, is_custom: bool = None, motive: str = None):
#     try:
#         if is_custom:
#             response = responses.handle_custom_message(motive)
#             await message.channel.send(response)
#         else:
#             response = responses.handle_message(user_message)
#             await message.author.send(response) if is_private else await message.channel.send(response)

#     except Exception as e:
#         print(f'Exception: {e}')


def run_discord_bot():
    # Get token value
    configs = Properties()
    with open('resources/app-config.properties', 'rb')as config_file:
        configs.load(config_file)

    token_key = configs.get('TOKEN').data

    # Create client, bot and intents
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='.', intents=intents)

    # @bot.event
    # async def on_ready():
    #     print(f'Boot {bot.user} is now running')

    commands_chat(bot)
    commands_music(bot)

    bot.run(token_key)
