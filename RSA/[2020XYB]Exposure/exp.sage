from Crypto.Util.number import *
import gmpy2


dp_high = 1153696846823715458342658568392537778171840014923745253759529432977932183322553944430236879985
c = 46735962204857190520476434898881001530665718155698898882603422023484998388668858692912250418134186095459060506275961050676051693220280588047233628259880712415593039977585805890920089318643002597837000049626154900908543384761210358835843974072960080857150727010985827690190496793207012355214605393036388807616 
e = 7621
n = 140376049134934822153964243403031201922239588054133319056483413311963385321279682186354948441840374124640187894619689719746347334298621083485494086361152915457458004998419817456902929318697902819798254427945343361548635794308362823239150919240307072688623000747781103375481834571274423004856276841225675241863
low_bits = 200
e_inv = inverse(e, n)
F.<x> = PolynomialRing(Zmod(n))
for k in range(1, e):
	# k = 1237
	f = (dp_high << low_bits) + x + (k - 1) * e_inv
	x0 = f.small_roots(X=2**low_bits, beta=0.44, epsilon=1/32)
	if len(x0) != 0:
		dp = Integer((dp_high << low_bits) + x0[0])
		p = (e * dp - 1 + k) // k
		if n % p == 0:
			q = n // p
			phi = (p - 1)*(q - 1)
			d = inverse(e, phi)
			m = pow(c, d, n)
			flag = long_to_bytes(m).decode("ISO-8859-1")
			if flag.startswith("flag"):
				print(flag)
				break