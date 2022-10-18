print("Tämä ohjelma muuttaa kokonimesi aakkoset, niitä vastaaviksi numeroiksi ja summaa ne.")
print("Ohjelma käyttää pohjoismaalaisia aakkosia.")
input_string = input('Anna kokonimesi: ')
user_list = list(input_string)
# print list
print('tuotettu lista: ', user_list)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    if (user_list[i] == "A" or user_list[i] == "a"):
        user_list[i] = 1
    elif (user_list[i] == "B" or user_list[i] == "B"):
        user_list[i] = 2
    elif (user_list[i] == "C" or user_list[i] == "c"):
        user_list[i] = 3
    elif (user_list[i] == "D" or user_list[i] == "d"):
        user_list[i] = 4
    elif (user_list[i] == "E" or user_list[i] == "e"):
        user_list[i] = 5
    elif (user_list[i] == "F" or user_list[i] == "f"):
        user_list[i] = 6
    elif (user_list[i] == "G" or user_list[i] == "g"):
        user_list[i] = 7
    elif (user_list[i] == "H" or user_list[i] == "h"):
        user_list[i] = 8
    elif (user_list[i] == "I" or user_list[i] == "i"):
        user_list[i] = 9
    elif (user_list[i] == "J" or user_list[i] == "j"):
        user_list[i] = 10
    elif (user_list[i] == "K" or user_list[i] == "k"):
        user_list[i] = 11
    elif (user_list[i] == "L" or user_list[i] == "l"):
        user_list[i] = 12
    elif (user_list[i] == "M" or user_list[i] == "m"):
        user_list[i] = 13
    elif (user_list[i] == "N" or user_list[i] == "n"):
        user_list[i] = 14
    elif (user_list[i] == "O" or user_list[i] == "o"):
        user_list[i] = 15
    elif (user_list[i] == "P" or user_list[i] == "p"):
        user_list[i] = 16
    elif (user_list[i] == "Q" or user_list[i] == "q"):
        user_list[i] = 17
    elif (user_list[i] == "R" or user_list[i] == "r"):
        user_list[i] = 18
    elif (user_list[i] == "S" or user_list[i] == "s"):
        user_list[i] = 19
    elif (user_list[i] == "T" or user_list[i] == "t"):
        user_list[i] = 20
    elif (user_list[i] == "U" or user_list[i] == "u"):
        user_list[i] = 21
    elif (user_list[i] == "V" or user_list[i] == "v"):
        user_list[i] = 22
    elif (user_list[i] == "W" or user_list[i] == "w"):
        user_list[i] = 23
    elif (user_list[i] == "X" or user_list[i] == "x"):
        user_list[i] = 24
    elif (user_list[i] == "Y" or user_list[i] == "y"):
        user_list[i] = 25
    elif (user_list[i] == "Z" or user_list[i] == "z"):
        user_list[i] = 26
    elif (user_list[i] == "Å" or user_list[i] == "å"):
        user_list[i] = 27
    elif (user_list[i] == "Ä" or user_list[i] == "ä"):
        user_list[i] = 28
    elif (user_list[i] == "Ö" or user_list[i] == "ö"):
        user_list[i] = 29
    elif (user_list[i] == " "):
        user_list[i] = 0
    elif ValueError:
        print("Alkio ", user_list[i],  " ei ollut ohjeiden mukainen ja se hylätään")
        user_list[i] = 0
        continue
    else:
        print("Alkio ", user_list[i],  " ei ollut ohjeiden mukainen ja se hylätään")
    user_list[i] = int(user_list[i])
# Calculating the sum of list elements
print("Laskettu summa = ", sum(user_list))
