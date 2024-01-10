arrival=['adele','fleda','owen','may','mona','gillbert','ford']
def party_late(arrival,name):
    if (arrival.index(name)+1)==(len(arrival)):
        return False 
    if (arrival.index(name)+1)>(len(arrival)/2):
        return True
    else:
        return False

print(party_late(arrival,name='gillbert'))
print(party_late(arrival,name='ford'))
print(party_late(arrival,name='mona'))

