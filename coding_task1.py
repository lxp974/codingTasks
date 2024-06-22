import pandas as pd
import numpy as np

# import text file
message_file = pd.read_csv('coding_qual_input.txt', sep=' ', header=None) #, names=['num','word']

# num = message_file.iloc[:,0]
# word = message_file.iloc[:,1]
# print(num)
# print(word)

# decoding function
def decode(message_file):

    tri = []
    sentence = []

    # approx number of rows for triangle numbers
    rows = round(np.sqrt(2*max(message_file.iloc[:,0])))

    # triangle numbers
    for i in range (1, rows+1):
        triangle_num = (i ** 2 + i)//2
        tri.append(triangle_num)

        # loop to compare triangle numbers with number in text file
        for k in tri: 
            for j in message_file.iloc[:,0]:
               # If numbers match, return word 
               if k == j:
                    # print (f'number {j} with triangle num {k} corresponds to {message_file.iloc[j-1,1]}')
                    found_word = message_file.iloc[j-1,1]
                    # Store result
                    if found_word not in sentence:
                        sentence.append(message_file.iloc[j-1,1])
    # print(tri)
    decoded = ' '.join(sentence)
    print (decoded)
    return decoded

decode(message_file)



