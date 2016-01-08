import requests
from xml.etree import ElementTree


def get_entity_id_for_name(name: str) -> int:
    url = "https://api.eveonline.com/eve/OwnerID.xml.aspx?names=" + name
    result = requests.get(url)
    tree = ElementTree.fromstring(result.content)

    # first: Current Time, Rowset, or Cached Until
    # second: row in rowset (0)
    # third: accessing the actual attribute in the result row.
    return tree[1][0][0].attrib['ownerID']


def get_entity_name(id: int) -> str:
    url = "https://api.eveonline.com/eve/CharacterName.xml.aspx?ids=" + str(id)
    result = requests.get(url)
    tree = ElementTree.fromstring(result.content)

    # first: Choice between Current Time (0), Rowset (1, this), Cached Until(2)
    # second: row in a rowset (0)
    # third: accessing the name for the name, id tuple.
    return tree[1][0][0].attrib['name']


def get_corp_name(id: int) ->str:       #Function to pull the Corporation Name from Corp ID
    url = "http://evewho.com/api.php?type=corporation&id=" +str(id)
    result = requests.get(url).json()

    corp_info = result['info'].copy()
    print(corp_info['name'])

get_corp_name(98114328)

def get_corp_history(id: int) ->str:
    url = "http://evewho.com/api.php?type=character&id=" +str(id)
    result = requests.get(url).json()

    corp_history_list = result['history'].copy()

    print(type(corp_history_list))

    for corp in corp_history_list:
        get_corp_name(corp['corporation_id'])

get_corp_history(776784803)
