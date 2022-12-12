
import string



plaintext = input('Enter your text: ')



key = int(input('Enter the key: '))




def caesar(input_text, key):



 output_text = ""



 input_text = input_text.lower()


 for c in input_text:



        if c in string.ascii_letters:



            temp = ord(c) + key
           
        if temp > ord('z'):



               temp = temp - 26



              
        output_text = output_text + chr(temp)



 else: output_text = output_text + c



 return output_text



print(caesar(plaintext, key))