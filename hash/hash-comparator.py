import hashlib

file1 = 'x.txt'
file2 = 'y.txt'

hash1 = hashlib.sha256()
hash1.update(open(file1, 'rb').read())

hash2 = hashlib.sha256()
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f"The file {file1} is different from the file {file2}.\n")
    print("The file1's hash is:" + hash1.hexdigest())
    print("\nThe file2's hash is:" + hash2.hexdigest())

else:
    print(f"The file: {file1} is equal to the file: {file2}")
    