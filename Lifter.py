from PlateCounter import *


def organize_input(data):
    rack_group = Group()

    for user in data:
        new_lifter = Lifter(user["name"], user["warmups"], pounds=user["unit"])
        rack_group.add_member(new_lifter)

    max_warmups = 0
    for lifter in rack_group.members:
        warmup_count = len(lifter.warmups)
        if warmup_count > max_warmups:
            max_warmups = warmup_count

    warmup_rounds = []
    organizing_group = rack_group.__copy__()
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

    print(rack_group)
    print(warmup_rounds)
    print(ret)
    return ret


class Lifter:
    def __init__(self, name, warmups, pounds=False):
        self.name = name
        self.warmups = [i for i in warmups if i != 0]
        self.pounds = pounds
        self.loading = self.serialize_warmups(pounds=pounds)

        if self.pounds:
            self.warmups = [round(round(lbs / 2.2046, 3) / 2.5) * 2.5 for lbs in warmups]
            self.pounds = False

    def serialize_warmups(self, pounds=False):
        ret = [bar_load(warm_up, pounds=pounds) for warm_up in self.warmups]
        return ret

    def __str__(self):
        load_list = []
        for load in self.loading:
            load_list.append(load.__str__())

        load_list = "\n".join(load_list)
        print(load_list)
        ret = {self.name: load_list}
        return str(ret)

    def __copy__(self):
        copy_instance = Lifter(name=self.name, warmups=self.warmups, pounds=self.pounds)
        return copy_instance


class Group:
    def __init__(self, lifters):
        self.members = lifters

    def __init__(self):
        self.members = []

    def __str__(self):
        ret = []
        for lifter in self.members:
            ret.append(lifter.__str__())

        return "\n".join(ret)

    def __copy__(self):
        copy_instance = Group()
        for lifter in self.members:
            copy_instance.add_member(lifter.__copy__())

        return copy_instance

    def add_member(self, new_member):
        self.members.append(new_member)


DEFAULT_LIFTER = Lifter("AAAAAAAAAAAAAAAA", [720])
