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
 