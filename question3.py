
import turtle


def get_user_input():
    n_sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))
    return n_sides, side_length, depth



def setup_turtle():
    # Set up turtle screen and turtle.
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0) 
    t.hideturtle()
    return t, screen


def draw_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        segment = length / 3
        draw_edge(t, segment, depth - 1)       # 1st segment
        t.right(60)                            # turn inward
        draw_edge(t, segment, depth - 1)       # 2nd segment
        t.left(120)                            # turn to continue
        draw_edge(t, segment, depth - 1)       # 3rd segment
        t.right(60)                            # return direction
        draw_edge(t, segment, depth - 1)       # 4th segment


def draw_polygon(t, n_sides, side_length, depth):
    angle = 360 / n_sides
    for _ in range(n_sides):
        draw_edge(t, side_length, depth)
        t.right(angle)

def main():
    # Take user input 
    n_sides, side_length, depth = get_user_input()

    # Setup turtle after input
    t, screen = setup_turtle()

    t.penup()
    t.goto(-side_length/2, side_length/2)
    t.pendown()

    # Draw the polygon
    draw_polygon(t, n_sides, side_length, depth)

    # Keep window open
    screen.mainloop()

if __name__ == "__main__":
    main()
