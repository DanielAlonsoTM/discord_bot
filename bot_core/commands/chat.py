from discord.ext import commands
import random


class Chat(commands.Cog, name='Chat Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hi', help='I will say hi for you')
    async def hi(self, ctx):
        await ctx.send(f'Hi {ctx.author}')

    @commands.command(name='joke', brief='I will say a joke of your fat mom', help='I will say a joke of your fat mom')
    async def joke(self, ctx):

        channel_id = ctx.message.author.voice.channel.id
        channel = ctx.guild.get_channel(channel_id)

        members_in_channel = channel.members
        # Member id: int
        # name: string
        # discriminator: string
        # bot: boolean
        # nick: string

        jokes = [
            'joke 1',
            'joke 2',
            'joke 3',
        ]

        message = ''

        if len(members_in_channel) > 1:
            user_selected = members_in_channel[random.randint(
                1, len(members_in_channel))]
            joke_selected = jokes[random.randint(1, len(jokes))]

            message = str(f'Hey {user_selected}, {joke_selected}')
        else:
            message = str(f'Hey {members_in_channel[0].nick}, fucking alone')

        await ctx.send(message)
