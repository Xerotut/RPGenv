
from mythic.models import MeaningTableElement, MeaningTable

def list_from_file(path, table):
    with open(path, "r") as f:
        content = f.read()

    words = content.split("\n")
    words = [word.lstrip("1234567890: ") for word in words]    
    
    for word in words:
        new_word = MeaningTableElement(table = table, word = word)
        new_word.save()

#list_from_file('mythic/word files/action II.txt', MeaningTable.objects.get(name = "Action II"))
