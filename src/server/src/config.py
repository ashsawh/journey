from yaml import load, SafeLoader
import os.path
import sys
from collections import namedtuple
from typing import Dict, Callable, NamedTuple


def parse(name: str, ingester: Callable) -> NamedTuple:
    """
    Parse a yml configuration file and retrieve it's attributes into a dictionary for use

    :param name:
    :param ingester:
    :return namedtupal:
    """
    try:
        filename = resolve_path() + "/" + name

        with open(filename) as f:
            data = load(f, Loader=SafeLoader)

        # get back named tuple containing configuration data
        return ingester(data)

    except Exception as error:
        print(error)


def resolve_path() -> str:
    """
    Resolve the path and get the configuration path to the config directory
    :return:
    """
    if sys.path[0]:
        config_path = os.path.realpath(sys.path[0] + '/../conf/')
    else:
        # On OS X, if the project root is a symlink, realpath doesn't resolve correctly
        config_path = os.path.realpath(os.path.dirname(__file__) + '/../../conf/')

    # get string containing file config path
    return config_path


def ingest(data: Dict) -> namedtuple:
    """
    Once data has been fetched from config file, load into immutable tupals for ease of use throughout application

    :param data:
    :return namedtupal:
    """
    Config: NamedTuple = namedtuple("Config", "general db")
    if 'general' not in data or 'db' not in data:
        raise ValueError("General ord db in config file")

    DbConfig: NamedTuple = namedtuple("DbConfig", "host port database user password")
    db = DbConfig(
        host=data['db']['host'],
        port=data['db']['port'],
        user=data['db']['user'],
        database=data['db']['database'],
        password=data['db']['password']
    )

    GeneralConfig: NamedTuple = namedtuple("GeneralConfig", "app log env")
    general: NamedTuple = GeneralConfig(
        app=data['general']['app_name'],
        log=data['general']['log_path'],
        env=data['general']['environment']
    )

    # get back a named tuple containing all configuration params
    return Config(db=db, general=general)
