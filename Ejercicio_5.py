def es_bisiesto(year=2023):
    if ((year % 4) == 0):
        if (not((year % 100) == 0) or ((year % 400) == 0)):
            print('El año ' + str(year) + ' es bisiesto')
    else:
        print('El año ' + str(year) + ' NO es bisiesto')

if __name__ == '__main__':
    print('Por favor digite el año a validar ==> ')
    year = int(input())
    es_bisiesto(year)