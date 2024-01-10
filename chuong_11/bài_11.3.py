animals = ["ant", "bear", "cat", "dog", "elephant", "fish", "goat", "hippo"]
animal=input('I want to find:')
print('Number of animals:',len(animals))
for i in animals:
    if animal==i:
        print('there is',animal,'in list of animals')
        break
else:
    print('not found')
    