import turtle

# Get inputs from the user
def get_user_input():
    n_sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))
    return n_sides, side_length, depth


# Setup turtle screen and turtle
def setup_turtle():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)          # Fast drawing
    t.hideturtle()      # Hide turtle cursor

    return t, screen


# Draw one edge using recursion
def draw_edge(t, length, depth):
    # Base case: draw a straight line
    if depth == 0:
        t.forward(length)
    else:
        segment = length / 3

        # First segment
        draw_edge(t, segment, depth - 1)

        # Inward triangle
        t.right(60)
        draw_edge(t, segment, depth - 1)

        t.left(120)
        draw_edge(t, segment, depth - 1)

        t.right(60)

        # Last segment
        draw_edge(t, segment, depth - 1)


# Draw the polygon using recursive edges
def draw_polygon(t, n_sides, side_length, depth):
    angle = 360 / n_sides

    for _ in range(n_sides):
        draw_edge(t, side_length, depth)
        t.right(angle)


def main():
    # Take user input
    n_sides, side_length, depth = get_user_input()

    # Setup turtle
    t, screen = setup_turtle()

    # Move turtle to a better start position
    t.penup()
    t.goto(-side_length / 2, side_length / 2)
    t.pendown()

    # Draw the shape
    draw_polygon(t, n_sides, side_length, depth)

    # Keep window open
    screen.mainloop()


if __name__ == "__main__":
    main()
