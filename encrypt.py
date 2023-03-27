alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(alfa, move):
    index = alphabet.index(alfa)
    newindex = index + move
    if newindex > len(alphabet)-1:
        newindex = newindex - (len(alphabet))
    newalfa = alphabet[newindex]
    return newalfa

if direction == 'encode':
    # array = text.split()
    newarr = []
    # print(array)
    for arr in text:
        i = encrypt(arr, shift)
        newarr.append(i)
    
    print("".join(newarr))
