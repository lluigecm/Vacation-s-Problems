def EvenSumR(num : int, res : int = 0):
    if num < 2:
        return res

    if not (num%10)%2:
        res += num % 10

    return EvenSumR(num // 10, res)

def main():
    num = int(input("Insira um numero qualquer: "))
    print(f"The sum of even numbers are: {EvenSumR(num = num)}")

main()