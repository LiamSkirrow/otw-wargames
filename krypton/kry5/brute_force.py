import sys
import operator

# Brute force approach:
# - starting with 'aaaaaa' apply this key to decrypt the sample text, then perform the 
#   char counting logic below, if the order of the descending prevalence is ETAOI, then save the key to a list
# - increment the key to 'aaaaab' and rinse and repeat
# - every now and then print out the % complete, and also print out the current size of the potential key list
# - I actually don't think we'll get a very large list at the end:
#   - to get: ETAOINxxxx.... then the probability is: 20!/(26!*6) ~= 10^-9

MATCH_SLICE = 4

# this is a superset of what we want to generate
goal_alphabet = 'ETAOINSRHDLUCMFYWGPBVKXQJZ'
cipherKeyList = ['A', 'A', 'A', 'A', 'A', 'A']
IDX_TOP_CHAR = 5
count = 0
approx_complete = 0

file = input('Enter source filename: ')
pw_file = input('Enter pw filename: ')

# tally up the decrypted plaintext to determine whether the key is a potential match
def analyse_ciphertext(text):
    freq_list = []
    sorted_list_offsets = []
    freq_dict = {}
    for char in text:
        freq_dict[char] = line.count(char)
    freq_list.append(freq_dict)

    # sort the dicts based on value
    for freq_dict in freq_list:
        sorted_list = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True)
        sorted_list_offsets.append(sorted_list)

    return sorted_list_offsets[0, MATCH_SLICE].keys() == goal_alphabet[0, MATCH_SLICE]

# apply the key to the text, to decrypt the plaintext
def decrypt_ciphertext(text, cipherKeyList):
    ck_len = len(cipherKeyList)
    pt_len = len(text)

    plaintext = []

    for i in range(0, pt_len, ck_len):
        # grab a chunk of text
        text_slice = text[i, i+ck_len]
        # unrotate the text using the key
        for j in range(0, ck_len):
            diff = text_slice[j] - (cipherKeyList[j] - 65)
            if(diff < 0): # ascii/utf-8 -> A = 65
                # subtract a negative number, so add it
                diff = 91 + diff
            else:
                text_slice[j] = text_slice[j] - diff

            plaintext.append(text_slice[j])

    return plaintext

# apply cipherKeyList to passwd, using alphabet
def decrypt_ciphertext_pw(passwd, cipherKeyList):
    print(passwd)
    pass    


# TODO: can be made more efficient, since we don't need to store A's or Z's since they're implicit
# increment the 6 letter cipher key, recursively
def increment_key(ck, idx):
    # print('idx: ' + str(idx) + ', ck: ' + ''.join(ck))
    # char = ck[idx]
    if(ck[IDX_TOP_CHAR-idx] == 'Z'):
        if(idx == IDX_TOP_CHAR):
            print('End Reached!')
            return
        
        ck[IDX_TOP_CHAR-idx] = 'A'
        ck = increment_key(ck, idx+1)
    else:
        # increment by one ascii value
        ck[IDX_TOP_CHAR-idx] = chr(ord(ck[IDX_TOP_CHAR-idx]) + 1)
    
    return ck

with open(pw_file, 'r') as f:
    for line in f:
        passwd = line.replace(' ', '')
        print('Encrypted password: ' + line)

# generate monoalphabetic-ciphers 0-5
with open(file, 'r') as f:
    for line in f:
        line = line.replace(' ', '')
        print('Sample ciphertext:')
        print(line)

        passwd_list = []

        while(True):
            count += 1
            if(count % 3089158 == 0):
                approx_complete += 1
                print(str(approx_complete) + 'pc complete...')
            
            # we've reached the end
            if(cipherKeyList == ['Z', 'Z', 'Z', 'Z', 'Z', 'Z']):
                print(''.join(cipherKeyList))
                break

            # do frequency analysis on the ciphertext
            plaintext = decrypt_ciphertext(line, cipherKeyList)

            # analyse ciphertext to check if it matches MATCH_SLICE many chars in the goal_alphabet
            potential_match = analyse_ciphertext(plaintext)

            if(potential_match):
                # apply the current key to the encrypted passwd and store the resultant decrypted passwd
                decrypted_passwd = decrypt_ciphertext(passwd, cipherKeyList)
                print('Found potential plaintext password: ' + plaintext + 'associated with key: ' + ''.join(cipherKeyList) + ' after ' + count + ' many iterations')
                passwd_list.append(plaintext)

            # increment the key
            cipherKeyList = increment_key(cipherKeyList, 0)
    
    # TODO: don't forget to output passwd_list to a file

    f.close()
