""" The cryptopals crypto challenges
Set 1 Challenge 3

Single-byte XOR cipher

The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

 You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

"""

"""
Achievement Unlocked

You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
"""

# The input is a hex-encoded string that represents an XOR-encrypted message
hex_encoded_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# Convert the hex-encoded string to a byte string for further processing
byte_string = bytes.fromhex(hex_encoded_string)

# Define a simple scoring function to measure how "English-like" a decrypted text is
# English letters, like 'E', 'T', 'A', 'O', 'I', 'N', etc., are more likely to appear in typical English text
english_characters = "ETAOIN SHRDLU"

# Scoring function that gives a higher score for characters frequently found in English text
def score_text(text):
    score = 0
    # Convert text to uppercase to make the comparison case-insensitive
    for char in text.upper():
        if char in english_characters:  # If the character is a common English letter
            score += 1  # Increase score for common English letters
    return score

# Initialize variables to track the best decryption attempt
best_score = -1  # Start with a very low score since we're looking for the highest score
best_decryption = None  # Variable to store the decrypted message with the best score
best_key = None  # Variable to store the XOR key that gives the best score

# Try all possible XOR keys (from 0 to 255) and attempt to decrypt the message
for i in range(256):
    # XOR each byte of the encrypted message with the current key (i)
    decrypted_text = bytes(a ^ i for a in byte_string).decode('latin1')  # Decode as 'latin1' to avoid errors with non-ASCII chars
    
    # Evaluate how "English-like" the decrypted text is by using the scoring function
    score = score_text(decrypted_text)
    
    # If the current decryption has a higher score than the previous best, update the best score and the corresponding values
    if score > best_score:
        best_score = score  # Update best score
        best_decryption = decrypted_text  # Store the decrypted text with the best score
        best_key = i  # Store the XOR key that gave the best score

# Output the best XOR key and the decrypted message that corresponds to it
print(f"Best key: {best_key}")  # Print the key that yielded the best decryption
print(f"Decrypted message: {best_decryption}")  # Print the decrypted message that has the highest English-likeness score

