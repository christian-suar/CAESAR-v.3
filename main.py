
message = "That Quick Fox Jumped Over 3 Sleepy Rabbits 29 Times."
character_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
num = 101


def ceaser_cipher(text:str, shift:str):
    result = ""
    for char in text:
        if char in character_list:
            result += character_list[(character_list.index(char)+shift)%62] # first instance of letter from text in charlist, shift by 101, divide by 62 for remainder for new char from charlist
        else:
            result += char

    return result

def ceaser_decipher(secret_message:str): 
 
    shift = 0

    while shift < 63:
        result = ""
        for char in secret_message:
            if char in character_list:
                result += character_list[(character_list.index(char)-shift)%62]
            else:
                result += char
        print(result + "\n")
        shift += 1



print("#########################################################################################################")
print("Encrypted: ")
print(ceaser_cipher(message,num))

print()

secret_message = ceaser_cipher(message,num)

print("Decrypted (original message): ")
ceaser_decipher(secret_message)
print("#########################################################################################################")