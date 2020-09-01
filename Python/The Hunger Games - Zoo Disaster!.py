animals_food = {   "antelope": ["grass"], \
              "big-fish": ["little-fish"], \
              "bug": ["leaves"], \
              "bear": ["big-fish", "bug", "chicken", "cow", "leaves", "sheep"], \
              "chicken": ["bug"], \
               "cow": ["grass"], \
               "fox": ["chicken", "sheep"], \
               "giraffe": ["leaves"], \
               "lion": ["antelope", "cow"], \
               "panda": ["leaves"], \
               "sheep": ["grass"]}

def who_eats_who(zoo):
    animals = zoo.split(',')
    history = []
    size_of_zoo = len(animals)
    index = 0
    while index < size_of_zoo and size_of_zoo > 1:
        #print(animals)
        if animals[index] not in animals_food:
            index += 1
            continue
        if index > 0:
            # check the left
            if animals[index - 1] in animals_food[animals[index]]:
                history.append("{} eats {}".format(animals[index], animals[index - 1]))
                animals.pop(index - 1)
                index = 0
                size_of_zoo -= 1
                continue
        if index < size_of_zoo - 1:
            # check the right
            if animals[index + 1] in animals_food[animals[index]]:
                history.append("{} eats {}".format(animals[index], animals[index + 1]))
                animals.pop(index + 1)
                index = 0
                size_of_zoo -= 1
                continue
        index += 1
                
    res = [zoo]
    for event in history:
        res.append(event)
    res.append(",".join(animals))
    return res