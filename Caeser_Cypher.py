letters="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypt=input("Do you want to encrypt a message? (Y/N):")
encrypt=encrypt.upper()

if encrypt == "Y":
    stringtoencrypt=input("Please enter A-Z characters to encrypt:")
    stringtoencrypt=stringtoencrypt.upper()
    ciphershift=input("Please enter a number between 1 and 25 to be your cipher key: ")
    ciphershift=int(ciphershift)
    stringencrypted=""
    for character in stringtoencrypt:
        position = letters.find(character)
        newposition = position+ciphershift
        if character in letters:
            stringencrypted = stringencrypted + letters[newposition]
        else:
            stringencrypted = stringencrypted + character
            
    ciphershift=str(ciphershift)
    print("You used a cipher shift of "+ciphershift)
    print("Your encrypted message reads:")
    print(stringencrypted)
    
    
if encrypt == "N":
    stringtodecrypt=input("Please enter A-Z characters to dencrypt:")
    stringtodecrypt=stringtodecrypt.upper()
    ciphershift=input("Please enter a number between 1 and 25 to be your cipher key: ")
    ciphershift=int(ciphershift)
    stringdecrypted=""
    for character in stringtodecrypt:
        position = letters.find(character)
        newposition = position-ciphershift
        if character in letters:
            stringdecrypted = stringdecrypted + letters[newposition]
        else:
            stringdecrypted = stringdecrypted + character
            
    ciphershift=str(ciphershift)
    print("You used a cipher shift of "+ciphershift)
    print("Your decrypted message reads:")
    print(stringdecrypted)
    


enc_string = input("Enter encrypted string:")

def alphabet():
    letters = "abcdefghijklmnopqrstuvwxyz"
    return(letters)

def dictionary():
    dictionary = open('/Users/gunna/Desktop/Cryptography/Caeser Cypher/sample.txt')
    list_of_words = []
    for word in dictionary.read().split(' '):
        list_of_words.append(word)
    dictionary.close()
    return(list_of_words)

def brute_force(enc_string):
    best_match = 0
    best_match_text = ""
    best_cipher = 0
    # loop to brute
    x = 0
    while x < 26:
        x = x + 1 
        stringtodecrypt=enc_string
        stringtodecrypt=stringtodecrypt.lower()
        ciphershift=int(x)
        stringdecrypted=""
        letters = alphabet()
        for character in stringtodecrypt:
            position = letters.find(character)
            newposition = position-ciphershift
            if character in letters:
                stringdecrypted = stringdecrypted + letters[newposition]
            else:
                stringdecrypted = stringdecrypted + character

        detected_words = 0
    
        for word in stringdecrypted.split(' '):
            word = word.strip(" ")
            word = word.strip(",")
            if word in dictionary():
                detected_words = detected_words + 1

        if detected_words > best_match:
            best_match_text = stringdecrypted
            best_cipher = str(ciphershift)
            number_of_detected_words = detected_words

    result = "Best matched text:",best_match_text,"With Ciphershift of:",best_cipher
    return(result)

answer = brute_force(enc_string)
print(answer)

