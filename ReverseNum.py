def main():
    num = int(input("Insert a integer number: "))
    print(f"The reversed number is {reverse(num)}")

def reverse(num : int):
    aux = num
    reverse = 0

    while aux != 0:
        reverse *= 10
        reverse += aux % 10
        aux = aux//10

    return reverse

main()