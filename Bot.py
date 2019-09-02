import discord
import config
import os
import random

pastapath = './pastas/'


class Client(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}')
        self.pastas = []

        print('Loading pastas')

        for filename in os.listdir('./pastas/'):
            print(filename)
            with open(pastapath + filename, 'r') as pastafile:
                self.pastas.append(pastafile.read())

        print('Pastas loaded!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if 'CSE' in str(message.content).upper():
            await message.channel.send('DID SOMEONE SAY CSE??')

        elif 'pasta' in str(message.content).lower():
            await message.channel.send(random.choice(self.pastas))


Client().run(config.token)
