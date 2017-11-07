import discord

client = discord.Client()
jose = 'The Argent Edge#4814'
drowsy = 'Drowsyyy#1893'
battle = 'Battle King#2805'

@client.event
async def on_ready():
    print('The ' + client.user.name + ' is awake!')

@client.event
async def on_message(message):

    chat = message.content.lower()
    who = str(message.author)

    if message.author == client.user:
        return

    elif message.content.startswith('!witcher'):
        await client.send_message(message.channel, '༼ つ ◕_◕ ༽つ JOSE PLAY')
        await client.send_message(message.channel, '༼ つ ◕_◕ ༽つ WITCHER 3')
        await client.send_message(message.channel, '😍')

    elif 'pinche' in chat and who == jose:
        await client.send_message(message.channel, 'language!')

    elif 'wes' in chat and who == jose:
        await client.send_message(message.channel, 'GAAAAAAAAAAYYYYYYYYY!')

    elif 'br' in chat and who == jose:
        await client.send_message(message.channel, 'stop playing it you addict')

    elif 'gotta go' in chat and who == drowsy:
        await client.send_message(message.channel, 'seeya Deondre')

    elif 'boobs' in chat and who == battle:
        await client.send_message(message.channel, 'battle about to eat that pink curry')

    elif 'test' in chat:
        await client.add_reaction(message, ':Only4Battle:367820413104947200')

    elif 'destiny' in chat:
        await client.add_reaction(message, ':HYPERLUL:338759962270629889')



client.run('TOKEN')
