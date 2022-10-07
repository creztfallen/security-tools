import random, string

size = int(input('Type the size for your pasword: '))
chars = string.ascii_letters + string.digits + "!çÇ@#$%&* -_.;:/?=+"

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size)))