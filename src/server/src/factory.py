from typing import Dict, Callable, NamedTuple


def generate_person(results: Dict):
    """
    Create a dictionary from sql that queried a person

    :param results:
    :return:
    """
    person = None

    if len(results) > 0:
        person = {
            "id": results[0],
            "name": results[1].decode("utf-8"),
            "img_url": results[2].decode("utf-8"),
            "location": results[3].decode("utf-8"),
            "colors": (results[4].decode("utf-8")).split(",")
        }

    return person


def generate_people(results: Dict):
    """
    Create a list of person dictionaries from sql query

    :param results:
    :return:
    """
    list = []

    if len(results) > 0:
        for item in results:
            person = {
                "id": item[0],
                "name": item[1].decode("utf-8"),
                "img_url": item[2].decode("utf-8"),
                "location": item[3].decode("utf-8"),
                "colors": (item[4].decode("utf-8")).split(",")
            }

            list.append(person)

    return list
