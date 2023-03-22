import discord
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        # Joins a voice channel

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):
        # Plays file from local system

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(
            source,
            after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {query}')

    @commands.command()
    async def yt(self, ctx, *, param):
        # Plays from a url
        # TODO
        return

    @commands.command()
    async def stream(self, ctx, *, param):
        # Streams from a url (same as yt, but doesn't predownload)
        # TODO
        return
    
    @commands.command()
    async def volume(self, ctx, *, param):
        # Change volume
        # TODO
        return
    
    @commands.command()
    async def stop(self, ctx, *, param):
        # Stop and disconect bot from voice channel
        # TODO
        return
    
    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        # TODO
        return
    
