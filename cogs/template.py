""""
Copyright © Krypton 2021 - https://github.com/kkrypt0nn
Description:
This is a template to create your own discord bot in python.

Version: 2.7
"""

import json
import os
import sys

from discord.ext import commands

# Only if you want to use variables that are in the config.json file.
if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

global question
question = []
# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="template"):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(name="question")
    # async def question(self, ctx):
    #     question.append(ctx.message.id)
    #     print(question)

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @commands.command(name="show")
    async def testcommand(self, ctx):
        await ctx.send("Question List:")
        print(self.bot.question)
        for message_id in self.bot.question:
            channel = ctx.message.channel
            message = await channel.fetch_message(message_id)
            print(message)
            users = set()
            for reaction in message.reactions:
                print(reaction)
                async for user in reaction.users():
                    users.add(user)
            print(f"users: {', '.join(user.name for user in users)}")
            print(users)
            if "WilliamMou" in [user.name for user in users]:
                await ctx.send(message.content)



# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(Template(bot))
