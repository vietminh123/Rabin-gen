import random
# Hàm tính a^m mod n
def powMod(a, k, n):
    result = 1
    a = a % n
    while k:
        if k & 1:
            result = (result * a) % n
        a = (a * a) % n
        k >>= 1
    return result
 
# Hàm kiểm tra a^m mod n có đồng dư với -1 hoặc 1 hay không
def Compute(a, n, k, m):
    mod = powMod(a, m, n)
    if mod == 1 or mod == n - 1:
        return True
    for _ in range (k - 1):
        mod = (mod * mod) % n
        if mod == n - 1:
            return True  
    return False
 
#Thuật toán Rabin Miller
def Miller_Rabin(n):
    if n == 2 or n == 3:
        return True
    if not(n & 1):
        return False
    k, m = 0, n - 1
    while not(m & 1):
        k += 1
        m >>= 1
    loop = 3
    for _ in range (loop):
        a = random.randint(2, n - 2)
        if not(Compute(a,n,k,m)):
            return False
    return True

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(e, phi_n):
    g, x, _ = extended_gcd(e, phi_n)
    if g != 1:
        raise Exception('Không thể tìm nghịch đảo modulo')
    else:
        return x % phi_n

def generateBigPrimeNumbers():
    big_number = int(1)
    for i in range (1,511):
        big_number += random.randint(0,1) * (1 << i)
    big_number += (2 ** 511)
    flag = False
    while not flag:
        if Miller_Rabin(big_number):
            flag = True
        else:
            big_number += 2
    return big_number

if __name__ == '__main__': 
    p = generateBigPrimeNumbers()
    q = generateBigPrimeNumbers()
    N = p*q
    phi_N = (p-1) * (q-1)
    random_bits = random.getrandbits(31)
    E = (1 << 32) | random_bits | 1
    flag = False;
    while True:
        if Miller_Rabin(E):
            flag = True;
        if flag:
            break;
        else:
            E += 2
    D = modinv(E,phi_N)
        
        
        
    
    
