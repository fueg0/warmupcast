import wx

LOADING = {"red": 0,
           "blue": 0,
           "yellow": 0,
           "green": 0,
           "white": 0,
           "black": 0,
           "silver": 0}

WEIGHTS = {"red": 25,
           "blue": 20,
           "yellow": 15,
           "green": 10,
           "white": 5,
           "black": 2.5,
           "silver": 1.25}

PLATES = ["red", "blue", "yellow", "green", "white", "black", "silver"]


def bar_load(weight, pounds=False):
    if pounds:
        weight = round(weight / 2.2046, 3)

    print("INPUT WEIGHT: ", weight, "kgs")
    weight = round(weight / 2.5) * 2.5
    print("WEIGHT IS: ", weight)
    ret = PlateCounter()
    ret.total = weight
    plate_load = weight - 20

    if weight < 20:
        ret = {"weight": weight,
               "loading": ret}
        print(ret)
        return ret

    ### START HERE
    # change this logic to utilize PlateCounter features
    for plate in ret.count:
        while plate.bar_weight <= plate_load:
            plate.count += 1
            plate_load -= plate.bar_weight

    print("FINAL LOAD IS: ", ret)
    return ret


class Plate:
    def __init__(self, kg_weight, color, scale, name):
        self.weight = kg_weight
        self.color = color
        self.scaling = scale
        self.name = name
        self.count = 0
        self.bar_weight = kg_weight * 2

    def __str__(self):
        ret = {"weight": self.weight,
               "name": self.name,
               "count": self.count
               }

        return str(ret)

    def __dict__(self):
        ret = {"weight": self.weight,
               "name": self.name,
               "count": self.count,
               "color": self.color,
               "scaling": self.scaling,
               "bar_weight": self.bar_weight
               }

        return ret


class PlateCounter:
    def __init__(self):
        self.total = 0
        self.red = Plate(25, wx.RED, 1, "red")
        self.blue = Plate(20, wx.BLUE, 1, "blue")
        self.yellow = Plate(15, wx.YELLOW, 0.8, "yellow")
        self.green = Plate(10, wx.GREEN, 0.6, "green")
        self.white = Plate(5, wx.WHITE, 0.4, "white")
        self.black = Plate(2.5, wx.BLACK, 0.2, "black")
        self.silver = Plate(1.25, wx.LIGHT_GREY, 0.1, "silver")
        self.count = [self.red, self.blue, self.yellow, self.green, self.white,
                      self.black, self.silver]

    def __str__(self):
        ret = [f"total: {self.total}"]
        for plate in self.count:
            ret.append(plate.__str__())

        return "\n".join(ret)

    def loading(self):
        ret = {}
        for plate in self.count:
            ret[plate.name] = plate.count

        return ret
