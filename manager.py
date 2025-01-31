import os 
import text_byte_manager
import text_compile
import json

class Manager:
    def __init__(self):
        pass

    def compress_data(self, input_path, output_path):
        with open(input_path, "r", encoding="utf-8") as file:
            text = file.read()
        
        text_handler = text_compile.TextHandler(text)
        symbol_codec = text_handler.calculate_symbols()

        text_codec = text_handler.code_symbols(symbol_codec)

        text_copiler = text_compile.Text_Compiler(text)
        code_symbols_str, len_symbols_array = text_copiler.recompile_text(text_codec)

        text_byter = text_byte_manager.TextByter(code_symbols_str, len_symbols_array)
        prepare_len_data = text_byter.prepare_len_data()
        splitter_symbols = text_byter.symbols_splitter_to_bytes()

        compres_len, proc = text_byter.compress_len_data(prepare_len_data)
        byte_code_str = text_byter.code_compress_len_data(compres_len)

        if os.path.exists(output_path) == False:
            os.mkdir(output_path)

        text_byter.save_compress_len_data(byte_code_str, output_path)
        text_byter.save_symbols_splitter_bytes(splitter_symbols, output_path)

        with open(f"{output_path}/codec.json", "w") as file:
            json.dump(text_codec, file)


if __name__ == "__main__":
    Manager().compress_data("test.txt", "test_compress")