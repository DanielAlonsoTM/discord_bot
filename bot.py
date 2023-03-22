import discord
import responses
from jproperties import Properties
from utils.url_check import url_check


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

    # Create client and intents
    intents = discord.Intents.all()

    client = discord.Client(intents=intents)

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

    client.run(token_key)
