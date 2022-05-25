

def charstr_to_hexstr(txt):
    frag_txt = ""
    for char in txt:
        int_char = ord(char)
        hex_char = "0x{:02x}".format(int_char)
        frag_txt += f"{hex_char}"
    return frag_txt

def hexstr_to_charstr(txt):
    frag_txt = ""
    i = 0
    for char in txt.split("0x"):
        if i <= 0:
            i += 1
        else:
            int_char = int(char, 16)
            str_char = chr(int_char)
            frag_txt += str_char
    return frag_txt

if __name__ == '__main__':
    # Assuming these two lose no information between transactions and
    # their result for str<-->hex is equivalent
    key = "mylittlepony"
    hexkey = "0x6d0x790x6c0x690x740x740x6c0x650x700x6f0x6e0x79"
    
    print(f"Key: {key}")
    print(f"Hexkey: {hexkey}")

    x = charstr_to_hexstr(key)
    y = hexstr_to_charstr(x)
    
    print(f"charstr_to_hexstr: {x}")
    print(f"hexstr_to_charset: {y}")

    passed_tests = 0
    total_tests = 2
    if x == hexkey:
        passed_tests += 1
    if y == key:
        passed_tests += 1
    print(f"[*] Passed {passed_tests} out of {total_tests}.")
    if passed_tests == total_tests:
        print(f"[+] All tests passed successfully!")
