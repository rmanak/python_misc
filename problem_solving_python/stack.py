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
    """
    converts an infix expression ( "A+B*C" ) to
    an postfix form (ABC*+)
    """
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
    """
    Evaluates a postfix expression using a shift/stack
    """
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


