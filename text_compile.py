import json
import math
import numpy as np
import text_byte_manager


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

            
            



with open("test.txt", "r", encoding="utf-8") as file:
    text = file.read()

th = TextHandler(text)
sd = th.calculate_symbols()

text_codec = th.code_symbols(sd)
#print(text_codec)
tc = Text_Compiler(text)
code_symbols_str, len_symbols_array = tc.recompile_text(text_codec)

tb = text_byte_manager.TextByter(code_symbols_str, len_symbols_array)
prepare_len_data = tb.prepare_len_data()
print(len(prepare_len_data))

splitter_symbols = tb.symbols_splitter_to_bytes()
tb.save_symbols_splitter_bytes(splitter_symbols, "test_compress")
compres_len, proc = tb.compress_len_data(prepare_len_data)
byte_code_str = tb.code_compress_len_data(compres_len)
tb.save_compress_len_data(byte_code_str, "test_compress")