def main():
    num = int(input("Insira um numero qualquer: "))
    print(f"The sum of even numbers are: {EvenSum(num)}")

def EvenSum(num : int):
    aux = num
    sum = 0

    while aux != 0 :
        if not (aux % 10)%2:
            sum += aux % 10
        aux = aux//10

    return sum

main()