#babyRSA, NCTF-2019, https://blog.soreatu.com/posts/intended-solution-to-crypto-problems-in-nctf-2019/

from Crypto.Util.number import *
import gmpy2

e = 65537
d = 19275778946037899718035455438175509175723911466127462154506916564101519923603308900331427601983476886255849200332374081996442976307058597390881168155862238533018621944733299208108185814179466844504468163200369996564265921022888670062554504758512453217434777820468049494313818291727050400752551716550403647148197148884408264686846693842118387217753516963449753809860354047619256787869400297858568139700396567519469825398575103885487624463424429913017729585620877168171603444111464692841379661112075123399343270610272287865200880398193573260848268633461983435015031227070217852728240847398084414687146397303110709214913
c = 5382723168073828110696168558294206681757991149022777821127563301413483223874527233300721180839298617076705685041174247415826157096583055069337393987892262764211225227035880754417457056723909135525244957935906902665679777101130111392780237502928656225705262431431953003520093932924375902111280077255205118217436744112064069429678632923259898627997145803892753989255615273140300021040654505901442787810653626524305706316663169341797205752938755590056568986738227803487467274114398257187962140796551136220532809687606867385639367743705527511680719955380746377631156468689844150878381460560990755652899449340045313521804
kphi = e*d - 1

for k in range(1, e):
    if kphi % k == 0:
        phi = kphi // k
        root = gmpy2.iroot(phi, 2)[0]
        for p in range(root - 2000, root + 2000):
            if phi % (p-1) == 0: break
        else: continue
        break

q = phi//(p-1) + 1
m = pow(c, d, p*q)
print(long_to_bytes(m))

# 'NCTF{70u2_nn47h_14_v3ry_gOO0000000d}'