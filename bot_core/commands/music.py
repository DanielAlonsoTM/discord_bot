from discord.ext import commands
from bot_core.engines.ytdl import YTDLSource


class Music(commands.Cog, name='Music Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join', help='Tells the bot to join the voice channel')
    async def join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send('{} is not connected to a voice channel'.format(ctx.message.author.name))
            return
        else:
            channel = ctx.message.author.voice.channel

        await channel.connect()

    @commands.command(name='leave', help='To make the bot leave the voice channel')
    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client

        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send('The bot is not connected to a voice channel')

    # @commands.command(name='play', help='To play song')
    # # Download source and play locally
    # async def play(self, ctx, url):
    #     try:
    #         async with ctx.typing():
    #             player = await YTDLSource.from_url(url, loop=bot.loop)
    #             ctx.voice_client.play(player, after=lambda e: print(
    #                 f'Player error: {e}') if e else None)

    #         await ctx.send('**Now playing:** {}'.format(player.title))
    #     except Exception as e:
    #         print(f'Error: {e}')
    #         await ctx.send('An error ocurred while I tried to play this song. Check the log')

    @commands.command(name='stream', help='To play song')
    async def stream(self, ctx, url):
        # Streams from a url (same as play, but doesn't predownload)
        try:
            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
                ctx.voice_client.play(player, after=lambda e: print(
                    f'Player error: {e}') if e else None)

            await ctx.send('**Now playing:** {}'.format(player.title))
        except Exception as e:
            print(f'Error: {e}')
            await ctx.send('An error ocurred while I tried to play this song. Check the log')

    @commands.command(name='resume', help='Resumes the song')
    async def resume(self, ctx):
        print(f'ctx: {ctx}')
        voice_client = ctx.message.guild.voice_client

        if voice_client.is_paused():
            voice_client.resume()
        else:
            await ctx.send('The bot was not playing anything before this. Use .play command')

    @commands.command(name='pause', help='This command pauses the song')
    async def pause(self, ctx):
        voice_client = ctx.message.guild.voice_client

        if voice_client.is_playing():
            voice_client.pause()
        else:
            await ctx.send('The bot is not playind anything at the moment')

    @commands.command(name='stop', help='Stops the song')
    async def stop(self, ctx):
        voice_client = ctx.message.guild.voice_client

        if voice_client.is_playing():
            voice_client.stop()
        else:
            await ctx.send('The bot is not playing anything at the moment')
