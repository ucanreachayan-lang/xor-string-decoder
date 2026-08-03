import sys
import string

MIN_STRING_LENGTH = 6

PRINTABLE = set(bytes(string.printable, "ascii"))

def xor_decode(data: bytes, key: int) -> bytes:    
    return bytes(b ^ key for b in data)

def find_printable_runs(data: bytes, min_len: int = MIN_STRING_LENGTH):   
    found = []
    current = bytearray()
    for byte in data:
        if byte in PRINTABLE:
            current.append(byte)
        else:
            if len(current) >= min_len:
                found.append(current.decode("ascii", errors="ignore"))
            current = bytearray()

    if len(current) >= min_len:
        found.append(current.decode("ascii", errors="ignore"))
    return found

def brute_force_xor(filepath: str):
    with open(filepath, "rb") as f:
        data = f.read()
    print(f"[+] Loaded file: {filepath} ({len(data)} bytes)")
    print(f"[+] Trying all 256 possible single-byte XOR keys...\n")
    results_by_key = {}

    for key in range(256):
        decoded = xor_decode(data, key)
        strings_found = find_printable_runs(decoded)

        if strings_found:
            results_by_key[key] = strings_found

    if not results_by_key:
        print("[-] No readable strings found with any single-byte XOR key.")
        return

    def score(strings_found):
        total = 0
        for s in strings_found:
            letters = sum(1 for c in s if c.isalpha())
            total += letters * len(s)
        return total

    ranked = sorted(results_by_key.items(), key=lambda kv: score(kv[1]), reverse=True)
    print("=== RESULTS (best candidates first) ===\n")
    for key, strings_found in ranked[:5]:   
        print(f"--- Candidate key: {key} (0x{key:02x}) ---")
        for s in strings_found:
            print(f"    {s}")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 xor_string_decoder.py <filename>")
        sys.exit(1)
        
    brute_force_xor(sys.argv[1])