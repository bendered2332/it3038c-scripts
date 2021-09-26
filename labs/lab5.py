# Take a word as input and count how many letters, how many vowels and how many consonants.

vowels = ['a', 'e', 'i', 'o', 'u']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

str = input("Enter a string: ").lower()

vowel_Counter = 0
consonant_Counter = 0

for x in str:
    if x in vowels:
        vowel_Counter += 1
        letter_Counter += 1
    else:
        consonant_Counter += 1
        letter_Counter = + 1

letter_Counter = vowel_Counter + consonant_Counter

print("Letters: ", letter_Counter)
print("Vowels: ", vowel_Counter)
print("Consonants: ", consonant_Counter)
