import connexion

from openapi_server.models.cat import Cat  # noqa: E501
from openapi_server.models.cats_response import CatsResponse  # noqa: E501
from uuid import uuid4

SAMPLE_CAT_STORAGE = {
    "1": {
        "id": "1",
        "name": "Garfield",
        "breed": "Persian"
    },
    "2": {
        "id": "2",
        "name": "Serafettin",
        "breed": "Turkish Angora"
    },
    "3": {
        "id": "3",
        "name": "Kitty",
        "breed": "British Longhair"
    }
}


def add_cat(cat=None):  # noqa: E501
    """Add a new cat to the store

    Creates a new cat in the store # noqa: E501

    :param cat: Cat object that needs to be added to the store
    :type cat: dict | bytes

    :rtype: Cat
    """
    if connexion.request.is_json:
        cat = Cat.from_dict(connexion.request.get_json())  # noqa: E501

    cat.id = uuid4().hex
    SAMPLE_CAT_STORAGE[cat.id] = cat.to_dict()
    return cat, 201


def delete_cat(cat_id):  # noqa: E501
    """Delete a cat

    Delete a cat # noqa: E501

    :param cat_id: Id of the cat desired to be deleted
    :type cat_id: str

    :rtype: None
    """
    SAMPLE_CAT_STORAGE.pop(cat_id)

    return None, 204


def get_cat(cat_id):  # noqa: E501
    """Retrieve a single cat

    Retrieve a single cat # noqa: E501

    :param cat_id: Id of the cat desired to be retrieved
    :type cat_id: str

    :rtype: Cat
    """
    return Cat.from_dict(SAMPLE_CAT_STORAGE[cat_id])


def list_cats():  # noqa: E501
    """Retrieves the list of all cats

    Retrieves the list of all cats # noqa: E501


    :rtype: CatsResponse
    """
    return CatsResponse(
        cats=list(map(lambda x: Cat.from_dict(x), SAMPLE_CAT_STORAGE.values())))


def update_cat(cat_id, cat=None):  # noqa: E501
    """Update an existing cat

     # noqa: E501

    :param cat_id: Id of the cat desired to be updated
    :type cat_id: str
    :param cat: Cat object that needs to be added to the store
    :type cat: dict | bytes

    :rtype: Cat
    """
    if connexion.request.is_json:
        cat = Cat.from_dict(connexion.request.get_json())  # noqa: E501
    cat.id = cat_id
    SAMPLE_CAT_STORAGE[cat_id] = cat.to_dict()
    return cat, 201
