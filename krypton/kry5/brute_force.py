import sys

# Brute force approach:
# - starting with 'aaaaaa' apply this key to decrypt the sample text, then perform the 
#   char counting logic below, if the order of the descending prevalence is ETAOI, then save the key to a list
# - increment the key to 'aaaaab' and rinse and repeat
# - every now and then print out the % complete, and also print out the current size of the potential key list
# - I actually don't think we'll get a very large list at the end:
#   - to get: ETAOINxxxx.... then the probability is: 20!/(26!*6) ~= 10^-9


# this is a superset of what we want to generate
goal_alphabet = 'ETAOINSRHDLUCMFYWGPBVKXQJZ'
cipherKeyList = ['A', 'A', 'A', 'A', 'A', 'A']
IDX_TOP_CHAR = 5
count = 0
approx_complete = 0

file = input('Enter source filename: ')
pw_file = input('Enter pw filename: ')

def analyse_ciphertext(text):
    pass

    return [plaintext, matching_alphabet]

# apply cipherKeyList to passwd, using alphabet
def decrypt_ciphertext_pw(passwd, cipherKeyList, alphabet):
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
            derived_alphabet = analyse_ciphertext(line, cipherKeyList)

            # check if the derived_alphabet partially matches the goal_alphabet
            # if so, apply the current key to the encrypted passwd and store the resultant decrypted passwd
            [plaintext, matching_alphabet] = decrypt_ciphertext_pw(passwd, cipherKeyList, derived_alphabet)

            # push to the storage list
            if(matching_alphabet):
                print('Found potential plaintext password: ' + plaintext + 'associated with key: ' + ''.join(cipherKeyList))
                passwd_list.append(plaintext)

            # increment the key
            cipherKeyList = increment_key(cipherKeyList, 0)
    
    # TODO: don't forget to output passwd_list to a file

    f.close()