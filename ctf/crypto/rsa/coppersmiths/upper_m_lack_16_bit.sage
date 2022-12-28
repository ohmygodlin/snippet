# f(x) = (mbar + x)^e - c (mod n)
# digits_missing,zongheng-2020, https://cloud.tencent.com/developer/article/1769199
import itertools

c = 62660062196860780748321891664224323210733407658954868754136813454276197326286989854755063135388270492115677534757771740441654605013455630509082901831383997174837303122307903048769036933981340466294080355175644010962515708905474510644455088727239628649170131534290730571906687613233026401827836518586465485444
n = 66442292138939994008585245717226499074430780356754301428786129627761199772080656972422189200687286655989342990033892222751162330429917160211076751202919221105000510408340684982768002644852287260860136071476247209262934997138516620028486517153019554511944103340884841254678682058936833441307291121560050184387
e = 5

b = 616839734200836264550000489233743369720556625384140795196598199604218412320838747477456532070489540436552579943450439963101783440564923982484679616225987
a = 3762025631478473827
cc = 7148116837567849778
mprefix = (a << (512 + 8 * 8)) + (b << (8*8)) + cc
mprefix = hex(mprefix)

hexdigit = '0123456789abcdef'
#hexdigit = map(hex, map(ord, hexdigit))

unknown = 4
kbits = (32 - unknown) * 4
#unknown = 2
#kbits = (16 - unknown) * 8
PR.<x> = PolynomialRing(Zmod(n))
for i in itertools.product(hexdigit, repeat = unknown):
    mbar = int(mprefix + ''.join(i), 16)
    #mbar = int(mprefix + i[2:] + j[2:], 16)
    mbar = mbar << kbits
    f = (mbar + x)^e - c
    roots = f.small_roots(X=2**kbits, beta=1)
    if roots:
        x0 = roots[0]
        m = x0 + mbar
        print(hex(m))

