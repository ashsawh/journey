from collections import namedtuple
from typing import Dict, Callable, NamedTuple, Optional, List
from mysql.connector import MySQLConnection
from factory import generate_person, generate_people

"""
### people
| **Field** | **Type**    |
| --------- | ----------- |
| id        | Primary Key |
| name      | Varchar     |
| img_url   | Varchar     |
| location  | Varchar     |

### people_colors
| **Field** | **Type**    |
| --------- | ----------- |
| id        | Primary Key |
| people_id | Foreign Key |
| color     | Varchar     |

"""


def findAll(conn: MySQLConnection) -> NamedTuple:
    """
    Find all people to colors, one to many, relationships \

    :param conn:
    :return:
    """
    cursor = conn.cursor()
    stmt = "SELECT p.*, GROUP_CONCAT(c.`color`) FROM `people` p LEFT JOIN `people_colors` c ON p.`id` = c.`people_id` GROUP BY p.`id`"
    cursor.execute(stmt)

    res = cursor.fetchall()
    return generate_people(res)


def findOneOrNone(conn: MySQLConnection, name: str) -> List[NamedTuple]:
    """
    Find person by id then grab all colors, one to many, relationships

    :param conn:
    :param name:
    :return:
    """
    cursor = conn.cursor(prepared=True)

    stmt = "SELECT p.*, GROUP_CONCAT(c.`color`) FROM `people` p LEFT JOIN `people_colors` c ON p.`id` = c.`people_id` " \
           "WHERE p.`name` COLLATE utf8mb4_general_ci LIKE %s GROUP BY p.`id` "

    param = '%{}%'.format(name)
    print(stmt)
    cursor.execute(stmt, (param,))

    res = cursor.fetchone()

    if res:
        return [generate_person(res)]
    else:
        return []
