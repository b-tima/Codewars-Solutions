def alphabet_war(battlefield):
    if battlefield.count('#') == 0:
        return battlefield.replace('[', '').replace(']', '')
    bunkers = {}
    prev_bunker = ""
    addInhabitants = False
    inhabitants = ""
    bombs = 0
    for c in battlefield:
        if c == '#':
            if prev_bunker in bunkers:
                bunkers[prev_bunker] += 1
            bombs += 1
        if c == ']':
            addInhabitants = False
            bunkers[inhabitants] = bombs
            prev_bunker = inhabitants
            inhabitants = ""
            bombs = 0
        elif addInhabitants:
            inhabitants += c
        elif c == '[':
            addInhabitants = True
    return "".join(filter(lambda x: bunkers[x] < 2, bunkers))