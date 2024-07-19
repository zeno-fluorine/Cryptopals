""" The cryptopals crypto challenges
    Challenge 2: Fixed XOR"""
    
""" Write a function that takes two equal-length buffers and produces their XOR combination"""

""" If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

... should produce:
746865206b696420646f6e277420706c6179

"""    
def fun_xor():
    # Hex decode first string
    str_1 = "1c0111001f010100061a024b53535009181c"
    str_1 = bytes.fromhex(str_1)
    
    # Hex decode second string
    str_2 = "686974207468652062756c6c277320657965"
    str_2 = bytes.fromhex(str_2)
    
    # XOR the two strings
    str_xor = bytes([b1 ^ b2 for b1, b2 in zip(str_1, str_2)])
    """ Iterates over corresponding bytes in str_1 and str_2 XORing them together. 
    The result is collected into a list of bytes, which is then converted back into a 'bytes' object"""
    
    # Print the output
    print(str_xor)
    
fun_xor()

""" The result is:

the kid don't play"""