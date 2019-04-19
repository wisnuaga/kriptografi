def build_key_list(key):
    key = key.upper()
    key = key.replace("J", "I")
    key_list = " "
    for i in key:
        if i not in key_list:
            key_list += i
    key_list = key_list.replace(' ', '')
    return list(key_list)

def build_matrix_key(key):
    matrix_key = []
    key_list = build_key_list(key)
    alfabet = [chr(index) for index in range(65, 91)]
    alfabet.remove("J")
    merge_list = key_list

    #merge key and alphabet
    for i in range(25):
        if alfabet[i] not in key_list:
            merge_list.append(alfabet[i])

    #build matrix key
    i = 0
    for col in range(5):
        temp = []
        for row in range(5):
            temp.append(merge_list[i])
            i = i + 1
        matrix_key.append(temp)

    return matrix_key

def build_msg_list(msg):
    msg = msg.upper()
    msg = msg.replace("J", "I")
    msg = msg.replace(" ", "")
    list_msg = list(msg)

    i = 0
    while(i < len(list_msg)-1):
        if (list_msg[i] == list_msg[i + 1]):
            list_msg.insert(i + 1, "X")
        i = i + 2

    if (len(list_msg) % 2 == 1):
        list_msg.append("X")
    return list_msg

def find_msg_index(list_msg, matrix_key):
    list_msg = build_msg_list(list_msg)
    list_index = []

    for index in range(len(list_msg)):
        for col in range(5):
            for row in range(5):
                if(list_msg[index] == matrix_key[col][row]):
                    list_index.append([col, row])
    return list_index


def encrypt(msg, matrix_key):
    list_index = find_msg_index(msg, matrix_key)
    result = []

    for index in range(0, len(list_index)-1, 2):
        first_col = list_index[index][0]
        first_row = list_index[index][1]
        seccond_col = list_index[index+1][0]
        seccond_row = list_index[index+1][1]

        if(first_row == seccond_row):
            first_char = matrix_key[(first_col+1)%5][first_row]
            seccond_char = matrix_key[(seccond_col+1)%5][seccond_row]
        elif(first_col == seccond_col):
            first_char = matrix_key[first_col][(first_row+1)%5]
            seccond_char = matrix_key[seccond_col][(seccond_row+1)%5]
        else:
            first_char = matrix_key[first_col][seccond_row]
            seccond_char = matrix_key[seccond_col][first_row]

        result.append([first_char, seccond_char])

    return to_string(result)

def decrypt(msg, matrix_key):
    list_index = find_msg_index(msg, matrix_key)
    result = []

    for index in range(0, len(list_index) - 1, 2):
        first_col = list_index[index][0]
        first_row = list_index[index][1]
        seccond_col = list_index[index + 1][0]
        seccond_row = list_index[index + 1][1]

        if (first_row == seccond_row):
            first_char = matrix_key[(first_col - 1) % 5][first_row]
            seccond_char = matrix_key[(seccond_col - 1) % 5][seccond_row]
        elif (first_col == seccond_col):
            first_char = matrix_key[first_col][(first_row - 1) % 5]
            seccond_char = matrix_key[seccond_col][(seccond_row - 1) % 5]
        else:
            first_char = matrix_key[first_col][seccond_row]
            seccond_char = matrix_key[seccond_col][first_row]

        result.append([first_char, seccond_char])

    return to_string(result)

def to_list(text):
    temp = build_msg_list(text)
    list_text = []

    for index in range(0, len(temp)-1, 2):
        list_text.append([temp[index], temp[index+1]])
    return list_text

def to_string(list_text):
    str = ""
    for col in range(len(list_text)):
        for row in range(2):
            str += list_text[col][row]
    return str


msg = "bodo amat bozz"
key = "bangsat jahat"
matrix_key = build_matrix_key(key)

en_msg = encrypt(msg, matrix_key)
dn_msg = decrypt(en_msg, matrix_key)

print (msg)
print (en_msg)
print (dn_msg)


