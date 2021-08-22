

# Author: Le Nguyen Thanh Toan
# Email Id: acemarco9@gmail.com

go_on = True
while go_on == True :
    print("--- MAIN MENU ---")
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. All allowed decryptions")
    print("4. Quit")
    user_option = input("Enter an option [1,2,3,4]: ")                                       #allow user to enter their option
    while user_option.isnumeric() == False or int(user_option) < 1 or int(user_option) > 4 :          #if user enter something that not a number, prompt error
        user_option = input("Invalid choice. Enter an option [1,2,3,4]: ")
    user_option = int(user_option)      #convert user_option to a number because right now it's still a string



    if user_option == 1 :
        print("In command 1 - Encrypt string")
        user_string = input("Please enter string to encrypt: ")
        offset = input("Please enter the offset of value (from 1 to 94): ")
        error = True            #I know this way is kinda not necessary but i just want to try another way to control input
        while error == True :
            error = False
            if offset.isnumeric() == False or int(offset) < 1 or int(offset) > 94 :        #check if the offset is a number
                error = True
            if error == True :
                offset = input("Error: You entered the offset incorrectly, please enter again: ")

        offset = int(offset)
        encrypted_string = ""
        number_represent_character = []
        for x in user_string :
            number_represent_character.append(ord(x))

        for i in range(len(number_represent_character)) :
            number_represent_character[i] = number_represent_character[i] + offset
            if number_represent_character[i] > 126 :
                number_represent_character[i] = number_represent_character[i] - 95
           # y is number in number_represent_character
        for y in number_represent_character :
            encrypted_string = encrypted_string + chr(y)
        print("The encrypted string is: ", encrypted_string)
##        i = 0
##        while i < len(number_represent_character) :
##            number_represent_character[i] = int( number_represent_character[i]) + offset
##            if  number_represent_character[i] > 126 :
##                 number_represent_character[i] = int( number_represent_character[i]) - 95
##            i += 1
        #print(number_represent_character)
##        for y in number_represent_character :
##            encrypted_string = encrypted_string + chr(y)
##        print("The encrypted string is: ", encrypted_string)

          #this way is better for controlling the offset
##        while offset.isnumeric() == False or int(offset) < 1 or int(offset) > 92  :     #check if the offset is a numbe
##            offset = input("Error: You entered the offset incorrectly, please enter again: ")
    elif user_option == 2 :
        print("In command 2 - Decrypt string")
        user_string_decrypt = input("Enter string to decrypt: ")
        offset_decrypt = input("Enter the offset value (from 1 to 94) : ")
        error = True
        while error == True :
            error = False
            if offset_decrypt.isnumeric() == False or int(offset_decrypt) < 1 or int(offset_decrypt) > 94 :
                error = True
            if error:
                offset_decrypt = input("You entered the offset incorrectly, please enter again: ")
        offset_decrypt = int(offset_decrypt)        #convert offset for decryption from a string to a integer
        number_represent_character_decrypt = []             #a list of number represent for string
        decrypted_string = ""
        for t in range(len(user_string_decrypt)) :
            number_represent_character_decrypt.append(ord(user_string_decrypt[t]))   #add list of number represent for string
        for u in range(len(number_represent_character_decrypt)) :
            number_represent_character_decrypt[u] = number_represent_character_decrypt[u] - offset_decrypt
            if number_represent_character_decrypt[u] < 32 :
                number_represent_character_decrypt[u] = number_represent_character_decrypt[u] + 95

        for q in number_represent_character_decrypt:
            decrypted_string = decrypted_string + chr(q)
        print("Decrypted string: ", decrypted_string)


    elif user_option == 3 :
        print("In command 3 - brute force")
        offset_decrypt_all = 1
        string_decrypt_all = input("Enter the string to decrypt: ")
        while offset_decrypt_all <= 94:
            number_for_character = []
            decrypted_all_string = ""
            offset_decrypt_all = int(offset_decrypt_all)
            for a in range(len(string_decrypt_all)) :
                number_for_character.append(ord(string_decrypt_all[a]))
            for z in range(len(number_for_character)) :
                number_for_character[z] = number_for_character[z] - offset_decrypt_all
                if number_for_character[z] < 32 :
                    number_for_character[z] = number_for_character[z] + 95
            for m in number_for_character :
                decrypted_all_string = decrypted_all_string + chr(m)
            print("Offset = ", offset_decrypt_all, ".Decryted string = ", decrypted_all_string)
            offset_decrypt_all += 1
    elif user_option == 4 :
        go_on = False
print("Thank you.")





















