import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

uppercaseLetter1 = chr(random.randint(65,90))
uppercaseLetter2 = chr(random.randint(65,90))
uppercaseLetter3 = chr(random.randint(65,90))
lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))
lowercaseLetter3 = chr(random.randint(97,122))
digit1 = int(random.randint(0,9))
digit2 = int(random.randint(0,9))
punctuation1 = chr(random.randint(33,47))

password = uppercaseLetter1 + uppercaseLetter2+ uppercaseLetter3 +lowercaseLetter1 + lowercaseLetter2+ lowercaseLetter3 + str(digit1) + str(digit2) + punctuation1 

final_password = shuffle(password)  # Fixed: renamed from 'pass'

print(final_password)

