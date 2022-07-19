from calculations import calculation
from messages import ms

opers = '+-*/'
memory = 0


def read_calc():
    print(ms[0])
    return input()


def check_calc():
    global memory
    while True:
        calc = read_calc()
        try:
            x, oper, y = calc.split()
            if x == 'M':
                x = memory
            if y == 'M':
                y = memory
            x = float(x)
            y = float(y)
        except Exception:
            print(ms[1])
        else:
            if oper in opers:
                check(x, y, oper)
                if y == 0 and oper == '/':
                    print(ms[3])
                    continue
                else:
                    return x, oper, y
            print(ms[2])


def addition_check(res):
    if is_one_digit(res):
        print(ms[10])
        answer_10 = input()
        if answer_10 == 'y':
            print(ms[11])
            answer_11 = input()
            if answer_11 == 'y':
                print(ms[12])
                answer_12 = input()
                if answer_12 == 'y':
                    return True
        return False
    return True


def save_result(res):
    global memory
    print(ms[4])
    answer_4 = input()
    if answer_4 == 'y':
        if addition_check(res=res):
            memory = res


def continue_calculations():
    print(ms[5])
    answer_5 = input()
    if answer_5 == 'y':
        return True
    return False


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += ms[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += ms[7]
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += ms[8]
    if msg != '':
        msg = ms[9] + msg
    print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    return False


def wrapper():
    x, oper, y = check_calc()
    return calculation(x=x, oper=oper, y=y)


def main():
    while True:
        res = wrapper()
        print(res)
        save_result(res=res)
        if not continue_calculations():
            break


if __name__ == '__main__':
    main()
