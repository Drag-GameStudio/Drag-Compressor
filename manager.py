import os 
import text_byte_manager
import text_compile
import json
import numpy as np



class Manager:
    def __init__(self):
        pass
    
    def compress_data(self, text):
        
        text_handler = text_compile.TextHandler(text)
        symbol_codec = text_handler.calculate_symbols()
        text_codec = text_handler.code_symbols(symbol_codec)

        text_copiler = text_compile.Text_Compiler(text)
        code_symbols_str, len_symbols_array = text_copiler.recompile_text(text_codec)
        text_byter = text_byte_manager.TextByter(code_symbols_str, len_symbols_array)
        #len_codec, hoffman_compress_data = text_byter.code_by_hoffman()
        #print(len(hoffman_compress_data) / 8)
        prepare_len_data = text_byter.prepare_len_data()
        splitter_symbols = text_byter.symbols_splitter_to_bytes()
        #print(len(prepare_len_data))
        #text_byter.save_hoffman_compress_len_data(hoffman_compress_data, "test_compress")
        compres_len, proc = text_byter.compress_len_data(prepare_len_data)
        byte_code_str = text_byter.code_compress_len_data(compres_len)


        return text_codec, text_byter, byte_code_str, splitter_symbols

    def save_compress_data(self, output_path, text_byter, byte_code_str, splitter_symbols, text_codec):
        if os.path.exists(output_path) == False:
            os.mkdir(output_path)

        text_byter.save_compress_len_data(byte_code_str, output_path)
        text_byter.save_symbols_splitter_bytes(splitter_symbols, output_path)

        with open(f"{output_path}/codec.json", "w", encoding='utf-8') as file:
            json.dump(text_codec, file, ensure_ascii=False)

    def full_compress(self, input_path, output_path):
        with open(input_path, "r", encoding="utf-8") as file:
            text = file.read()
        text_codec, text_byter, byte_code_str, splitter_symbols = self.compress_data(text)
        self.save_compress_data(output_path, text_byter, byte_code_str, splitter_symbols, text_codec)
        
    def recursion_data_compress(self, file_path):
        with open(file_path, "rb") as f:
            file_value = f.read()
        os.remove(file_path)

        output_path = file_path.split(".")[:-1][0]
        data_str = file_value.decode('ANSI')
        text_codec, text_byter, byte_code_str, splitter_symbols = self.compress_data(data_str)
        #print(text_codec)
        self.save_compress_data(output_path, text_byter, byte_code_str, splitter_symbols, text_codec)

if __name__ == "__main__":
    
    Manager().full_compress("test.txt", "test_compress") # 2 рекурсии
    #Manager().recursion_data_compress("test_compress/len_data/len_data/len_data.bin")
    #Manager().recursion_data_compress("test_compress/main_text.bin")