import random


def handle_message(message: str):
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello there'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return 'Help message'

    else:
        return 'What do u say?'


def handle_custom_message(motive: str):
    if motive == 'url':
        return 'This message is an url, will be put in the channel [CHANNEL]'
    else:
        return 'Not implemented yet'
