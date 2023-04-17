
with open("nato_phonetic_alphabet.csv") as data_file:
    data = data_file.readlines()
    clean_data = []
    for chars in data:
        if '\n' in chars:
            clean_data.append(chars.rstrip("\n"))
        elif data[-1] == chars:
            clean_data.append(chars)
    # cleaning the "\n" #

nato_dict = {key[0]: key[2:] for key in clean_data[1:]}  # data[1:]}

phonetic_name = input("what is your name? ")
phonetic_name_list = []

for letter in phonetic_name:
    for code in nato_dict:
        if letter.upper() == code:
            phonetic_name_list.append(nato_dict[code])

print(phonetic_name_list)
