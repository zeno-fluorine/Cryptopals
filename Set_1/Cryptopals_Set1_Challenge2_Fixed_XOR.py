""" The cryptopals crypto challenges
Set 1 Challenge 2

Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination

If your function works properly, then when you feed it the string

1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179

"""

import base64

def xor_hex_strings(hex_string_1, hex_string_2):
    # Convert hex strings to bytes
    byte_string_1 = bytes.fromhex(hex_string_1)
    byte_string_2 = bytes.fromhex(hex_string_2)

    # Perform XOR on the byte strings
    xor_result = bytes(a ^ b for a, b in zip(byte_string_1, byte_string_2))

    # Return the XOR result as a hexadecimal string
    return xor_result.hex()

# Problem usage:
string_1 = '1c0111001f010100061a024b53535009181c'
string_2 = '686974207468652062756c6c277320657965'

xor_result = xor_hex_strings(string_1, string_2)
print(xor_result)
            
