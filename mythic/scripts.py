
from mythic.models import MeaningTableElement, MeaningTable
from django.core import serializers

def list_from_file(path, table):
    with open(path, "r") as f:
        content = f.read()

    words = content.split("\n")
    words = [word.lstrip("1234567890: ") for word in words]  
    words = [word for word in words if word !=""]
    print(words)
      
    for word in words:
        new_word = MeaningTableElement(table = table, word = word)
        new_word.save()


def serialize_data_to_json(thing_to_serialize):
    return serializers.serialize('json', thing_to_serialize)

#list_from_file('mythic/word files/test.txt')
