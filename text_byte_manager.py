import numpy as np

class TextByter:
    def __init__(self, code_symbols_str, len_symbols_array):
        self.code_symbols_str = code_symbols_str
        self.len_symbols_array = len_symbols_array

    def symbols_splitter_to_bytes(self):
        splitter = []
        curr_splitter = []

        for curr_code in self.code_symbols_str:
            if len(curr_splitter) >= 8:
                curr_splitter_str = ""
                for el in curr_splitter:
                    curr_splitter_str += el

                splitter.append(curr_splitter_str)
                curr_splitter = []

            curr_splitter.append(curr_code)
        

        return splitter
    
    def parse_int_to_3bit(self, number):
        return format(number, '03b')
    
    def prepare_len_data(self):
        compress_array = [] #add -1, 0 4 len

        curr_compress = []

        for i in range(len(self.len_symbols_array)):
            if len(curr_compress) == 4:
                compress_array.append(curr_compress)
                curr_compress = []
            
            else:
                if i == len(self.len_symbols_array) - 1:
                    for j in range(4 - len(curr_compress)):
                        curr_compress.append(-2)
                    compress_array.append(curr_compress)
                    continue
                    

            if len(curr_compress) in (0, 2):
                curr_compress.append(self.len_symbols_array[i])
                continue
            
            if len(curr_compress)  in (1, 3):
                if i < len(self.len_symbols_array) - 1:
                    if curr_compress[0] == self.len_symbols_array[i + 1]:
                        curr_compress.append(-1)
                    else:
                        curr_compress.append(0)
                
                continue

        return compress_array

    def flatten(self, array):
        flatten_array = []
        for i in range(len(array)):
            for j in range(len(array[i])):
                flatten_array.append(array[i][j])
        
        return flatten_array

    def compress_len_data(self, prepare_len_data):
        flatten_prepare_len_data = self.flatten(prepare_len_data)

        compress_array = []
        curr_compress = []
        c_copress = 0

        offset = 0
        for i in range(len(flatten_prepare_len_data)):
            if i + offset < len(flatten_prepare_len_data):
                if len(curr_compress) >= 4:
                    compress_array.append(curr_compress)
                    curr_compress = []
                else:
                    if i + offset == len(flatten_prepare_len_data) - 1:
                        for j in range(3 - len(curr_compress)):
                            curr_compress.append(-2)
                        compress_array.append(curr_compress)


                if flatten_prepare_len_data[i + offset] == -1:
                    curr_compress.append(flatten_prepare_len_data[i + offset])
                    c_copress += 1
                    offset += 2
                    continue
                curr_compress.append(flatten_prepare_len_data[i + offset])
        
        return compress_array, c_copress
    
    def code_compress_len_data(self, compress_data):
        with_code = []
        for x in compress_data:
            new_data = []
            for i in range(len(x)):
                if i in (0, 2):
                    new_data.append(self.parse_int_to_3bit(x[i]))
                else:
                    if x[i] != -2:
                        new_data.append(-x[i])
                    else:
                        new_data.append(0)

            with_code.append(new_data)

        byte_code_str = []
        for el in with_code:
            full_byte = ""
            for i in range(len(el)):
                full_byte += str(el[i])

            byte_code_str.append(full_byte)

        return byte_code_str

    def save_compress_len_data(self, code_compress_data, save_path):
        all_bytes = b""
        for byte_str in code_compress_data:
            new_byte = bytes([int(byte_str, 2)])
            all_bytes += new_byte
        data = bytearray(all_bytes)
        with open(f"{save_path}/len_data.bin", "wb") as file:
            file.write(data)
        
    def save_symbols_splitter_bytes(self, splitter_symbols, save_path):
        all_bytes = b""
        for byte_symbol in splitter_symbols:
            new_byte = bytes([int(byte_symbol, 2)])
            all_bytes += new_byte
        data = bytearray(all_bytes)

        with open(f"{save_path}/main_text.bin", "wb") as file:
            file.write(data)






