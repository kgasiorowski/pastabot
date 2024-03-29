import discord
import config
import random
import pastas

pastapath = './pastas/'
PREFIX = '%'
modeswitch = PREFIX + 'bot'
clean = PREFIX + 'clean'


class Client(discord.Client):

    def __init__(self):
        super(Client, self).__init__()
        self.enabled = True

        print('Loading pastas')
        self.pastas = pastas.get_pastas()
        print('Pastas loaded!')

    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(modeswitch):
            self.enabled = not self.enabled

            if self.enabled:
                await message.channel.send('Bot enabled.')
            else:
                await message.channel.send('Bot disabled.')

        if not self.enabled:
            return

        if message.content.startswith(clean):

            try:
                limit = int(message.content.split(' ')[1])
            except:
                limit = 20

            async for msg in message.channel.history(limit=int(limit)):
                if msg.author == self.user:
                    await msg.delete()

            async for msg in message.channel.history(limit=1):
                await msg.delete()

        elif 'cse' in str(message.content).lower():
            await message.channel.send('DID SOMEONE SAY CSE??')

        elif 'pasta' in str(message.content).lower():
            randompasta = random.choice(self.pastas)
            await message.channel.send('> ' + randompasta[0] + '\n\n' + randompasta[1])

        elif 'chevy' in str(message.content).lower() and 'impala' in str(message.content).lower():
            await message.channel.send('> chevy impala')

        elif 'finch' in str(message.content).lower():
            await message.channel.send(f'Uh, {message.author.mention}, please uh pay attention in uh, uh, class.')


client = Client()
client.run(config.token)
