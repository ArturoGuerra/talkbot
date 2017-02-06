#!/usr/bin/env python3.5
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
    msg_in = input("Input:")
    msg = msg_in
    if msg_in.startswith("embed "):
        send_id = msg.split(" ")
        msg = msg.split("| ",1)[1]
        em = discord.Embed(description=msg, colour=color_blue)
        await client.send_message(discord.Object(id=send_id[1]), embed=em)
    if msg_in.startswith("main "):
        send_id = msg.split(" ")
        msg = msg.split("| ",1)[1]
        await client.send(discord.Object(id=send_id[1]), msg)
    await my_message()
client.loop.create_task(my_message())
client.run(config['token'], bot=False)