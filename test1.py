import random
# Hàm tính a^m mod n
def binPow(a, k, n):
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
    mod = binPow(a, m, n)
    if mod == 1 or mod == n - 1:
        return True
    for _ in range (k):
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
    k,m = 0, n - 1
    while not(m & 1):
        k+=1
        m >>= 1
    loop = 3
    for _ in range (loop):
        a = random.randint(2, n - 2)
        if not(Compute(a,n,k,m)):
            return False
    return True

def generateBigPrimeNumbers():
    big_number = int(1)
    for i in range (1,512):
        big_number += random.randint(0,1) * (1 << i)
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
    print(p)
    print(q)
    N = p*q
    phi_N = (p-1) * (q-1)
    E = 0
    for i in range(0,11):
        E += random.randint(0,9)*(10**i)
        flag = False;
        while not flag:
            if Miller_Rabin(E):
                flag =True
            else:
                E+=2;
    k = 1
    d = (k * phi_N + 1)/E
    while True:
        
        
    
    
