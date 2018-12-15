
def check_balanced(input_str):
    """
    Checks if input string is balanced paranthesis
    """
    stack = list()
    balanced = True
    for char_ in input_str:
        if char_ == '(':
            stack.append(char_)
        elif char_ == ')':
            if len(stack) == 0:
                balanced = False
                break
            else:
                _ = stack.pop()
        else:
            continue

    if balanced and len(stack) == 0:
        return True

    return False

for x in ['(', ')', '((', '))', ')(', '(())', '(()', ')())()', '( (( )', '()()()', '(( ) ())']:
    print('{} is {}'.format(x, check_balanced(x)))


def generalized_check_balance(input_str):
    """
    Generalization of balanced paranthesis to
    also include '{}' and '[]'
    """
    stack = list()
    balanced = True
    matches = {'}': '{', ')': '(', ']':'['}
    for char_ in input_str:
        if char_ in '[{(':
            stack.append(char_)
        elif char_ in '])}':
            if len(stack) == 0:
                balanced = False
                break
            last_char = stack.pop()
            if matches[char_] != last_char:
                balanced = False
                break
        else:
            pass

    if balanced and len(stack) == 0:
        return True

    return False

for x in ['()', '{}', '[]', '}{', '{]', '( {} ]', '( {} [] )', '(( [ { } )]', '() {} [ () ]']:
    print('{} is {}'.format(x, generalized_check_balance(x)))


def decimal_rep(a):
    """
    Returns decimal representation of a
    """
    div = 1
    stack = list()
    if a == 0:
        return '0'
    while a > 0:
        rem = a % 2
        a = a // 2
        stack.append(rem)

    stack.reverse()
    return ''.join([str(x) for x in stack])

for x in [0, 1, 2, 3, 4, 5, 8, 16, 1024]:
    print("decimal of {} is {}".format(x, decimal_rep(x)))


def infix_to_postfix(str_):
    str_ = ''.join(str_.split())
    opstack = list()
    operators = {'+', '-', '/', '*'}
    operator_precedence = {'/': 1,
                           '*': 1,
                           '+': 0,
                           '-': 0}
    paranthesis = {'(', ')'}
    output = list()
    def _is_operand(char_):
        return ((char_ not in paranthesis) and
                (char_ not in operators) )

    for char_ in str_:
        if _is_operand(char_):
            output.append(char_)
            continue
        if char_ in operators:
            if opstack:
                if opstack[-1] in operators:
                    if operator_precedence[opstack[-1]] >= operator_precedence[char_]:
                        output.append(opstack.pop())
            opstack.append(char_)
            continue
        if char_ == '(':
            opstack.append(char_)
        if char_ == ')':
            last_val = ''
            while last_val != '(':
                last_val = opstack.pop()
                if last_val != '(':
                    output.append(last_val)

    while opstack:
        output.append(opstack.pop())

    return ''.join(output)

for expression in ['A + B + C',
                   'A + B * C',
                   '(A+B)*C',
                   'A * B / C + D',
                   'A*B+C/D*F/G+H+W/N']:
    print("postfix of {} is {}".format(expression, infix_to_postfix(expression)))

def evaluate_postfix(expression):
    def plus(x, y):
        return x+y

    def minus(x, y):
        return x - y

    def multiply(x, y):
        return x*y

    def div(x, y):
        return x / y

    operators = {'+': plus,
                 '/': div,
                 '-': minus,
                 '*': multiply}

    stack = list()
    for char_ in expression:
        if char_ not in operators:
            stack.append(int(char_))
        else:
            left = stack.pop()
            right = stack.pop()
            res = operators[char_](left, right)
            stack.append(res)

    return stack[0]


for x in ['2+3/5', '3*4+5', '(2+3)*4']:
    print("{} = {}".format(x, evaluate_postfix(infix_to_postfix(x))))


class Node:
    """
    Node object for a linked list class
    """
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, next_):
        self.next = next_

    def get_next(self):
        return self.next

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

class LinkedList:
    """
    A simple implementation of Linked List
    """
    def __init__(self):
        self.head = None

    def add(self, val):
        tmp_ = Node(val)
        tmp_.set_next(self.head)
        self.head = tmp_

    def _get_vals(self):
        curr = self.head
        while curr is not None:
            yield curr.get_val()
            curr = curr.get_next()

    def size(self):
        count = 0
        iterator = self._get_vals()
        for _ in iterator:
            count += 1

        return count

    def __len__(self):
        return self.size()

    def __iter__(self):
        return self._get_vals()

    def search(self, target_val):
        iterator = self._get_vals()
        for val in iterator:
            if val == target_val:
                return True
        return False

    def remove(self, target_val):
        curr = self.head
        previous = None
        while curr is not None:
            curr_val = curr.get_val()
            if curr_val == target_val:
                break
            previous = curr
            curr = curr.get_next()
        if curr is None:
            print("item not found for removal")
            return None

        if previous is None:
            self.head = curr.get_next()
            return None

        previous.set_next(curr.get_next())

mylist = LinkedList()
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
print(mylist.size())
print(mylist.search(5))
print(mylist.search(4))
print(mylist.remove(3))
print(mylist.remove(5))
print(len(mylist))
print(list(mylist))
for x in mylist:
    print(x)


bases = [''.join([str(y) for y in list(x)]) for x in [range(n) for n in range(1, 11)]]
print(bases)
def convert_to_string(num_int, base=10):
    BASE = bases[base-1]
    if num_int >= base:
        mod = num_int % base
        return convert_to_string(num_int // base, base=base) + BASE[mod]
    else:
        return BASE[num_int]


for x in [1, 11, 10, 23, 10321]:
    print("str of {} is {}".format(x, convert_to_string(x)))


for x in [1, 2, 3, 4, 5, 6, 16]:
    print("str of {} is {}".format(x, convert_to_string(x, base=2)))


def tree(branch_len, t, min_len=5, delta=15, deg=20):
    if branch_len > min_len:
        t.forward(branch_len)
        t.right(deg)
        tree(branch_len-delta, t, min_len=min_len, delta=delta, deg=deg)
        t.left(2*deg)
        tree(branch_len-delta, t, min_len=min_len, delta=delta, deg=deg)
        t.right(deg)
        t.backward(branch_len)

def tree2(branch_len, t, min_len=5, delta=15, deg=20):
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
    Recursive solution to Hanoi tower
    """
    if height >= 1:
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)

def move_disk(from_pole, to_pole):
    print("move from {} to {}".format(from_pole, to_pole))

move_tower(4, "A", "C", "B")

def optimal_change(change, coins={1, 5, 10, 25}):
    """
    Not efficient recursive call for optimal change problem
    """
    if change in coins:
        return 1, [change]

    counts = list()
    outcomes = list()
    which_coin = list()

    for coin in coins:
       if change > coin:
            a, b = optimal_change(change-coin, coins=coins)
            count = a+1
            counts.append(count)
            outcomes.append(b)
            which_coin.append(coin)

    min_count = min(counts)
    min_index = counts.index(min_count)
    best_outcome = outcomes[min_index]
    best_coin = which_coin[min_index]

    return min_count, best_outcome + [best_coin]

for x in [1, 11, 23, 27]:
    print(x, optimal_change(x))

print(optimal_change(42, coins={1, 10, 20, 21}))

def optimal_change2(change, known_ones, coins={1, 5, 10, 25}):
    """
    Not efficient recursive call for optimal change problem with
    caching
    """
    if change in known_ones:
        return known_ones[change]

    if change in coins:
        known_ones[change] = (1, [change])
        return (1, [change])

    counts = list()
    outcomes = list()
    which_coin = list()

    for coin in coins:
       if change > coin:
            a, b = optimal_change2(change-coin, known_ones, coins=coins)
            count = a+1
            counts.append(count)
            outcomes.append(b)
            which_coin.append(coin)

    min_count = min(counts)
    min_index = counts.index(min_count)
    best_outcome = outcomes[min_index]
    best_coin = which_coin[min_index]

    known_ones[change] = (min_count, best_outcome + [best_coin])
    return min_count, best_outcome + [best_coin]

print(optimal_change2(63, known_ones=dict(), coins={1,2,5,10,20,21}))

def optimal_change3(change, coins={1,2,5, 10, 25}):
    """
    dynamic programming approach to optimal change
    """
    optimals = dict()
    if change < min(coins):
        raise ValueError("change must be greater than min")
    optimals[min(coins)] = 1, [min(coins)]
    optimals[0] = 0, []
    for next_val in range(min(coins)+1, change+1):
        potentials = list()
        associate_coins = list()
        previous_coins = list()
        for coin in coins:
            x = optimals.get(next_val - coin)
            if x is not None:
                a, b = x
                potentials.append(1+a)
                associate_coins.append(coin)
                previous_coins.append(b)
        best_val = min(potentials)
        best_index = potentials.index(best_val)
        optimals[next_val] = best_val, previous_coins[best_index] + [associate_coins[best_index]]
    return optimals

print(optimal_change3(63, coins={1,2,5,10,20,21}).get(63))




