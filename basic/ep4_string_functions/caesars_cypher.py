# A - Z 65 - 90
# a - z 97 - 122
# ord(your_letter)
# chr(your_code)

# Use issuper() to decide which unicodes to work with
# Add the key(number of characters to shift) and if 
# the key is bigger or smaller then the unicode for 
# A, Z, a, z increase or decrease by 26

# receive the message to encrypt and the number of characters to shift
message = "hello"
key = 24

# prepare the secret_message
secret_message = ""

# cycle through each character in the message
for char in message: 
    # if it isn't a letter then keep it as it is 
    if char.isalpha():
    # get the character code and add the shift amount
        char_code = ord(char)
        char_code += key
    
        # if uppercase then compare to uppercase unicodes
        if char.isupper():
            # if bigger than Z subtract 26
            if char_code > ord("Z"):
                char_code -= 26

            # if smaller than A add 26
            if char_code < ord("A"):
                char_code += 26
                
        # Do the same for lowercase characters
        else:
            if char_code > ord("z"):
                char_code -= 26

            # if smaller than A add 26
            if char_code < ord("a"):
                char_code += 26

        # convert from code to letter and add to message
        secret_message += chr(char_code)
    else: 
    	secret_message += char

print("Encrypted: ", secret_message)

key = -key
orig_message = ""

for char in secret_message: 
    # if it isn't a letter then keep it as it is 
    if char.isalpha():
    # get the character code and add the shift amount
        char_code = ord(char)
        char_code += key
    
        # if uppercase then compare to uppercase unicodes
        if char.isupper():
            # if bigger than Z subtract 26
            if char_code > ord("Z"):
                char_code -= 26

            # if smaller than A add 26
            if char_code < ord("A"):
                char_code += 26
                
        # Do the same for lowercase characters
        else:
            if char_code > ord("z"):
                char_code -= 26

            # if smaller than A add 26
            if char_code < ord("a"):
                char_code += 26

        # convert from code to letter and add to message
        orig_message += chr(char_code)
    else: 
    	orig_message += char

print("Decrypted: ", orig_message)