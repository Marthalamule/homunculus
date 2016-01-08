from api import eve_xml, zkb
from util.discord_util import reply


def init():
    pass


def handle(message, client):
    args = message.content[5:]

    try:
        char_id = eve_xml.get_entity_id_for_name(args)
        zkb_stats = zkb.query_character_stats(char_id)

        msg = "\n{} [{} - {}] \n{} \n{}".format(
                zkb_stats['info']['name'],
                zkb_stats['shipsDestroyed'],
                zkb_stats['shipsLost'],
                eve_xml.get_entity_name(zkb_stats['info']['corporationID']),
                eve_xml.get_entity_name(zkb_stats['info']['allianceID']))

        client.send_message(message.channel, msg)

    except TypeError:
        reply(client, message, "\nNo killboard information found on pilot. "
                               "\nEnter a dude who's bad enough to be found. ")

