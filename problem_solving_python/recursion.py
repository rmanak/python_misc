
# This is a global variable used for base lookup characters
BASES = [''.join([str(y) for y in list(x)]) for x in [range(n) for n in range(1, 11)]]
print(BASES)

def convert_to_string(num_int, base=10):
    """
    converts an integer number to its string repr in base=base
    """
    base_chars = BASES[base-1]
    if num_int >= base:
        mod = num_int % base
        return convert_to_string(num_int // base, base=base) + base_chars[mod]
    else:
        return base_chars[num_int]


for x in [1, 11, 10, 23, 10321]:
    print("str of {} is {}".format(x, convert_to_string(x)))


for x in [1, 2, 3, 4, 5, 6, 16]:
    print("str of {} is {}".format(x, convert_to_string(x, base=2)))


def tree(branch_len, t, min_len=5, delta=15, deg=20):
    """
    Recursively draws a tree using a Turtle object `t`
    """
    if branch_len > min_len:
        t.forward(branch_len)
        t.right(deg)
        tree(branch_len-delta, t, min_len=min_len, delta=delta, deg=deg)
        t.left(2*deg)
        tree(branch_len-delta, t, min_len=min_len, delta=delta, deg=deg)
        t.right(deg)
        t.backward(branch_len)

def tree2(branch_len, t, min_len=5, delta=15, deg=20):
    """
    Same as above, but different way of thinking about the base case
    of the recursion
    """
    if branch_len > min_len:
        t.forward(branch_len)
        t.right(deg)
        t.forward(branch_len)
        tree(branch_len-delta, t, min_len=min_len, delta=delta, deg=deg)
        t.backward(branch_len)
        t.left(2*deg)
        t.forward(branch_len)
        tree(branch_len-delta, t, min_len=min_len, delta=delta, deg=deg)
        t.backward(branch_len)
        t.right(deg)
        t.backward(branch_len)


def draw_tree():
    """
    calls the tree to draw the tree
    """
    import turtle
    turt = turtle.Turtle()
    win = turtle.Screen()
    turt.color("green")
    tree(75, turt)
    turt.left(90)
    turt.color("red")
    tree2(75, turt)
    win.exitonclick()

if False:
    draw_tree()

def kotch(seg_len, t):
    """
    Recursive drawing of Kotch fractal
    """
    if seg_len < 20:
        t.forward(seg_len)
    else:
        kotch(seg_len/3, t)
        t.left(60)
        kotch(seg_len/3, t)
        t.right(120)
        kotch(seg_len/3, t)
        t.left(60)
        kotch(seg_len/3, t)

def draw_kotch():
    """
    Driver function for kotch
    """
    import turtle
    turt = turtle.Turtle()
    win = turtle.Screen()
    turt.color("green")
    kotch(20*3**2, turt)
    win.exitonclick()

if False:
    draw_kotch()

# This is the most elegent solution using recurssion!!

def move_tower(height, from_pole, to_pole, with_pole):
    """
    Recursive solution to Hanoi tower,
    this is the most elegent representation of a problem
    solving with recursion!!!
    """
    if height >= 1:
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)

def move_disk(from_pole, to_pole):
    print("move from {} to {}".format(from_pole, to_pole))

move_tower(4, "A", "C", "B")


