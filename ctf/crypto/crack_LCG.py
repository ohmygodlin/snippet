'''
http://www.soreatu.com/ctf/writeups/Writeup%20for%20Crypto%20problems%20in%20NCTF%202019.html
https://zeroyu.xyz/2018/11/02/Cracking-LCG/
'''
# python2
import hashlib
import primefac
from pwn import *
from Crypto.Util.number import *

host, port = '139.129.76.65', 60001
r = remote(host, port)

context.log_level = 'debug'

def proof_of_work():
    print '[+] Proof of work...'
    r.recvuntil('hexdigest() = ')
    digest = r.recvline().strip()
    r.recvuntil("s[:7].encode('hex') =")
    prefix = r.recvline().strip().decode('hex')
    # s = r.recvline().strip()
    for suffix in range(256**3):
        guess = prefix + long_to_bytes(suffix, 3)
        if hashlib.sha256(guess).hexdigest() == digest:
            print '[+] find: ' + guess.encode('hex')
            break
    r.recvuntil("s.encode('hex') = ")
    # r.sendline(s)
    r.sendline(guess.encode('hex'))

def solve1(N, a, b, n1):
    return (n1 - b) * inverse(a, N) % N

def solve2(N, a, n1, n2):
    b = (n2 - n1 * a) % N
    return solve1(N, a, b, n1)

def solve3(N, n1, n2, n3):
    a = (n3 - n2) * inverse(n2 - n1, N) % N
    return solve2(N, a, n1, n2)

def solve4(n1, n2, n3, n4, n5, n6):
    t1 = n2 - n1
    t2 = n3 - n2
    t3 = n4 - n3
    t4 = n5 - n4
    t5 = n6 - n5
    N = GCD(t3*t1 - t2**2, t5*t2 - t4*t3)
    factors = primefac.factorint(N)
    while not isPrime(N):
        for prime, order in factors.items():
            if prime.bit_length() > 128:
                continue
            N = N / prime**order
    return solve3(N, n1, n2, n3)

def challenge1():
    print '[+] Solving challenge1...'
    r.recvuntil('lcg.N = ')
    N = int(r.recvline().strip())
    r.recvuntil('lcg.a = ')
    a = int(r.recvline().strip())
    r.recvuntil('lcg.b = ')
    b = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next1 = int(r.recvline().strip())

    init_seed = solve1(N, a, b, next1)
    r.recvuntil('lcg.seed = ')
    r.sendline(str(init_seed))

def challenge2():
    print '[+] Solving challenge2...'
    r.recvuntil('lcg.N = ')
    N = int(r.recvline().strip())
    r.recvuntil('lcg.a = ')
    a = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next1 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next2 = int(r.recvline().strip())

    init_seed = solve2(N, a, next1, next2)
    r.recvuntil('lcg.seed = ')
    r.sendline(str(init_seed))

def challenge3():
    print '[+] Solving challenge3...'
    r.recvuntil('lcg.N = ')
    N = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next1 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next2 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next3 = int(r.recvline().strip())

    init_seed = solve3(N, next1, next2, next3)
    r.recvuntil('lcg.seed = ')
    r.sendline(str(init_seed))

def challenge4():
    print '[+] Solving challenge4...'
    r.recvuntil('lcg.next() = ')
    next1 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next2 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next3 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next4 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next5 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next6 = int(r.recvline().strip())

    init_seed = solve4(next1, next2, next3, next4, next5, next6)
    r.recvuntil('lcg.seed = ')
    r.sendline(str(init_seed))

proof_of_work()

challenge1()
challenge2()
challenge3()
challenge4()

r.interactive()