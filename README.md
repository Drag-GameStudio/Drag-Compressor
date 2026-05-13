
### 🚀 Powered by ADG System
The original version of this document offers a superior layout and faster navigation. 
**Check it out here:** [Full Documentation Interface](https://draggame-adg-frontend.hf.space/docs/adg_doc_58e6b88ce2dcf840fc2222c9e4e9ce99)
---

# Project Overview: Huffman-Based Text Compression System

## **Project Title**
Huffman-Based Text Compression and Decompression System

---

## **Project Goal**
The primary goal of this project is to provide an efficient, modular, and scalable system for compressing and decompressing text data using Huffman coding. By leveraging symbol frequency analysis, byte manipulation, and recursive compression techniques, the system significantly reduces the size of text files while preserving the original content. This solution is ideal for applications requiring optimized storage and transmission of textual data.

---

## **Core Logic & Principles**
The system is built around the Huffman coding algorithm, a widely-used method for lossless data compression. The architecture is modular, with distinct components handling specific tasks such as symbol encoding, byte-level operations, and recursive compression. The following principles define the core logic:

1. **Huffman Coding**:
   - The system uses the Huffman algorithm to assign shorter binary codes to more frequently occurring symbols in the text, thereby reducing the overall size of the encoded data.
   - A Huffman tree is constructed from character frequencies, and binary codes are generated for each character based on the tree structure.

2. **Modular Design**:
   - The system is divided into multiple Python modules, each responsible for a specific aspect of the compression and decompression process. This modularity ensures maintainability and scalability.

3. **Recursive Compression**:
   - The system supports recursive compression, where the already compressed binary data can be further compressed for additional size reduction.

4. **Byte-Level Operations**:
   - Specialized components handle the conversion of binary strings into byte-sized chunks and manage the storage of compressed data.

5. **Automation**:
   - Documentation generation is automated using GitHub Actions to ensure the project remains well-documented and up-to-date.

---

## **Key Features**
- **Huffman Encoding and Decoding**:
  - Efficiently compresses text data by assigning variable-length binary codes to characters based on their frequency.
  - Decodes compressed data back to its original form.

- **Recursive Compression**:
  - Supports multi-level compression for further size optimization.

- **Byte-Level Manipulation**:
  - Splits encoded symbols into byte-sized chunks for efficient storage.
  - Compresses and encodes length data into compact binary formats.

- **File Handling**:
  - Reads input text files, compresses them, and saves the compressed data and metadata to disk.
  - Handles binary and JSON files for decompression and text reconstruction.

- **Automated Documentation**:
  - Uses GitHub Actions to generate and maintain project documentation automatically.

- **Error Handling and Optimization**:
  - Basic error handling for file I/O and encoding/decoding mismatches.
  - Opportunities for optimization in recursive compression and logging.

---

## **Dependencies**
The following libraries and tools are required to run the project:

1. **Python**: The primary programming language used for the implementation.
2. **NumPy**: For efficient array manipulations in byte-level operations.
3. **GitHub Actions**: For automating documentation generation using the `autodoc.yml` workflow.
4. **External Workflow Repository**: Provides reusable workflows for the AutoDoc system.
5. **JSON**: For storing and retrieving symbol-to-code mappings during compression and decompression.

---

This Huffman-Based Text Compression and Decompression System is a robust and modular solution for reducing text file sizes while maintaining data integrity. Its recursive compression capability, byte-level operations, and automated documentation make it a versatile tool for developers and organizations seeking efficient data storage and transmission solutions.
## Executive Navigation Tree

### 📄 Core Engine
- [GitHub Workflow AutoDoc](#github-workflow-autodoc)
- [AutoDoc Config](#autodoc-config)

### 📂 Text Processing
- [Text Handler](#text-handler)
- [Calculate Symbols](#calculate-symbols)
- [Get Max Symbol](#get-max-symbol)
- [Get New Byte Code](#get-new-byte-code)
- [Code Symbols](#code-symbols)
- [Text Compiler](#text-compiler)
- [Code Text](#code-text)
- [Recompile Text](#recompile-text)
- [Compose Text](#compose-text)

### ⚙️ Bit Operations
- [BitsHandler](#bitshandler)
- [From Byte to Bit](#from-byte-to-bit)
- [Byte Reader](#byte-reader)
- [Read Bytes File](#read-bytes-file)
- [Symbols Splitter to Bytes](#symbols_splitter_to_bytes)
- [Save Symbols Splitter Bytes](#save_symbols_splitter_bytes)
- [TextByter Class](#textbyter-class)
- [Parse Int to 3Bit](#parse_int_to_3bit)

### 📦 Compression
- [Huffman Compression](#huffman-compression)
- [Code by Hoffman](#code_by_hoffman)
- [Compression Manager](#compression-manager)
- [Prepare Len Data](#prepare_len_data)
- [Normilize Len Data](#normilize-len-data)
- [Flatten](#flatten)
- [Compress Len Data](#compress_len_data)
- [Code Compress Len Data](#code_compress_len_data)
- [Save Compress Len Data](#save_compress_len_data)
- [Save Hoffman Compress Len Data](#save_hoffman_compress_len_data)
- [Decompress Len Data](#decompress-len-data)
- [Decompress Text Data](#decompress-text-data)
- [Get Keys by Value](#get-keys-by-value)
<a name="github-workflow-autodoc"></a>
## GitHub Workflow: AutoDoc Automation

### Functional Role
This workflow automates the generation of project documentation using GitHub Actions. It is triggered on pushes to the `main` branch or manually via the `workflow_dispatch` event.

### Key Logic Flow
1. **Trigger Events:**
   - Automatically runs when a commit is pushed to the `main` branch.
   - Can also be triggered manually via the GitHub Actions interface.

2. **Reusable Workflow:**
   - Leverages a reusable workflow from the repository `Drag-GameStudio/ADG` located at `.github/workflows/reuseble_agd.yml`.
   - This external workflow handles the actual documentation generation process.

3. **Authentication:**
   - Uses the `ADG_API_TOKEN` secret for authentication, ensuring secure access to external services or APIs.

### Inputs, Outputs, and Parameters
| Entity              | Type   | Role                                   | Notes                                      |
|---------------------|--------|----------------------------------------|-------------------------------------------|
| `push`              | Event  | Trigger for automatic execution        | Monitors changes to the `main` branch.    |
| `workflow_dispatch` | Event  | Manual trigger for the workflow        | Allows developers to run the workflow manually. |
| `ADG_API_TOKEN`     | Secret | Authentication for external services   | Must be configured in the repository secrets. |
| `reuseble_agd.yml`  | File   | Reusable workflow for documentation    | Located in the external repository.       |

> **Warning:** Ensure that the `ADG_API_TOKEN` secret is correctly configured in the repository to avoid authentication failures.

---
<a name="autodoc-config"></a>
## AutoDoc Configuration: `autodocconfig.yml`

### Functional Role
Defines the configuration for the AutoDoc system, specifying project metadata, ignored files, and documentation structure settings.

### Key Configuration Parameters
1. **Project Metadata:**
   - `project_name`: `"Project"` - The name of the project.
   - `language`: `"en"` - Documentation language.

2. **Ignored Files:**
   - Excludes Python bytecode, environment files, logs, databases, and version control directories from documentation generation.

3. **Build Settings:**
   - `save_logs`: `false` - Disables saving logs.
   - `log_level`: `2` - Sets the verbosity level for logs.

4. **Structure Settings:**
   - `include_intro_links`: `true` - Adds links to introductory sections.
   - `include_intro_text`: `true` - Includes introductory text in the documentation.
   - `include_order`: `true` - Maintains the order of sections in the documentation.

5. **Global File Usage:**
   - `use_global_file`: `true` - Enables the use of a global configuration file.
   - `max_doc_part_size`: `5000` - Limits the size of documentation parts.

### Inputs, Outputs, and Parameters
| Entity               | Type   | Role                                   | Notes                                      |
|----------------------|--------|----------------------------------------|-------------------------------------------|
| `project_name`       | String | Specifies the project name             | Used in generated documentation headers.  |
| `language`           | String | Sets the documentation language        | Default is English (`en`).                |
| `ignore_files`       | List   | Files/directories to exclude           | Includes temporary files, logs, and caches. |
| `save_logs`          | Bool   | Toggles log saving                     | If `true`, logs are saved.                |
| `log_level`          | Int    | Sets log verbosity                     | Higher values increase verbosity.         |
| `max_doc_part_size`  | Int    | Limits documentation part size         | Prevents overly large documentation files.|

> **Note:** Adjust the `ignore_files` list to include any additional files or directories specific to your project that should not be documented.

---
<a name="text-handler"></a>
## `TextHandler` Class: Symbol Frequency Analysis and Encoding

The `TextHandler` class is responsible for analyzing the frequency of symbols in the input text and generating a symbol-to-binary-code mapping for encoding purposes.

### Key Methods

####
<a name="calculate-symbols"></a> `calculate_symbols()`
Calculates the frequency of each symbol in the input text.

- **Logic:**
  - Iterates over each symbol in `self.text_data`.
  - Updates a dictionary `symbols_data` with the frequency count of each symbol.

- **Output:**
  - A dictionary where keys are symbols and values are their frequencies.

####
<a name="get-max-symbol"></a> `get_max_symbol(symbols_data)`
Finds the symbol with the highest frequency in the provided dictionary.

- **Logic:**
  - Iterates over the dictionary `symbols_data` to find the symbol with the maximum frequency.

- **Input:**
  - `symbols_data`: Dictionary of symbols and their frequencies.

- **Output:**
  - A tuple containing the symbol with the highest frequency and its count.

####
<a name="get-new-byte-code"></a> `get_new_byte_code(codec_level, old_byte_code=None)`
Generates a new binary code for a symbol based on the current codec level.

- **Logic:**
  - If `old_byte_code` is `None`, initializes a new binary code with all zeros of length `codec_level`.
  - Otherwise, increments the binary code by 1, handling carry-over.

- **Inputs:**
  - `codec_level`: Integer specifying the length of the binary code.
  - `old_byte_code`: (Optional) The previous binary code to increment.

- **Output:**
  - A new binary code as a string.

####
<a name="code-symbols"></a> `code_symbols(symbols_data)`
Generates a binary code for each symbol based on its frequency.

- **Logic:**
  - Sorts symbols by frequency in descending order.
  - Assigns binary codes based on the frequency rank, with shorter codes for more frequent symbols.

- **Input:**
  - `symbols_data`: Dictionary of symbols and their frequencies.

- **Output:**
  - A dictionary mapping symbols to their binary codes.

---
<a name="text-compiler"></a>
## `Text_Compiler` Class: Text Encoding and Recompilation

The `Text_Compiler` class encodes text data into binary strings using a symbol-to-binary-code mapping and manages the length of each encoded symbol.

### Key Methods

####
<a name="code-text"></a> `code_text(symbols_codec)`
Encodes the input text into a binary string and calculates the length of each encoded symbol.

- **Logic:**
  - Iterates over each symbol in `self.text_data`.
  - Appends the binary code for the symbol to `code_symbols_str`.
  - Records the length of each binary code in `len_symbols_array`.

- **Inputs:**
  - `symbols_codec`: Dictionary mapping symbols to binary codes.

- **Outputs:**
  - `code_symbols_str`: A binary string representing the encoded text.
  - `len_symbols_array`: A list of integers representing the length of each encoded symbol.

####
<a name="recompile-text"></a> `recompile_text(symbols_codec)`
Encodes the text and returns the binary string and symbol lengths.

- **Logic:**
  - Calls `code_text(symbols_codec)` to encode the text.

- **Input:**
  - `symbols_codec`: Dictionary mapping symbols to binary codes.

- **Outputs:**
  - `code_symbols_str`: A binary string representing the encoded text.
  - `len_symbols_array`: A list of integers representing the length of each encoded symbol.

---
<a name="compose-text"></a> `compose_text(text_array)`
Combines a list of symbols into a single text string.

- **Input:**
  - `text_array`: List of symbols.

- **Output:**
  - A string representing the reconstructed text.

---
<a name="bitshandler"></a>
## `Bitshandler` Class: Decompression and Text Reconstruction

The `Bitshandler` class handles bit-level operations for decompressing encoded text and reconstructing the original text.

### Key Methods

####
<a name="from-byte-to-bit"></a> `from_byte_to_bit(bytes_bcode)`
Converts a byte array into a list of 8-bit binary strings.

- **Input:**
  - `bytes_bcode`: A byte array.

- **Output:**
  - A list of 8-bit binary strings.

---

### Inputs, Outputs, and Parameters

| Entity               | Type        | Role                                   | Notes                                      |
|----------------------|-------------|----------------------------------------|-------------------------------------------|
| `text_data`          | String      | Input text data for encoding           | Used in `TextHandler` and `Text_Compiler`.|
| `symbols_data`       | Dictionary  | Symbol frequency data                  | Generated by `calculate_symbols`.         |
| `symbols_codec`      | Dictionary  | Symbol-to-binary-code mapping          | Generated by `code_symbols`.              |
| `main_text_bits`     | List        | Encoded text bits                      | Input for `Bitshandler`.                  |
| `len_data_bits`      | List        | Encoded length data bits               | Input for `Bitshandler`.                  |
| `codec_json`         | Dictionary  | Symbol-to-binary-code mapping          | Input for `Bitshandler`.                  |
| `input_path`         | String      | Directory containing input files       | Used in `ByteReader`.                     |

---

### Notes
- **Error Handling:**
  - The code lacks robust error handling for file I/O and input validation.
- **Optimization Opportunities:**
  - Refactor nested loops in `code_symbols` and `decompress_len_data` for improved performance.
  - Add logging and exception handling for better debugging.


It seems you haven't provided a specific request or input. Could you clarify what you'd like assistance with? For example, do you need documentation for a specific code fragment, an explanation of a component, or updates to the project profile? Let me know how I can help!
<a name="byte-reader"></a>
## `ByteReader` Class: File I/O and Byte-to-Bit Conversion

The `ByteReader` class handles reading binary and JSON files and converting bytes to bit arrays.

### Key Methods

####
<a name="read-bytes-file"></a> `read_bytes_file()`
Reads binary and JSON files from the specified input path.

- **Output:**
  - `main_text_byte`: Binary data for the main text.
  - `len_data_byte`: Binary data for symbol lengths.
  - `codec_json`: JSON data mapping symbols to binary codes.

####
<a name="symbols_splitter_to_bytes"></a> `symbols_splitter_to_bytes()`
Splits the binary string of encoded symbols (`code_symbols_str`) into byte-sized chunks (8 bits each).

- **Logic:**
  - Iterates through `code_symbols_str` and groups bits into chunks of 8.
  - Appends each chunk to a list and returns the list of byte-sized strings.

- **Output:**
  - A list of binary strings, each representing 8 bits.

---

####
<a name="save_symbols_splitter_bytes"></a> `save_symbols_splitter_bytes(splitter_symbols, save_path)`
Saves the byte-sized chunks of encoded symbols as a binary file.

- **Logic:**
  - Converts each binary string into a byte and writes it to a file named `main_text.bin`.
  
- **Output:**
  - A binary file containing the encoded symbols.

---

### Inputs, Outputs, and Parameters
| Entity               | Type        | Role                                   | Notes                                      |
|----------------------|-------------|----------------------------------------|-------------------------------------------|
| `code_symbols_str`   | String      | Encoded symbols as a binary string     | Input for `symbols_splitter_to_bytes`.    |
| `len_symbols_array`  | List        | Length data for symbols                | Input for length data preparation and compression. |
| `number`             | Integer     | Number to convert to 3-bit binary      | Input for `parse_int_to_3bit`.            |
| `compress_data`      | List        | Compressed length data                 | Input for `code_compress_len_data`.       |
| `save_path`          | String      | Directory for saving binary files      | Used in all save methods.                 |
| `hoffman_data`       | String      | Huffman-compressed length data         | Input for `save_hoffman_compress_len_data`. |
| `splitter_symbols`   | List        | Byte-sized chunks of encoded symbols   | Input for `save_symbols_splitter_bytes`.  |

---

### Notes
- **Error Handling:** Limited error handling is visible in the code. Potential issues include:
  - File I/O errors during save operations.
  - Incorrect input formats for binary string conversions.
- **Optimization Opportunities:**
  - Refactor nested loops in `prepare_len_data` and `compress_len_data` for better readability and performance.
  - Add validation for input data to prevent runtime errors.
- **Integration Points:**
  - Relies on `hofman_compress.huffman_encode` for Huffman encoding.
  - Outputs binary files (`len_data.bin`, `len_data_<padding>.bin`, `main_text.bin`) for use in other components.


markdown
<a name="textbyter-class"></a>
## Byte-Level Operations: `TextByter` Class in `text_byte_manager.py`

### Functional Role
The `TextByter` class is responsible for managing byte-level operations in the compression pipeline. It handles tasks such as splitting encoded symbols into byte-sized chunks, preparing and compressing length data, and saving compressed data to binary files. It also integrates with the Huffman encoding system for further compression.

---

### Class Attributes
| Attribute            | Type        | Role                                   | Notes                                      |
|----------------------|-------------|----------------------------------------|-------------------------------------------|
| `code_symbols_str`   | String      | Encoded symbols as a binary string     | Input for splitting into byte-sized chunks. |
| `len_symbols_array`  | List        | Length data for symbols                | Input for length data preparation and compression. |

---

### Key Methods and Logic

####
<a name="parse_int_to_3bit"></a> `parse_int_to_3bit(number)`
Converts an integer into a 3-bit binary string.

- **Logic:**
  - Subtracts 1 from the input number and formats it as a 3-bit binary string.
  
- **Output:**
  - A 3-bit binary string.

---

####
<a name="huffman-compression"></a>
## Huffman Compression: `hofman_compress.py`

### Functional Role
Implements Huffman encoding and decoding algorithms for compressing and decompressing data based on character frequencies.

### Key Functions and Logic
1. **Huffman Tree Construction:**
   - `huffman_tree(freqs)`: Builds a binary tree where each leaf node represents a character and its frequency.
   - Uses a priority queue (`heapq`) to iteratively combine the two least frequent nodes.

2. **Code Generation:**
   - `huffman_codes(tree, prefix)`: Recursively traverses the Huffman tree to generate binary codes for each character.

3. **Encoding:**
   - `huffman_encode(data)`: 
     - Computes character frequencies using `Counter`.
     - Builds a Huffman tree and generates codes.
     - Encodes the input data into a binary string.

4. **Decoding:**
   - `huffman_decode(encoded, codes)`:
     - Reverses the encoding process by mapping binary codes back to characters.
     - Iteratively matches binary substrings to decode the original data.

### Inputs, Outputs, and Parameters
| Entity               | Type        | Role                                   | Notes                                      |
|----------------------|-------------|----------------------------------------|-------------------------------------------|
| `freqs`              | Dict        | Character frequencies                  | Input for `huffman_tree`.                 |
| `tree`               | Node Object | Huffman tree                           | Output of `huffman_tree`.                 |
| `data`               | Iterable    | Input data to encode                   | Can be a string or list of characters.    |
| `encoded`            | String      | Huffman-encoded binary string          | Output of `huffman_encode`.               |
| `codes`              | Dict        | Mapping of characters to binary codes  | Output of `huffman_codes`.                |

> **Note:** The `Node` class is a custom `namedtuple` with attributes `char`, `freq`, `left`, and `right`.

---
<a name="code_by_hoffman"></a> `code_by_hoffman()`
Compresses the `len_symbols_array` using Huffman encoding.

- **Logic:**
  - Calls `hofman_compress.huffman_encode()` with `len_symbols_array` as input.
  - Returns the Huffman codec and compressed data.

- **Output:**
  - A dictionary mapping symbols to Huffman codes and the compressed data.

---

####
<a name="compression-manager"></a>
## Compression Manager: `manager.py`

### Functional Role
Orchestrates the compression process, including text handling, byte-level operations, and recursive compression.

### Key Methods and Logic
1. **Data Compression:**
   - `compress_data(text)`:
     - Creates a `TextHandler` to calculate symbol frequencies and generate codes.
     - Uses `Text_Compiler` to encode text and prepare symbol data.
     - Utilizes `TextByter` for byte-level operations, including preparing and compressing length data.

2. **Data Saving:**
   - `save_compress_data(output_path, ...)`:
     - Saves compressed data and metadata (e.g., binary files and codec JSON) to the specified output directory.

3. **Full Compression Workflow:**
   - `full_compress(input_path, output_path)`:
     - Reads text from a file, compresses it, and saves the output.

4. **Recursive Compression:**
   - `recursion_data_compress(file_path)`:
     - Reads binary data, decodes it to text, and recursively compresses it.

### Inputs, Outputs, and Parameters
| Entity               | Type        | Role                                   | Notes                                      |
|----------------------|-------------|----------------------------------------|-------------------------------------------|
| `text`               | String      | Input text for compression             | Used in `compress_data`.                  |
| `output_path`        | String      | Directory for saving compressed data   | Created if it does not exist.             |
| `file_path`          | String      | Path to binary file for recursive compression | Input for `recursion_data_compress`. |
| `text_codec`         | Dict        | Symbol-to-code mapping                 | Output of `compress_data`.                |
| `byte_code_str`      | String      | Compressed binary string               | Output of `compress_data`.                |
| `splitter_symbols`   | List        | Byte-sized chunks of encoded symbols   | Output of `compress_data`.                |

> **Warning:** Recursive compression removes the original binary file. Ensure backups are made if necessary.


markdown
<a name="prepare_len_data"></a> `prepare_len_data()`
Prepares the length data (`len_symbols_array`) for compression by grouping it into chunks of 4 and adding control codes (`-1` and `0`).

- **Logic:**
  - Iterates through `len_symbols_array` and groups elements into chunks of 4.
  - Adds control codes to indicate repeated or non-repeated values.
  
- **Output:**
  - A nested list where each sublist contains 4 elements.

---

####
<a name="normilize-len-data"></a> `normilize_len_data()`
Normalizes the length data bits into a structured array.

- **Logic:**
  - Splits each 8-bit segment of `self.len_data_bits` into two 4-bit codes.
  - Converts each 4-bit code into integers and adjusts for signed values.

- **Output:**
  - A list of structured arrays representing normalized length data.

####
<a name="flatten"></a> `flatten(array)`
Flattens a nested array into a single-level list.

- **Input:**
  - `array`: A nested list.

- **Output:**
  - A flat list containing all elements of the input array.

####
<a name="compress_len_data"></a> `compress_len_data(prepare_len_data)`
Further compresses the prepared length data into chunks of 4 elements, applying additional control codes.

- **Logic:**
  - Flattens the prepared length data.
  - Iterates through the flattened list and adds control codes for repeated values.
  
- **Output:**
  - A nested list of compressed data and the count of control codes (`-1`).

---

####
<a name="code_compress_len_data"></a> `code_compress_len_data(compress_data)`
Converts the compressed length data into binary strings.

- **Logic:**
  - Iterates through the compressed data and converts integers into binary strings.
  - Ensures that the total length of each binary string does not exceed 8 bits.
  
- **Output:**
  - A list of binary strings representing the compressed length data.

---

####
<a name="save_compress_len_data"></a> `save_compress_len_data(code_compress_data, save_path)`
Saves the compressed length data as a binary file.

- **Logic:**
  - Converts each binary string into a byte and writes it to a file named `len_data.bin`.
  
- **Output:**
  - A binary file containing the compressed length data.

---

####
<a name="save_hoffman_compress_len_data"></a> `save_hoffman_compress_len_data(hoffman_data, save_path)`
Saves Huffman-compressed length data as a binary file.

- **Logic:**
  - Groups the Huffman data into byte-sized chunks (8 bits each).
  - Pads the last chunk with zeros if necessary.
  - Writes the data to a file named `len_data_<padding>.bin`.
  
- **Output:**
  - A binary file containing the Huffman-compressed length data.

---

####
<a name="decompress-len-data"></a> `decompress_len_data(normilize_len_data_array)`
Decompresses the normalized length data into a flat list of symbol lengths.

- **Logic:**
  - Iterates over the normalized length data and reconstructs the original lengths.

- **Input:**
  - `normilize_len_data_array`: List of structured arrays from `normilize_len_data`.

- **Output:**
  - A list of integers representing the decompressed symbol lengths.

####
<a name="decompress-text-data"></a> `decompress_text_data(len_data)`
Decompresses the encoded text bits into symbols.

- **Logic:**
  - Flattens `self.main_text_bits`.
  - Iterates over `len_data` to extract binary codes of the specified lengths.
  - Maps each binary code to its corresponding symbol using `get_keys_by_value`.

- **Input:**
  - `len_data`: List of integers representing the lengths of encoded symbols.

- **Output:**
  - A list of symbols representing the decompressed text.

####
<a name="get-keys-by-value"></a> `get_keys_by_value(value)`
Finds the key in `self.codec_json` corresponding to a given binary code.

- **Input:**
  - `value`: A binary string representing a symbol's code.

- **Output:**
  - The symbol corresponding to the binary code.

####

    