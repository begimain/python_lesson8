from typing import Union, Any


def arithmetic(x, y, z):
    if z == "+":
        return (x + y)
    elif z == "-":
        return (x - y)
    elif z == "*":
        return (x * y)
    elif z == "/":
        return (x / y)
    else:
        return ("Invalid operation")


# while True:

# def is_year_leap(x):
#
#     if x % 4 == 0:
#         if x % 400 == 0:
#             print('True')
#         elif x % 100 != 0:
#             print('True')
#         else:
#             print('False')
#     else:
#         print('False')


def square(a):
    p = 4 * a
    s = a * a
    d = (a ** 2) / 2
    d = d ** 0.5

    k = (p, s, d)

    return k


print(square(16))


def season(month):
    if month == 12 or month < 3:
        return "Зима"
    elif month == 3 or month < 6:
        return "Весна"
    elif month == 6 or month < 9:
        return "Лето"
    else:
        return "Осень"


# month = input("Введите месяц(число):")

# while True:
#     if month.isdigit():
#
#         # month = input("Введите месяц(число):")
#         continue
#     else:
#         break
# month = int(month)
# while True:
#  if month == 0:
#
#      # month = input("Введите месяц(число):")
#      continue
#  else:
#      break
#
# month = int(month)
#
# answer = season(month)
# print(answer)

n = int(input())
m = int(input())
y = int(input())


def bank(n, m, y):
    nal = n
    year = y

    def money(year = None):
        if year <= 0:
            return n
        else:
            nal: Union[float, Any] = n * 1.1 + m
            year = year - 1
            return money()


from math import sqrt


def is_prime(number):

    if number % 2 == 0 and number != 2:
        return False

    if number == 0 or number == 1:
        return False


    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:
            return False
    return True

n = int(input('Введите число: '))
print(is_prime(n))

if __name__ == '__main__':
    print(arithmetic(2, 3, '+'))
    print(arithmetic(2, 2, '*'))
    print(arithmetic(4, 2, '-'))
    print(arithmetic(4, 2, '/'))
    print(arithmetic(4, 2, 0))
    print(n)
