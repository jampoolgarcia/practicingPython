# exercist three - make a program that asks a character and indicates whether it is a vowel or not

char = input("Enter a charater: ").lower()

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print(f"Yes, it is a vowel")
else:
    print(f"No, it not is a vowel")