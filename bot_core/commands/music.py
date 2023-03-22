from discord.ext import commands
from bot_core.ytdl import YTDLSource


def commands_music(bot: commands.bot):
    @bot.command(name='join', help='Tells the bot to join the voice channel')
    async def join(ctx):
        if not ctx.message.author.voice:
            await ctx.send('{} is not connected to a voice channel'.format(ctx.message.author.name))
            return
        else:
            channel = ctx.message.author.voice.channel

        await channel.connect()

    @bot.command(name='leave', help='To make the bot leave the voice channel')
    async def leave(ctx):
        voice_client = ctx.message.guild.voice_client

        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send('The bot is not connected to a voice channel')

    @bot.command(name='play', help='To play song')
    async def play(ctx, url):
        try:
            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=bot.loop)
                ctx.voice_client.play(player, after=lambda e: print(
                    f'Player error: {e}') if e else None)

            await ctx.send('**Now playing:** {}'.format(player.title))
        except Exception as e:
            print(f'Error: {e}')
            await ctx.send('An error ocurred while I tried to play this song. Check the log')

    @bot.command(name='resume', help='Resumes the song')
    async def resume(ctx):
        print(f'ctx: {ctx}')
        voice_client = ctx.message.guild.voice_client

        if voice_client.is_paused():
            voice_client.resume()
        else:
            await ctx.send('The bot was not playing anything before this. Use .play command')

    @bot.command(name='pause', help='This command pauses the song')
    async def pause(ctx):
        voice_client = ctx.message.guild.voice_client

        if voice_client.is_playing():
            voice_client.pause()
        else:
            await ctx.send('The bot is not playind anything at the moment')

    @bot.command(name='stop', help='Stops the song')
    async def stop(ctx):
        voice_client = ctx.message.guild.voice_client

        if voice_client.is_playing():
            voice_client.stop()
        else:
            await ctx.send('The bot is not playing anything at the moment')
