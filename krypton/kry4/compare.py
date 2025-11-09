pw_key = 'KSVVWBGSJDSVSISVXBMNYQUUKBNWCUANMJS'

kry_freq = 'SQJUBNCGDZVWMYTXKELAFIOHRP'
eng_freq = 'ETAOINSRHDLUCMFYWGPBVKXQJZ'
#eng_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

#KSVVWBGSJDSVSISVXBMNYQUUKBNWCUANMJS
#WELLDONETHELEVELFOURPASSWORDIS

translate = {' ':' ', 'S':'E', 'Q':'A', 'J':'T', 'U':'S', 'B':'O', 'N':'R', 'C':'I', 'G':'N', 'D':'H','V':'L', 'W':'D', 'M':'U', 'Y':'P', \
             'T':'F', 'X':'F', 'K':'W', 'E':'G', 'L':'P', 'A':'B', 'F':'V', 'I':'K', 'O':'X', 'H':'Q', 'R':'J', 'P':'Z'}
#translate = {' ':' ', 'S':'E', 'Q':'T', 'J':'A', 'U':'O', 'B':'I', 'N':'N', 'C':'S', 'G':'H', 'D':'R'} \
        #'V':'L', 'I':'V'}

# KSVWBGDIXMNYQUCAJ

"""'Z':'D', 'V':'L', 'W':'C', 'M':'U', 'Y':'M', 'T':'W', 
'X':'F', 'K':'G', 'E':'Y', 'L':'P', 'A':'B', 'F':'V', 'I':'K', 'O':'J', 'H':'X', 'R':'Q', 'P':'Z'}"""

f = input('File: ')
file = open(f, 'r')

for line in file:
    print(line, end="")

#close(file)
file = open(f, 'r')

for line in file:
    for char in line:
        if char in translate:
            print(translate[char], end="")
        else:
            print('*', end="")

print()
