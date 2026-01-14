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
# TODO: Person 2 – Implement recursion
def draw_edge(t, length, depth):
    """
    Draw a single edge recursively with inward indentation.

    Rules to implement:
    - Depth 0: straight line
    - Depth 1: line becomes: ——\⁄—— (one inward indentation)
    - Depth 2+: recursively apply indentation to all 4 new segments
    - Inward triangle logic:
        1. Divide edge into 3 segments
        2. Draw first segment
        3. Turn right 60° (inward), draw second segment
        4. Turn left 120° to continue, draw third segment
        5. Turn right 60° to return direction, draw fourth segment
    """
    # TODO: implement recursion logic
    pass

# ================================
# Part 4: Polygon Drawing Function
# ================================
# TODO: Person 1 – Implement polygon drawing loop
def draw_polygon(t, n_sides, side_length, depth):
    """
    Draw a complete polygon using recursive edges.

    Rules:
    - Loop through all sides of the polygon
    - For each side, call draw_edge()
    - Turn right by interior angle after each edge:
      angle = 360 / n_sides
    """
    # TODO: implement polygon drawing loop
    pass

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
