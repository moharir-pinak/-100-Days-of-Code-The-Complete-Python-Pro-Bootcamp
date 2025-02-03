# def encrypt (text,shift):
    
#     encoded = ""
    
#     for i in range(len(text)):
        
#         if text[i] in alphabet:
#             position = alphabet.index(text[i])
#             new_position = (position + shift) 
#             encoded += alphabet[new_position]
#         else:
#             encoded += text[i]
#     print (encoded)
# def decrypt (text,shift):
    
#     decoded = ""
    
#     for i in range(len(text)):
        
#         if text[i] in alphabet:
#             position = alphabet.index(text[i])
#             new_position = (position - shift) 
#             decoded += alphabet[new_position]
#         else:
#             decoded += text[i]
#     print(decoded)
import art
print (art.logo)
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
      shift_amount *= -1
    for letter in start_text:
      
        if letter not in alphabet:
            end_text += letter
        else:
      
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Should_continue = True
while Should_continue :
    direction = input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text , shift , direction)

    rerun = input ("If u want to encode or decode type Yes if not type No : \n").lower()

    if rerun == "No":
        Should_continue = False
        print ("Bye user")
    
        