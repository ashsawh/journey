from mysql import connector
from typing import NamedTuple


def get_conn(config: NamedTuple) -> connector.MySQLConnection:
    """
    Accept parsed configuration data and create mysql connector

    :param config:
    :return:
    """
    return connector.connect(
      host=config.db.host,
      database=config.db.database,
      user=config.db.user,
      passwd=config.db.password
    )
