# Searching
def search(instances_List, word):
    j = 0
    found = 0
    No = ['No Results Found']
    Matches = []
    while j < len(instances_List):
        tempDict = instances_List[j].__dict__
        for key in tempDict:
            if str(word) in str(tempDict[key]):
                print(tempDict.__str__(), ' had a match.')
                Matches.append(tempDict.__str__())
                found += 1
        j += 1
    if found == 0:
        print(No)
    else:
        return Matches
