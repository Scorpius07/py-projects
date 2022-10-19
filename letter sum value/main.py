from calc import calculation

def taking_input():
    char = ""
    try:
        char = str(input("Enter the word: "))
    except ValueError:
        print("Invalid Input!"), exit()
    char = char.lower()
    return char


print("Note: This program will help you in calculating the Sum of all letters "
      "in 1 word!")

# 'Total' variable gets the sum of the characters and 
# 'word' gets the "word" that the user enters.
total, word = calculation(taking_input())
print(f'The total sum of every letter in "{word}" is {total}')
