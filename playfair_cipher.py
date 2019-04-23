class Playfair:
    __removed_char = 'J'
    __subs_char = 'I'
    __additional_char = 'X'

    def __init__(self, message, key):
        self.message = message.upper()
        self.key = key.upper()
        self.msg_list = self.__build_msg_list()
        self.key_list = self.__build_key_list()
        self.alfabet_list = self.__build_alfabet_list()
        self.matrix_key = self.__build_matrix_key()
        self.msg_index = self.__build_index(self.msg_list)

    def __build_key_list(self):
        key = self.key.replace(self.__removed_char, self.__subs_char)
        temp = ""
        for i in key:
            if i not in temp:
                temp += i
        temp = temp.replace(' ', '')
        return list(temp)

    def __build_alfabet_list(self):
        alfabet = [chr(index) for index in range(65, 91)]
        alfabet.remove(self.__removed_char)
        return alfabet

    def __build_matrix_key(self):
        matrix_key = []
        merge_list = self.__build_key_list()

        # merge key and alphabet
        for i in range(25):
            if self.alfabet_list[i] not in self.key_list:
                merge_list.append(self.alfabet_list[i])

        # build matrix key
        i = 0
        for y in range(5):
            temp = []
            for x in range(5):
                temp.append(merge_list[i])
                i = i + 1
            matrix_key.append(temp)

        return matrix_key

    def __build_msg_list(self):
        msg = self.message.replace(self.__removed_char, self.__subs_char)
        msg = msg.replace(' ', '')
        list_msg = list(msg)

        i = 0
        while (i < len(list_msg) - 1):
            if (list_msg[i] == list_msg[i + 1]):
                list_msg.insert(i + 1, "X")
            i = i + 2

        if (len(list_msg) % 2 == 1):
            list_msg.append("X")
        return list_msg

    def __build_msg_index(self):
        return self.__build_index(self.msg_list)

    def __build_index(self, msg):
        list_index = []
        for i in range(len(msg)):
            for y in range(5):
                for x in range(5):
                    if (msg[i] == self.matrix_key[y][x]):
                        list_index.append([y, x])
        return list_index

    @staticmethod
    def to_list(text):
        temp = build_msg_list(text)
        list_text = []

        for index in range(0, len(temp) - 1, 2):
            list_text.append([temp[index], temp[index + 1]])
        return list_text

    @staticmethod
    def to_string(list_text):
        str = ""
        for col in range(len(list_text)):
            for row in range(2):
                str += list_text[col][row]
        return str

    def encrypt(self):
        e_msg = []

        for i in range(0, len(self.msg_index) - 1, 2):
            first_col = self.msg_index[i][0]
            first_row = self.msg_index[i][1]
            seccond_col = self.msg_index[i + 1][0]
            seccond_row = self.msg_index[i + 1][1]

            if (first_row == seccond_row):
                first_char = self.matrix_key[(first_col + 1) % 5][first_row]
                seccond_char = self.matrix_key[(seccond_col + 1) % 5][seccond_row]
            elif (first_col == seccond_col):
                first_char = self.matrix_key[first_col][(first_row + 1) % 5]
                seccond_char = self.matrix_key[seccond_col][(seccond_row + 1) % 5]
            else:
                first_char = self.matrix_key[first_col][seccond_row]
                seccond_char = self.matrix_key[seccond_col][first_row]

            e_msg.append([first_char, seccond_char])

        return self.to_string(e_msg)
    
    def decrypt(self):
        e_msg = self.encrypt()
        e_msg_index = self.__build_index(e_msg)
        d_msg = []

        for i in range(0, len(e_msg_index) - 1, 2):
            first_col = e_msg_index[i][0]
            first_row = e_msg_index[i][1]
            seccond_col = e_msg_index[i + 1][0]
            seccond_row = e_msg_index[i + 1][1]

            if (first_row == seccond_row):
                first_char = self.matrix_key[(first_col - 1) % 5][first_row]
                seccond_char = self.matrix_key[(seccond_col - 1) % 5][seccond_row]
            elif (first_col == seccond_col):
                first_char = self.matrix_key[first_col][(first_row - 1) % 5]
                seccond_char = self.matrix_key[seccond_col][(seccond_row - 1) % 5]
            else:
                first_char = self.matrix_key[first_col][seccond_row]
                seccond_char = self.matrix_key[seccond_col][first_row]

            d_msg.append([first_char, seccond_char])

        return self.to_string(d_msg)


msg = "Umumkan Hasil Pemilu Besok Pagi"
key = "Hutan Borneo"
pf = Playfair(msg, key)

print ("Pesan : " + pf.message)
print ("Kunci : " + pf.key)
print ("======================================")
print ("Encrypt : " + pf.encrypt())
print ("Decrypt : " + pf.decrypt())