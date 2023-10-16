from Lifter import *
from PlateCounter import *
from copy import deepcopy


# Code here should be for procesing lists of inputs into list of dicts that
# contain loadings, main can then organize the loading and run as a state
# machine running image.py code to visualize each next load

# expected format of data:
test_data_nick = {
    "name": "Nick",
    "warmups": [70, 100, 130, 160, 177.5, 187.5],
    "pounds": False
}

test_data_alex = {
    "name": "Alex",
    "warmups": [100, 110, 120, 130, 135],
    "pounds": True
}

test_data_mario = {
    "name": "Mario",
    "warmups": [70, 120, 160, 190, 207.5, 215],
    "pounds": False
}


def organize_input(data):
    ret = Group()

    for user in data:
        new_lifter = Lifter(user["name"], user["warmups"], pounds=user["pounds"])
        ret.add_member(new_lifter)

    max_warmups = 0
    for lifter in ret.members:
        warmup_count = len(lifter.warmups)
        if warmup_count > max_warmups:
            max_warmups = warmup_count

    warmup_rounds = []
    organizing_group = ret.__copy__()
    for i in range(0, max_warmups):
        loads_for_round = []
        for lifter in organizing_group.members:
            try:
                loads_for_round.append({
                    "name": lifter.name,
                    "load": lifter.warmups.pop(0),
                    "loading": lifter.loading.pop(0)
                })
            except IndexError:
                pass

        warmup_rounds.append(loads_for_round)

    ret = warmup_rounds

    # for access to warmup_rounds, use:
    # warmup_rounds[flight][attempt]["name"]
    # warmup_rounds[flight][attempt]["load"]
    # warmup_rounds[flight][attempt]["loading"]

    print(ret)
    print()
    print(warmup_rounds)
    return ret


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bar_load(0)
    print()
    bar_load(20)
    print()
    bar_load(22.5)
    print()
    bar_load(23)
    print()
    bar_load(70)
    print()
    bar_load(165)
    print()
    bar_load(405, pounds=True)
    print()
    bar_load(227.5)
    print()

    organize_input([test_data_nick, test_data_alex])
