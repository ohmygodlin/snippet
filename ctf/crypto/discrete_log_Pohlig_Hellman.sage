#Cantilever, CryptoCTF 2022, https://zhuanlan.zhihu.com/p/546270351
from tqdm import tqdm
from Crypto.Util.number import *

N = 7069789930583271525053215046247773438899869283661158227309691853515987055334306019600324056376312479212090202373516405860759222837585952590589336295698718699890424169542280710721069784487366121478569760563045886361884895363592898476736269784284754788133722060718026577238640218755539268465317292713320841554802703379684173485217045274942603346947299152498798736808975912326592689302969859834957202716983626393365387411319175917999258829839695189774082810459527737342402920881184864625678296442001837072332161966439361793009893108796934406114288057583563496587655548536011677451960307597573257032154009427010069578913
c = 109770827223661560471527567179288748906402603483328748683689436879660543465776899146036833470531024202351087008847594392666852763100570391337823820240726499421306887565697452868723849092658743267256316770223643723095601213088336064635680075206929620159782416078143076506249031972043819429093074684182845530529249907297736582589125917235222921623698038868900282049587768700860009877737045693722732170123306528145661683416808514556360429554775212088169626620488741903267154641722293484797745665402402381445609873333905772582972140944493849645600529147490903067975300304532955461710562911203871840101407995813072692212
e = 65537

def pollard_pm1(N,B=0):
    if not B: B=ceil(sqrt(N))
    a = Integers(N).random_element()
    b = a
    for ell in tqdm(list(primes(B))):
        q = 1
        while q < N:
            q *= ell
        b = b^q
        if b == 1:
            return 0
        d = gcd(b.lift()-1,N)
        if d > 1: return d
    return 0

p = pollard_pm1(N, B=2^19)

q = N // p
Zp, Zq = Zmod(p), Zmod(q)
m_2p = discrete_log(Zp(c), Zp(e))
m_2q = discrete_log(Zq(c), Zq(e))
m_2 = crt([m_2p, m_2q], [p-1, q-1])
print(long_to_bytes(m_2))
