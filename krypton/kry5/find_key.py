# we know that the key length is 6, so we can look at the 0, 6, 12... letter and 
# treat this as a monoalphabetic cipher. We can repeat this for all other offsets,
# doing frequency analysis for each of them independently to resolve the key...

file = input('Enter filename: ')

# generate monoalphabetic-ciphers 0-5
with open(file, 'r') as f:
    for line in f:
        line = line.replace(' ', '')
        print(line)
        for offset in range (0, 6):
            print('Offset: ' + str(offset)) 
            for i in range(offset, len(line), 6):
                print(str(line[i])+' ', end="")
            print()
