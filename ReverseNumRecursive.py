def ReversedR(num : int, r_num : int = 0):
    if num == 0:
        return r_num

    r_num *= 10

    return ReversedR(num // 10, r_num + num % 10)

def main():
    num = int(input("Insert a integer number: "))
    print(f"The reversed number is {ReversedR(num)}")

main()