import discord
import time
g_client = discord.Client()
@g_client.event
async def on_message(message):
    if message.author == g_client.user: return
    if not(message.content.lower().startswith("dorfl")): return
    if not(message.channel.id == 808742739226787874 or message.channel.id == 809881861371330610): return
    query = message.content.lower().split(" ")
    if len(query) < 3: return
    if query[1] == "voice" or query[1] == "text":
        for channeli in message.channel.guild.channels:
            if channeli.name == query[2]: return
        channel = (await message.channel.guild.categories[1].create_voice_channel(query[2])) if query[1] == "voice" else (await message.channel.guild.categories[0].create_text_channel(query[2]))
        await channel.set_permissions(message.author, overwrite=discord.PermissionOverwrite.from_pair(discord.Permissions.all_channel(), discord.Permissions.none()))
        if query[1] == "text":
            await channel.set_permissions(message.channel.guild.default_role, read_messages=False)
        await message.channel.send("`created channel " + query[2] + " and gave " + message.author.name + " op`")
g_client.run("token", bot=True)
