# 1st method
# import turtle
# chima =turtle.Turtle()

# 2nd method 

# Turtle graphics Documentation https://docs.python.org/3/library/turtle.html
# Use it when required 

# from turtle import Turtle , Screen

# chima = Turtle()
# chima.shape("turtle")
# chima.color("gold1")    # colors and their names https://cs111.wellesley.edu/reference/colors

# #moving the turtle 
# chima.forward(100.00)

# my_screen = Screen()
# print(my_screen.window_height)
# my_screen.exitonclick()


# for searching the python packages use https://pypi.org/ 


# Using pretty table for the creation of the table 
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon name", "Type", "Id"]
# 1st method of adding data 

# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])

#2nd method of adding data
table.add_rows(
    [
        ["Pikachu", "Electric . Ground" ,36  ],
        ["Charizard", "Fire · Flying", 85, ],
        ["Blastoise", "Water ", 88],
        ["Mewtwo", "Psychic", 151 ],
        ["Zygarde", "Dragon · Ground",150],
        ["Yveltal", "Dark · Flying", 149],
        ["Dragonite", "Dragon · Flying", 147],
    ]
)

table.align = "l"

print(table)