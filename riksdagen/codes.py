"""Module containing getters for different codes to riksdagens api."""
import requests
from typing import Dict, Tuple
from datetime import datetime
import custom_time
import sys


def _get_codes(url, root_key, key, identifier, f_name) -> Tuple[Dict, datetime]:
    res = requests.get(url)
    json_dict = res.json()
    root_dict = json_dict[root_key]
    date = root_dict["@systemdatum"]
    code_list = root_dict[key]
    entry_dict = {entry[identifier]: entry for entry in code_list}
    
    lost_keys = len(code_list) - len(entry_dict)
    if lost_keys: 
        print(f"{f_name}:: Lost {lost_keys} because of multiple types with same '{identifier}'.")

    return (entry_dict, custom_time.str_to_datetime(date))
    

def get_document_types() -> Tuple[Dict, datetime]:
    code_dict = {
        'url': 'http://data.riksdagen.se/sv/koder/?typ=doktyp&utformat=json',
        'root_key': 'typer',
        'key': 'typ',
        'identifier': 'seriekod',
        'f_name': sys._getframe().f_code.co_name,
    }

    return _get_codes(**code_dict)


def get_organs() -> Tuple[Dict, datetime]:
    code_dict = {
        'url': 'http://data.riksdagen.se/sv/koder/?typ=organ&utformat=json',
        'root_key': 'organ',
        'key': 'organ',
        'identifier': 'kod',
        'f_name': sys._getframe().f_code.co_name,
    }

    return _get_codes(**code_dict)


def get_roles() -> Tuple[Dict, datetime]:
    code_dict = {
        'url': 'http://data.riksdagen.se/sv/koder/?typ=roll&utformat=json',
        'root_key': 'roller',
        'key': 'roll',
        'identifier': 'kod',
        'f_name': sys._getframe().f_code.co_name,
    }

    return _get_codes(**code_dict)
    

def get_national_meetings() -> Tuple[Dict, datetime]:
    code_dict = {
        'url': 'http://data.riksdagen.se/sv/koder/?typ=riksmote&utformat=json',
        'root_key': 'riksmoten',
        'key': 'riksmote',
        'identifier': 'id',
        'f_name': sys._getframe().f_code.co_name,
    }

    return _get_codes(**code_dict)