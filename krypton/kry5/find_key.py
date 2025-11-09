# we know that the key length is 6, so we can look at the 0, 6, 12... letter and 
# treat this as a monoalphabetic cipher. We can repeat this for all other offsets,
# doing frequency analysis for each of them independently to resolve the key...

import operator

file = input('Enter filename: ')
alphabet = 'ETAOINSRHDLUCMFYWGPBVKXQJZ'

### STEP 0: create raw output files accounting for offsets

# generate monoalphabetic-ciphers 0-5
with open(file, 'r') as f:
    for line in f:
        line = line.replace(' ', '')
        print(line)
        for offset in range (0, 6):
            output_file = open('raw_offset'+str(offset), 'w+')
            print('Offset: ' + str(offset)) 
            for i in range(offset, len(line), 6):
                #print(str(line[i])+' ', end="")
                output_file.write(line[i])
            print()

### STEP 1: obtain character count of raw text files

freq_list = []

for offset in range(0, 6):
    with open('raw_offset'+str(offset)) as f:
        for line in f:
            freq_dict = {}
            for char in line:
                freq_dict[char] = line.count(char)         
    freq_list.append(freq_dict)

### STEP 2: build alphabets for each offset file

sorted_list_offsets = []

# sort the dicts based on value
for freq_dict in freq_list:
    sorted_list = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_list_offsets.append(sorted_list)
    print('items: ' + str(sorted_list))

#print(sorted_list_offsets[0][0])

alpha_list = []

for l in sorted_list_offsets:
    alpha_dict = {}
    letter_offset = 0
    for elem in l:
        if(elem[0] not in [' ', '\n']):
            alpha_dict[elem[0]] = alphabet[letter_offset]
            #print(letter_offset)
            letter_offset += 1
    alpha_list.append(alpha_dict)

# debug print
print()
for d in alpha_list:
    print(d.keys())


freq_list_o0 = 'SIXMJEYWLPVRTHFQKAGNZCBODU'
freq_list_o1 = 'KVYODRNCSBXEZIFUGJMPWLTQAH'
freq_list_o2 = ''
freq_list_o3 = ''
freq_list_o4 = ''
freq_list_o5 = ''

# X next up is to write these offsetted strings to their own file
# - then need to do FA on each file individually, store these translation dicts{} in this file
# - using each of the six translation dicts, perform the 6 way interleaved translation on the krypton5 PW file

# - if the pw is still pretty jumbled, we can try and figure out the 'distance' from each jumbled char to the encrypted version
#   to derive a jumbled key, one that can possibly be easily visually corrected, allowing us to work backwards to get to the exact plaintext

