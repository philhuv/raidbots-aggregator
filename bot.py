import discord
import character_repository
import asyncio
import app_constants
from simulation_service import runSim, run_droptimizer

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!runall'):
        await message.channel.send("I'm on it! Brb")
        characters = character_repository.get_characters()
        tasks = []
        for character in characters:
            tasks.append(asyncio.create_task(run_droptimizer(character, app_constants.MYTHIC)))
        results = await asyncio.gather(*tasks)
        updated_message = ''
        for result in results:
            print (result[0] + ': ' + result[1])
            updated_message = updated_message + \
                result[0] + ': ' + result[1] + '\n'
        await message.channel.send(updated_message)



client.run('ODY3NjMwNjQxNDA3NzIxNDky.YPj6AA.ydIb0sQxDHs92X0xsw_EM3cj-Jc')