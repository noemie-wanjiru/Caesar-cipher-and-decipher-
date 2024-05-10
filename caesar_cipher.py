#create a list named alphabet whose elements consist of the english alphabet
alphabet=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# cipher with left shift 
"""We create a function Cipher to encrpyt data using a caesar cipher with a left shift, the function takes no arguments
It requires the user to enter the cipher key and the text to be encryted"""

def cipher():
    try:
        key=int(input('Enter the cipher key'))
        text=str(input('Enter the text to be ciphered')).lower()
    
        #We create an empty string cipheredtext to store the our ciphered text
        cipheredtext=str()
    
        # We use a for loop to iterate through the text 
        for element in text:
    
            """ An if statement is used to check if an element is in the alphabet list, if present we check the location of the element in the 
            alphabet list and store it in a variable, index."""
            
            if element in alphabet:
                index=alphabet.index(element)
                """To determine the ciphered element we take the modulus of the difference between the index (position of the element to be ciphered) 
                and the key, by the length of the alphabet."""
                c=(index-key)%len(alphabet)
                #we use the index c to identifiy the ciphered element and store it in a variable b
                b=alphabet[c]
                #We append the new element to the ciphered text
                cipheredtext=cipheredtext+b
    
        #If the element is not present in the alphabet, it is appended without changes to the ciphered text
        
            else: 
                cipheredtext=cipheredtext+ element
                #The function then returns the ciphered text
        print("This is the encrypted text: ", cipheredtext)
    except:
        print("Please enter an integer as the cipher key")
#decipher with right shift
"""We create a function Cipher to decrpyt data using a caesar cipher with a right shift, the function takes no arguments
It requires the user to enter the cipher key and the text to be encryted"""

def decipher():
    try:
        key=int(input('Enter the cipher key'))
        text=str(input('Enter the text to be deciphered')).lower()
    
        #We create an empty string decipheredtext to store the our ciphered text
        decipheredtext=str()
    
         # We use a for loop to iterate through the text 
        for element in text:
    
            """An if statement is used to check if an element is in the alphabet list if present we check the location of the element in the 
            alphabet list and store it in a variable, index"""
                       
            if element in alphabet:
                index=alphabet.index(element)
                """To determine the index of the ciphered element we take the modulus of the sum of the index (position of the element to be ciphered) 
                and the key, by the length of the alphabet."""
                c=(index+key)%len(alphabet)
                #we use the index c to identifiy the ciphered element and store it in a variable b
                b=alphabet[c]
                #We append the new element to the ciphered text
                decipheredtext=decipheredtext+b
    
                """ If the element is not present in the alphabet, it is appended without changes to the ciphered text
                The function then returns the ciphered text"""
            
            else: 
                decipheredtext=decipheredtext+ element
        print("This is the decrypted text: ", decipheredtext)    
    except:
        print("Please enter an integer as the cipher key")
    
    #create a variable action that stores the action the user would like to perform, encryption or decryption

action=input("What function would you like to perform? \n Encryption\n Decryption:").lower()
    # A switch case statement is implemented to provide the user with two options encryption and decryption
match action: 
    #if the user selects encryption then program runs the cipher function and encrypts the text
    case "encryption":
        cipher()
                
    # if the user selects decryption then the program runs the decipher function and decrypts the text
    case "decryption":
        decipher()
    
    
