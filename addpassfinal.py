from Crypto.Cipher import AES
import hashlib
import base64

input = open('/data/jmeter/key.txt','r')
key = input.readline().strip()
input.close()

def _pad(s):
    bs = AES.block_size
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)


def _generate_encrypt_key(key):
    n = len(key)
    if n == 0:
        return ''
    e = ''
    for i in range(0, n):
        f = key[i]
        g = ord(f)
        if f == '0':
            f = '9'
        h = g % int(f)
        if f == '1':
            h = g << 1
        if f == '2':
            h = g ^ 2
        x = g + h
        if x < 33:
            x = 33 + g % h
        if x > 126:
            x = 126 - g % h
        e += str(chr(x % 256))
    return hashlib.sha256(e.encode("utf-8")).hexdigest()[0:32]


def _passwd_encrypt(okey, passwd):
    key = _generate_encrypt_key(okey)
    iv = hashlib.sha256(key.encode('utf-8')).hexdigest()[0:16]
    AESCipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))

    cipher = AESCipher.encrypt(_pad(passwd).encode('utf-8'))
    cipher = base64.b64encode(cipher).decode('utf-8')
    return cipher
    
tempaddedpass = _passwd_encrypt(key, 'admin@1234')
addedpass = 'start' + tempaddedpass + 'end'
#print(key,addedpass)
#print(key,type(key))


output = open('/data/jmeter/pass.txt', 'w')
output.write(addedpass)
output.close()

