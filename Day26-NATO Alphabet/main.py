import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic = {row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic)

word = input("Enter the word: ").upper()
output_list = [phonetic[letter] for letter in word]
print(output_list)