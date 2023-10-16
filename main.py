from Lifter import *
from PlateCounter import *


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
