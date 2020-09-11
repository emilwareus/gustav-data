"""Module containing getters for different codes to riksdagens api."""
import requests
from typing import Dict, Tuple
from datetime import datetime
import custom_time
import sys


def _get_codes(url, root_key, key) -> Tuple[Dict, datetime]:
    res = requests.get(url)
    json_dict = res.json()
    root_dict = json_dict[root_key]
    date = root_dict["@systemdatum"]
    code_list = root_dict[key]

    return (code_list, custom_time.str_to_datetime(date))
    

def get_document_types() -> Tuple[Dict, datetime]:
    code_dict = {
        'url': 'http://data.riksdagen.se/sv/koder/?typ=doktyp&utformat=json',
        'root_key': 'typer',
        'key': 'typ',
    }

    return _get_codes(**code_dict)


def get_organs() -> Tuple[Dict, datetime]:
    code_dict = {
        'url': 'http://data.riksdagen.se/sv/koder/?typ=organ&utformat=json',
        'root_key': 'organ',
        'key': 'organ',
    }

    return _get_codes(**code_dict)


def get_roles() -> Tuple[Dict, datetime]:
    code_dict = {
        'url': 'http://data.riksdagen.se/sv/koder/?typ=roll&utformat=json',
        'root_key': 'roller',
        'key': 'roll',
    }

    return _get_codes(**code_dict)
    

def get_national_meetings() -> Tuple[Dict, datetime]:
    code_dict = {
        'url': 'http://data.riksdagen.se/sv/koder/?typ=riksmote&utformat=json',
        'root_key': 'riksmoten',
        'key': 'riksmote',
    }

    return _get_codes(**code_dict)