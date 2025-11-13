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
cipherKeyList = ['A', 'A', 'A']
IDX_TOP_CHAR = 2

file = input('Enter source filename: ')
pw_file = input('Enter pw filename: ')

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

# generate monoalphabetic-ciphers 0-5
with open(file, 'r') as f:
    for line in f:
        line = line.replace(' ', '')
        print('Sample ciphertext:')
        print(line)
        while(True):
        # for i in range(0, 100):
            print(''.join(cipherKeyList))
            cipherKeyList = increment_key(cipherKeyList, 0)

            # we've reached the end
            if(cipherKeyList == ['Z', 'Z', 'Z']):
                print(''.join(cipherKeyList))
                break
    f.close()