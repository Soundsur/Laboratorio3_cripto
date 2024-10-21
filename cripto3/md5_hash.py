import hashlib

# Input string
input_string = "123456"

# Compute MD5 hash
md5_hash = hashlib.md5(input_string.encode()).hexdigest()

# Display the result
print(f"MD5 hash of '{input_string}' is: {md5_hash}")
