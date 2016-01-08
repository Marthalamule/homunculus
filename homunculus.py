import discord
from plugins import price, who
from util.discord_util import reply, log_in_client
from util.modules_util import make_module_dict

# Configure what to load here.
modules = make_module_dict([price,
                            who])

client = discord.Client()
log_in_client(client)


@client.event
def on_message(message):
    if message.author == client.user:
        return
        
    #
    # Module commands
    #
    
    handled_by_module = False
    for c, m in modules.items():
        if message.content.startswith(c):
            m.handle(message, client)
            handled_by_module = True
    
    
    #
    # Global commands
    #

    if handled_by_module:
        return
    
    # elif message.content.startswith('!help'):
    #     for _, m in modules.items():
    #         m.help()

    elif message.content.startswith('Are you there?'):
        reply(client, message, "Yes, yes I am. No worries. Everything is fine.")

    # This needed to be done. With updated responses!
    elif message.content.startswith('!poop'):
        if message.author.name == 'Ipoopedbad Ernaga':
            post = "Narcissist"
        else:
            post = "{} and Poop are friends."\
            .format(message.author.mention())
        reply(client, message, post)

    elif message.content.startswith('!ping'):
        reply(client, message, "We're not doing this again.")

    elif message.content.startswith('!trivia'):
        post = "Fuck you, {}. Blame Fenrir."\
            .format(message.author.mention())
        reply(client, message, post)


@client.event
def on_ready():
    for _, m in modules.items():
        m.init()
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


client.run()
