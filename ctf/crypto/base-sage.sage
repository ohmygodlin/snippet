# solve equation, PolyRSA, CryptoCTF 2022, https://zhuanlan.zhihu.com/p/543950067
n = 44538727182858207226040251762322467288176239968967952269350336889655421753182750730773886813281253762528207970314694060562016861614492626112150259048393048617529867598499261392152098087985858905944606287003243

PR.<k> = PolynomialRing(ZZ)

p = k**6 + 7*k**4 - 40*k**3 + 12*k**2 - 114*k + 31377
q = k**5 - 8*k**4 + 19*k**3 - 313*k**2 - 14*k + 14011
n0 = p * q

f = n - n0
sol = f.roots()
x = sol[0][0]
p = p(x)
q = q(x)

# discrete_log
F.<a> = GF(2^13)
g = F.gen()
discrete_log_rho(g^1234, g)