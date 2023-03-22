import discord
from discord.ext import commands
import reply_handlers.responses as responses
from jproperties import Properties
from utils.url_check import url_check
from bot_core.commands.music import commands_music


async def send_message(message: str, user_message: str, is_private: bool, is_custom: bool = None, motive: str = None):
    try:
        if is_custom:
            response = responses.handle_custom_message(motive)
            await message.channel.send(response)
        else:
            response = responses.handle_message(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(f'Exception: {e}')


def run_discord_bot():
    # Get token value
    configs = Properties()
    with open('resources/app-config.properties', 'rb')as config_file:
        configs.load(config_file)

    token_key = configs.get('TOKEN').data

    # Create client, bot and intents
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix='.', intents=intents)

    @client.event
    async def on_ready():
        print(f'Boot {client.user} is now running')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(
            f"================\n{username} said: '{user_message}' \nChannel: ({channel})\n================\n")

        if len(user_message) > 0:
            # Check if message is an url
            if url_check(user_message):
                await send_message(message, user_message, is_private=False, is_custom=True, motive='url')
            else:
                # If the user message contains a '?' in front of the text, it becomes a private message
                if user_message[0] == '?':
                    user_message = user_message[1:]  # [1:] Removes the '?'
                    await send_message(message, user_message, is_private=True)
                else:
                    await send_message(message, user_message, is_private=False)
        else:
            await send_message(message, user_message, is_private=False)

    @bot.event
    async def on_ready():
        print(f'Boot {bot.user} is now running')
        
    @bot.event
    async def on_message(message) :
        # bot.process_commands(msg) is a couroutine that must be called here since we are overriding the on_message event
        await bot.process_commands(message) 
        if str(message.content).lower() == "hello":
            await message.channel.send('Hi!')
        
        if str(message.content).lower() in ['swear_word1','swear_word2']:
            await message.channel.purge(limit=1)

    # @bot.command(name='stop', help='Stops the song')
    # async def stop(ctx):
    #     voice_client = ctx.message.guild.voice_client

    #     if voice_client.is_playing():¡¡
    #         await voice_client.stop()
    #     else:
    #         await ctx.send('The bot is not playing anything at the moment')

    commands_music(bot);

    # client.run(token_key)
    bot.run(token_key)
