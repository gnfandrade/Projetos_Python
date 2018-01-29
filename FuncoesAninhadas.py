# Função aninhada para multiplicar números.
def firstElement(num1, num2):
    """

    :param fisrt Number:
    :param Second Number:
    :return: secondElement()
    """
    def secondElement():
        return num1 * num2
    return secondElement()

def main():
    for i in range(11):
       print("3 x %i = %i"%(i, firstElement(3, i)))


main()