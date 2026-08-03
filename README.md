# XOR String Decoder

## Overview

The **XOR String Decoder** is a Python-based command-line tool that brute-forces all possible single-byte XOR keys (0–255) to recover readable strings from XOR-encoded files. It is designed as a beginner-friendly cybersecurity and malware analysis project, demonstrating techniques commonly used in reverse engineering and digital forensics.

The tool automatically ranks candidate keys based on the readability of the decoded strings, helping identify the most likely encryption key.

## Features

* Brute-forces all 256 possible single-byte XOR keys
* Extracts printable ASCII strings
* Automatically ranks the most likely XOR keys
* Displays the top decoding candidates
* Lightweight command-line application
* Useful for malware analysis and reverse engineering practice

## Technologies Used

* Python 3
* sys
* string

## How It Works

1. Load a binary file.
2. Apply every possible single-byte XOR key (0–255).
3. Search for printable ASCII strings.
4. Score each decoded result based on readability.
5. Display the highest-ranked candidate keys and recovered strings.

## Project Structure

```text
project/
│
├── xor_string_decoder.py
└── README.md
```

## How to Run

1. Clone this repository.

2. Navigate to the project directory.

3. Run the program:

```bash
python xor_string_decoder.py <filename>
```

Example:

```bash
python xor_string_decoder.py sample.bin
```

## Example Output

```text
[+] Loaded file: sample.bin
[+] Trying all 256 possible single-byte XOR keys...

=== RESULTS (best candidates first) ===

--- Candidate key: 55 (0x37) ---
Hello World
Password123
example.com

--- Candidate key: 91 (0x5B) ---
RandomText
LoginPage
```

## Learning Objectives

This project demonstrates:

* XOR encryption fundamentals
* Brute-force cryptanalysis
* Binary file processing
* ASCII string extraction
* Malware analysis basics
* Reverse engineering techniques
* Python file handling
* Command-line application development

## Use Cases

* Malware analysis
* Digital forensics
* Reverse engineering practice
* Capture The Flag (CTF) challenges
* Cybersecurity learning
* Binary data inspection

## Future Improvements

* Multi-byte XOR key detection
* Automatic key recovery
* Hex dump output
* Export recovered strings to a text file
* Support for UTF-8 and Unicode strings
* GUI version using Tkinter
* Entropy-based key ranking
* Support for multiple input files

## Disclaimer

This project is intended for educational purposes and cybersecurity training. It should only be used to analyze files that you own or have permission to inspect.

## Author

Developed as a cybersecurity project to explore XOR cryptography, malware analysis, reverse engineering, and binary file investigation using Python.
