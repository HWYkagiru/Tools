import discord
from discord.ext import commands

sen = input("Bot Token: ")
CopyServer= input("Server id you want to copy: ")
PasteServer = input("server id to copy the server in: ")

intents = discord.Intents.default()
senity = commands.Bot(command_prefix='!', intents=intents)

@senity.event
async def on_ready():
    CopyServer = discord.utils.get(senity.guilds, id=int(CopyServer))
    Copying = discord.utils.get(senity.guilds, id=int(PasteServer))
    
    if CopyServer is None:
        print(f'Unable to find server: {CopyServer} [Make Sure that You are in the Server] ')
        return

    if Copying is None:
        print(f'Unable to find a guild with the id: {PasteServer} [Make Sure that You are in the Server] ')
        return

    for channel in Copying.channels:
        print(f'Deleting channel: {channel.name}')
        await channel.delete()

    for role in Copying.roles:
        if role.name != "@everyone":
            print(f'Deleting role: {role.name}')
            try:
                await role.delete()
            except discord.Forbidden:
                print(f'Cannot delete role: {role.name}')

    for role in CopyServer.roles:
        if role.name != "@everyone":
            print(f'Creating role: {role.name}')
            await Copying.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)

    for category in CopyServer.categories:
        print(f'Creating category: {category.name}')
        await Copying.create_category(name=category.name)

    for channel in CopyServer.channels:
        if isinstance(channel, discord.TextChannel):
            print(f'Creating text channel: {channel.name}')
            await Copying.create_text_channel(name=channel.name, category=discord.utils.get(Copying.categories, name=channel.category.name) if channel.category else None)
        elif isinstance(channel, discord.VoiceChannel):
            print(f'Creating voice channel: {channel.name}')
            await Copying.create_voice_channel(name=channel.name, category=discord.utils.get(Copying.categories, name=channel.category.name) if channel.category else None)

    print("Copied Successfully")

senity.run(sen)
