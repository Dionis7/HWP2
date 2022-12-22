number = input('Введите вещественное число: ')
def sum (number):
    sum = 0
    for i in number:
        if i != ',':
            sum = sum + int(i)
    return sum
print (sum(number))