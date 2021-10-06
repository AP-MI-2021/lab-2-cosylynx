import math


def get_temp(temp: float, temp_from: str, temp_to: str) -> float:
    """
    Transformă o temperatură dată într-o scară dată (K, F sau C) într-o altă scară dată.
    :temp: temperatura
    :temp_from: scara din care se face conversia
    :temp_to: scara în care se face conversia
    :conv_temp: temperatura convertită din prima scară în cea de-a doua scară
    """
    conv_temp = temp
    if temp_from == 'C':
        if temp_to == 'K':
            conv_temp = temp + 273.15
        elif temp_to == 'F':
            conv_temp = temp * 9/5 + 32
    elif temp_from == 'F':
        if temp_to == 'C':
            conv_temp = (temp - 32) * 5/9
        elif temp_to == 'K':
            conv_temp = (temp - 32) * 5/9 + 273.15
    elif temp_from == 'K':
        if temp_to == 'F':
            conv_temp = (temp-273.15) * 9/5 + 32
        elif temp_to == 'C':
            conv_temp = temp - 273.15
    else:
        return False
    return conv_temp


def get_cmmdc(n1, n2):
    '''
    :n1: primul număr
    :n2: cel de-al doilea număr
    :return: cmmdc al celor două numere
    '''
    while n2:
        remainder = n1 % n2
        n1 = n2
        n2 = remainder
    return n1


def get_cmmmc(numbers: list[int]) -> int:
    """
    Calculează CMMMC al n numere date.
    :numbers: numere întregi preluate dintr-o listă
    :return: cel mai mic multiplu comun al numerelor din listă
    CMMMC = Produsul numerelor din lista / CMMDC
    """
    aux = get_cmmdc(numbers[0], numbers[1])
    cmmmc = (numbers[0] * numbers[1]) // aux
    sub_numbers = numbers[2:len(numbers)]
    for x in sub_numbers:
        aux = get_cmmdc(cmmmc, x)
        cmmmc = (cmmmc * x) // aux
    return cmmmc


def get_largest_prime_below(n):
    '''
    Găsește ultimul număr prim mai mic decât un număr dat.
    :param n: un număr întreg
    :return: cel mai mare număr prim mai mic decât numărul dat
    '''

    for numar in reversed(range(n)):
        prime = True
        if numar < 2:
            prime = False
        if numar == 2:
            prime = True
        for i in range(2, int(math.sqrt(numar)+1)):
            if numar % i == 0:
                prime = False
        if prime:
            return numar
    return False


def test_get_temp():
    assert get_temp(1, 'C', 'C') == 1
    assert get_temp(1, 'C', 'F') == 33.8
    assert get_temp(1, 'C', 'K') == 274.15
    assert get_temp(2, 'F', 'F') == 2
    assert get_temp(2, 'F', 'C') == -16.666666666666668
    assert get_temp(2, 'F', 'K') == 256.4833333333333
    assert get_temp(3, 'K', 'K') == 3
    assert get_temp(3, 'K', 'C') == -270.15
    assert get_temp(3, 'K', 'F') == -454.27
    assert get_temp(99, "xmf", "yayx") is False


def test_get_cmmmc():
    assert get_cmmmc([2, 3, 4, 5, 6]) == 60
    assert get_cmmmc([0, 12, 4]) == 0
    assert get_cmmmc([21, 4]) == 84
    assert get_cmmmc([4, 3, 4, 5]) == 60


def test_get_largest_prime_below():
    assert get_largest_prime_below(1) is False
    assert get_largest_prime_below(-1) is False
    assert get_largest_prime_below(-7) is False
    assert get_largest_prime_below(21) == 19
    assert get_largest_prime_below(7042) == 7039
    assert get_largest_prime_below(7041) == 7039
    assert get_largest_prime_below(2) is False
    assert get_largest_prime_below(3) == 2


def main():
    while True:
        print('1. Transformarea temperaturii dintr-o scară în alta')
        print('2. Calcularea CMMMC al n numere')
        print('3. Găsirea unui număr prim mai mic decât un număr dat')
        print('x. Încheie programul')
        optiune = input('Alege opțiunea: ')
        if optiune == '1':
            temperatura = float(input("Introduceți valoarea temperaturii: "))
            temp_din = input("Introduceți unitatea de măsură din care doriți să faceți conversia: ")
            while temp_din not in ['C', 'K', 'F']:
                temp_din = input("Introduceți una dintre literele C, F sau K.. ")
            temp_in = input("Introduceți unitatea de măsură în care doriți să faceți conversia: ")
            while temp_in not in ['C', 'K', 'F']:
                temp_in = input("Introduceți una dintre literele C, F sau K.. ")
            convertit = get_temp(temperatura, temp_din, temp_in)
            print(f"Temperatura în {temp_in} este de {convertit}° !")

        elif optiune == '2':
            numere_str = input('Dați numerele separate printr-un spațiu: ')
            numere_str_lst = numere_str.split(' ')
            numere_int_lst = []
            for nr_str in numere_str_lst:
                numere_int_lst.append(int(nr_str))
            cmmmc = get_cmmmc(numere_int_lst)
            print(f"Cel mai mic multiplu comun al acestor numere este {cmmmc}.")

        elif optiune == '3':
            nr_ales = int(input("Dați un număr natural :"))
            largest_prime_below = get_largest_prime_below(nr_ales)
            if largest_prime_below:
                print(f"Cel mai mic număr prim mai mic decât {nr_ales} este {largest_prime_below}.")
            else:
                print(f"Nu există niciun număr prim mai mic decât {nr_ales}")
        elif optiune == 'x':
            break
        else:
            print('Opțiune invalidă!')


test_get_temp()
test_get_cmmmc()
test_get_largest_prime_below()
main()
