def decrypt_ciphertext(text, cipherKeyList):
    ck_len = len(cipherKeyList)
    pt_len = len(text)
    plaintext = []
    for i in range(0, pt_len, ck_len):
        # grab a chunk of text
        text_slice = text[i:(i+ck_len)]
        print('text_slice: ' + text_slice)
        # unrotate the text using the key
        for j in range(0, ck_len):
            diff = ord(text_slice[j]) - (ord(cipherKeyList[j]) - 65)
            if(diff < 65): # ascii/utf-8 -> A = 65
                # subtract a negative number, so add it
                diff = diff + 26
                # print('negative diff')
                char = chr(diff)
            else:
                char = chr(ord(text_slice[j]) - diff)
            plaintext.append(char)
            print('Decrypted char: ' + char +  ', diff: ' + str(diff))
        print()
        print('plaintext: ' + ''.join(plaintext))
    return plaintext

def open_files():
    f_encrypt = open('./eg_encrypt')
    f_key  = open('./eg_key')
    for key in f_key:
        print(key)
    for line in f_encrypt:
        print(line)
    f_encrypt.close()
    f_key.close()
