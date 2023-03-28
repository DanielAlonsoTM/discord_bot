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
        active_users = [
            'user A',
            'user B',
            'user C'
        ]

        jokes = [
            'joke 1',
            'joke 2',
            'joke 3',
        ]

        user_selected = active_users[random.randint(1, len(active_users))]
        joke_selected = jokes[random.randint(1, len(jokes))]

        await ctx.send(f'Hey {user_selected}, {joke_selected}')
