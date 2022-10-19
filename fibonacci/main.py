def particular_num(previous_result01, previous_result02):
    n, sum1 = 0, 0
    n = int(input("\nWhich Fibonacci number do you want: "))
    if n == 0:
        print(0), exit()
    if n == 1:
        print(1), exit()

    for num in range(n - 1):
        sum1 = previous_result01 + previous_result02
        previous_result01 = previous_result02
        previous_result02 = sum1
    print(sum1)


def next_num(previous_result01, previous_result02):
    end, num = False, 0
    print("\nFirst Fib-Number: 0")
    while not end:
        num = previous_result01 + previous_result02
        previous_result01 = previous_result02
        previous_result02 = num
        print(f"\nThe Next Fib-Number: {num}")
        choice = str(input("Do you want to continue?\n(Y)es! | (N)o!\n> ", allowRegexes=[r'y|n']))  # inputStr X
        if choice.lower() == "n":
            print("Hoping you liked the program :)"), exit()


print("Hello! This Program will give you Fibonacci Series!")
previous_result1, previous_result2 = 1, 0
decision = int(input("\nWhich way do you want to find your Fibonacci number?\n(1) I've a specific number. Find which " 
                        "fibonacci number is at that number's position\n(2)Keep giving me the next Fibonacci Number. "
                        "I'll say when to end (annoying)\nDecision: "))
if decision == 1:
    particular_num(previous_result1, previous_result2)
if decision == 2:
    next_num(previous_result1, previous_result2)
