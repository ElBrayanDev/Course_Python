from turtle import Turtle, Screen # importing Turtle class and instantiating

graphics = Turtle()
print(graphics)
graphics.shape("turtle")
graphics.color("coral")
graphics.forward(100)
graphics.circle(25)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from pretty_table_printer import pretty_table_printer
table = pretty_table_printer()
print(table)