from discord.ext import commands
from utils.url_check import url_check
import reply_handlers.responses as responses


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


def listener_kick(bot: commands.bot):
    @bot.event
    async def on_message(message):
        # bot.process_commands(msg) is a couroutine that must be called here since we are overriding the on_message event
        await bot.process_commands(message)

        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == bot.user:
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
