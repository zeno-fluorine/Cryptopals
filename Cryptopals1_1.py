""" The cryptopals crypto challenges
    Challenge 1: Convert hex to base64"""
    
""" The String:
     49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
     
     Should produce:
     SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
     
     
     So go ahead and make that happen. You'll need to use this code for the rest of the exercies."""
     
     
""" Cryptopals Rule
    
    Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing."""
    
data_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print(type(data_hex))
    
print(bytes.fromhex(data_hex))