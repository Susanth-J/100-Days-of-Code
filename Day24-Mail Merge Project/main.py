PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_temp:
    content = letter_temp.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


