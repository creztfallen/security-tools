import hashlib
string = input('Type the string to be hashed: \n')

menu = int(input('''### CHOOSE THE HASH ENCODING TYPE ###
             1.MD5
             2.SHA1
             3.SHA256
             4.SHA512
             
             Type the preferred hash number: '''))

if menu == 1:
    result = hashlib.md5(string.encode('utf-8'))
    print("The MD5 hashed string is :" + result.hexdigest())
elif menu == 2:
    result = hashlib.sha1(string.encode('utf-8'))
    print("The SHA1 hashed string is :" + result.hexdigest())    
elif menu == 3:
    result = hashlib.sha256(string.encode('utf-8'))
    print("The SHA256 hashed string is :" + result.hexdigest())   
elif menu == 4:
    result = hashlib.sha512(string.encode('utf-8'))
    print("The SHA512 hashed string is :" + result.hexdigest())       
    
    