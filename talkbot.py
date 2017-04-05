#!/usr/bin/env python3.5
import sys
import discord
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
client = discord.Client()

@client.event
async def on_ready():
    logger.info("User: {}".format(client.user.name))
    logger.info("User Discriminator: {}".format(client.user.discriminator))
    logger.info("User ID: {}".format(client.user.id))

async def my_message():
    await client.wait_until_ready()
    while True:
        msg_in = input("Input:")
        msg = msg_in.split(" ")
        try:
            idx = msg.index("|")
            send_msg = ' '.join(msg[idx+1:])
            if msg[0] == 'embed':
                em = discord.Embed(description=send_msg, colour=0x1EA1F1)
                await client.send_message(discord.Object(id=msg[1]), embed=em)
            elif msg[0] == "main":
                await client.send_message(discord.Object(id=msg[1]), send_msg)
        except Exception as e:
            print(e)
client.loop.create_task(my_message())
bot_state = True if 'true' in sys.argv else False
client.run(sys.argv[1], bot=bot_state)
