# recursive_polygon_collab.py
# =====================================
# Boilerplate: Recursive Polygon Pattern with Inward Triangles
# Python Turtle – Collaboration Ready
# =====================================

import turtle

# ================================
# Part 1: User Input (before opening turtle)
# ================================
# TODO: Person 1 – Implement user input
def get_user_input():
    """
    Prompt user for polygon details and recursion depth.
    Rules:
    - Number of sides (n_sides)
    - Side length in pixels (side_length)
    - Recursion depth (depth)
    """
    n_sides = 0       # TODO: replace with input prompt
    side_length = 0   # TODO: replace with input prompt
    depth = 0         # TODO: replace with input prompt
    return n_sides, side_length, depth

# ================================
# Part 2: Turtle Setup (after input)
# ================================
# TODO: Person 1 – Implement turtle setup
def setup_turtle():
    """
    Set up turtle screen and turtle.
    - Screen background: white
    - Turtle speed: fastest
    - Hide turtle for clean drawing
    """
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    return t, screen

# ================================
# Part 3: Recursive Edge Function
# ================================
def draw_edge(t, length, depth):
    """
    Draw a single edge recursively with inward indentation.
 
    Rules:
    - Depth 0: straight line
    - Depth 1: line becomes: ——\⁄—— (one inward indentation)
    - Depth 2+: apply indentation recursively to each of the 4 segments
 
    Inward triangle implementation:
    1. Divide line into 3 segments
    2. Draw first segment
    3. Turn right 60° (inward), draw second segment
    4. Turn left 120° to continue, draw third segment
    5. Turn right 60° to return direction, draw fourth segment
    """
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

# ================================
# Part 4: Polygon Drawing Function
# ================================
def draw_polygon(t, n_sides, side_length, depth):
    """
    Draw a complete polygon using recursive edges.
 
    Rules:
    - Loop through all sides
    - Draw each edge recursively
    - Turn right by interior angle after each edge: angle = 360 / n_sides
    """
    angle = 360 / n_sides
    for _ in range(n_sides):
        draw_edge(t, side_length, depth)
        t.right(angle)
# ================================
# Part 5: Program Execution
# ================================
# TODO: Both – integrate parts
def main():
    # 1. Take user input first
    n_sides, side_length, depth = get_user_input()

    # 2. Setup turtle after input
    t, screen = setup_turtle()

    # 3. Optional: reposition for better view
    t.penup()
    t.goto(-side_length/2, side_length/2)
    t.pendown()

    # 4. Draw the polygon
    draw_polygon(t, n_sides, side_length, depth)

    # 5. Keep window open
    screen.mainloop()

if __name__ == "__main__":
    main()
