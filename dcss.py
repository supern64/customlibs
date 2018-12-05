# Discord.CSS
# The wackiest Discord library EVER.
# Based on discord.py

import discord
import cssparser
from sys import argv
import logging
import importlib
from inspect import isawaitable

logger = logging.getLogger("dcss")
fmt = "%(asctime)-15s: %(message)s"
logging.basicConfig(format=fmt)

def start_bot(bot):
    logger.info("Starting bot...")
    global prefix
    prefix = bot["bot"]["prefix"]
    try: # Read presence config
        bot["bot"]["game"]
    except KeyError:
        game = None
    else:
        game = bot['bot']['game']
    try:
        bot['bot']['status']
    except KeyError:
        status = discord.Status.online
    else:
        try:
            status = discord.Status[bot['bot']["status"]]
        except KeyError:
            print("Invalid status provided. Valid values are:\nonline\noffline\nidle\ndnd\ndo_not_disturb\ninvisible")
    try: # load required user libraries
        bot['libs']
    except KeyError:
        pass
    else:
        libs = [m.strip() for m in bot["libs"].split(",")]
        for i in libs:
            try:
                importlib.import_module(i)
            except Exception as c:
                logger.exception("Loading module {0} failed. ({1})".format(i, str(c)))
                print("Loading module {0} failed. ({1})".format(i, str(c)))
    global client
    if game == None:
        client = discord.Client(status=status) # Create client
    else:
        client = discord.Client(status=status, activity=discord.Game(game))
    @client.event
    async def on_message(message): # Parsing time!
        if message.author.bot:
            return
        try:
            bot[message.content.split()[0][1:]]
        except KeyError:
            return
        else:
            if message.content.startswith(prefix):
                arguments = message.content.split()[1:]
                cmd = bot[message.content.split()[0][1:]]
                try:
                    cmd['checks']
                except KeyError:
                    pass
                else:
                    checks = [l.strip() for l in cmd['checks'].split(", ")]
                    if "owner" in checks:
                        app = await client.application_info()
                        if app.owner.id == message.author.id:
                            pass
                        else:
                            await message.channel.send("No permission.")
                            return
                try:
                    cmd['eval']
                except KeyError:
                    evaled = None
                    pass
                else:
                    try:
                        evaled = eval(cmd["eval"].replace("(", '("').replace(")", '")').format(arguments=arguments), globals(), locals())
                        if isawaitable(evaled):
                            evaled = await evaled
                    except:
                        await message.channel.send("An error occured while executing the command.")
                        raise
                try:
                    await message.channel.send(cmd['response'].format(arguments=arguments, evaled=evaled))
                except IndexError:
                    try:
                        await message.channel.send(_mix(cmd['response']))
                    except NameError:
                        await message.channel.send("An error occured while making a response. Most likely arguments fed in incorrectly.")
                return
    @client.event
    async def on_ready():
        print(str(client.user) + " is ready!")
    try:
        client.run(bot['bot']['token'])
    except:
        print("Failed to login. Please check your token.")
    return

def _mix(string):
      try:
            return string.replace("{", "%(").replace("}", ")s") % globals()
      except KeyError:
            try:
                return string.replace("{", "%(").replace("}", ")s") % locals()
            except KeyError as e:
                raise NameError("{0} is not defined".format(str(e)))

if argv[1] == "run":
    global bot
    try:
        logger.debug("Parsing CSS")
        bot = cssparser.parse_file(argv[2])
    except IndexError:
        print("Usage: dcss.py run [bot CSS file name]")
    start_bot(bot)
    
else:
    print("""Usage: dcss.py [command] [arguments] \n     Where [command] is one of: run""")
