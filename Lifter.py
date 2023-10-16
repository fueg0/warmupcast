from PlateCounter import *


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
