from discord.ext import commands


def commands_chat(bot: commands.bot):
    @bot.command(name='hi', help='I will say hi for you')
    async def hi(ctx):
        await ctx.send(f'Hi {ctx.author}')
