""" The cryptopals crypto challenges
Set 1 Challenge 1

Convert hex to base64

The string:49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

"""

"""
Cryptopals Rule:
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
"""

import base64

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

byte_data = bytes.fromhex(hex_string) # Convert hex string to bytes
base64_string = base64.b64encode(byte_data).decode('utf-8') # Convert bytes to Base64

print(f"Base64: {base64_string}")
