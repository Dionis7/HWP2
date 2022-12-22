number = int(input('Введите число N: '))
def formula(number):
    count = 1
    for i in range (1, number+1):
        count*=i
        print(count)
formula(number)