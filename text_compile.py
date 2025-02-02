import json
import math
import numpy as np
import text_byte_manager
from py_progress.progress import ProgressBar

class TextHandler:
    def __init__(self, text_data):
        self.text_data = text_data

    def calculate_symbols(self):
        symbols_data = {}
        for element_text in self.text_data:
            if symbols_data.get(element_text) is None:
                symbols_data[element_text] = 1
            else:
                symbols_data[element_text] += 1

        return symbols_data
    
    def get_max_symbol(self, symbols_data):
        max_value = ["", 0]
        for key in list(symbols_data.keys()):
            if max_value[1] < symbols_data[key]:
                max_value[0] = key
                max_value[1] = symbols_data[key]

        return max_value

    def get_new_byte_code(self, codec_level, old_byte_code = None):
        if old_byte_code is None:
            byte_code = ""
            for _ in range(codec_level):
                byte_code += "0"
            return byte_code
        
        
        new_code = []
        for el in old_byte_code:
            new_code.append(int(el))


        for i in range(codec_level):
            curr_index = codec_level - i - 1
            if new_code[curr_index] + 1 > 1:
                new_code[curr_index] = 0
            else:
                new_code[curr_index] += 1
                break
        
        new_str_code = ""
        for el in new_code:
            new_str_code += str(el)

        return new_str_code
            
    def code_symbols(self, symbols_data):
        new_codec = {}

        current_symbols_data: dict = symbols_data
        codec_level = 1
        under_codec_level = 2

        sym_codec = None

        for i in range(len(list(symbols_data.keys()))):
            if under_codec_level <= 0:
                codec_level += 1
                under_codec_level = math.pow(2, codec_level)
                sym_codec = None

            max_data = self.get_max_symbol(current_symbols_data)
            current_symbols_data.pop(max_data[0])
            under_codec_level -= 1
            
            sym_codec = self.get_new_byte_code(codec_level, sym_codec)
            new_codec[max_data[0]] = sym_codec

        return new_codec
            
class Text_Compiler:
    def __init__(self, text_data: str):
        self.text_data = text_data

    def code_text(self, symbols_codec):
        code_symbols_str = ""
        len_symbols_array = []
        for symbol_index in range(len(self.text_data)):
            code_symbol = symbols_codec[self.text_data[symbol_index]]
            len_symb = len(code_symbol)

            code_symbols_str += code_symbol
            len_symbols_array.append(len_symb)
        
        return code_symbols_str, len_symbols_array

    def recompile_text(self, symbols_codec):
        code_symbols_str, len_symbols_array = self.code_text(symbols_codec)

        return code_symbols_str, len_symbols_array


class Bitshandler:
    def __init__(self, main_text_bits, len_data_bits, codec_json):
        self.main_text_bits = main_text_bits
        self.len_data_bits = len_data_bits
        self.codec_json = codec_json

    def normilize_len_data(self):
        normilize_len_data_array = []
        for el in self.len_data_bits:
            first_code = int(el[:3], 2) + 1
            index_1_code = -int(el[3])

            second_code = int(el[4:7], 2) + 1
            index_2_code = -int(el[7])

            current_array = [first_code, index_1_code, second_code, index_2_code]
            normilize_len_data_array.append(current_array)

        return normilize_len_data_array

    def decompress_len_data(self, normilize_len_data_array):
        len_data = []
        for el in normilize_len_data_array:
            for child_el_i in range(len(el)):
                if el[child_el_i] == -1:
                    len_data.append(el[child_el_i - 1])
                else:
                    if el[child_el_i] != 0:
                        len_data.append(el[child_el_i])

        return len_data

    def flatten(self, array):
        flatten_array = []
        for i in range(len(array)):
            for j in range(len(array[i])):
                flatten_array.append(array[i][j])
        
        return flatten_array

    def get_keys_by_value(self, value):
        for key in list(self.codec_json.keys()):
            if self.codec_json[key] == value:
                return key

    def decompress_text_data(self, len_data):
        flatten_text_bits = self.flatten(self.main_text_bits)
        codes_text = []
        pb = ProgressBar(len(len_data))


        for curr_len in len_data:
            new_arr = flatten_text_bits[:curr_len]
            byte_code = ""
            for el in new_arr:
                byte_code += el

            codes_text.append(self.get_keys_by_value(byte_code))
            flatten_text_bits = flatten_text_bits[curr_len:]
            
            pb.progress_with_time(" ")

        return codes_text

    def compose_text(self, text_array):
        all_text = ""
        for el in text_array:
            all_text += str(el)
        
        return all_text

class ByteReader:
    def __init__(self, input_path):
        self.input_path = input_path

    def read_bytes_file(self):
        with open(f"{self.input_path}/main_text.bin", "rb") as f:
            main_text_byte = f.read()  

        with open(f"{self.input_path}/len_data.bin", "rb") as f:
            len_data_byte = f.read()

        with open(f"{self.input_path}/codec.json", "r", encoding="utf-8") as f:
            codec_json = json.load(f)
            
        return main_text_byte, len_data_byte, codec_json

    def from_byte_to_bit(self, bytes_bcode):
        bytes_array = list(bytes_bcode)
        bits_array = []

        for byte_element in bytes_array:
            bits_array.append(format(byte_element, "08b"))

        return bits_array


if __name__ == "__main__":
    br = ByteReader("test_compress")
    main_text_byte, len_data_byte, codec_json = br.read_bytes_file()

    main_text_bits = br.from_byte_to_bit(main_text_byte)
    len_data_bits = br.from_byte_to_bit(len_data_byte)

    bh = Bitshandler(main_text_bits, len_data_bits, codec_json)
    normilize_len_data_array = bh.normilize_len_data()
    len_data = bh.decompress_len_data(normilize_len_data_array)

    text_array = bh.decompress_text_data(len_data)
    print(bh.compose_text(text_array))



