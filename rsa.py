import congruenzelineari as cl


def findpub(N,fiN,numkeys):
	primekchiavi=[x for x in range(1,1000) if cl.Mcd(x,fiN) ==1 and cl.Mcd(x,N)==1]
	print('chiavi usabili (prime ',numkeys,')')
	return primekchiavi[1:numkeys]

def keys(e,fiN,N):
	couple=cl.trovasol(e,1,fiN)
	return [e,N], [couple[0],N]

def crypt(m,e):
	criptato=[]
	for x in range(len(m)):
		criptato.append(m[x]**e)
	return criptato

def decrypt(m,couple,N,e):
	criptato=crypt(m,e)
	for x in range(len(m)):
		print((criptato[x]**couple[0])%N)

def main():
	p=557 
	q=307
	N=p*q
	fiN=(p-1)*(q-1)
	e=31		#1<e<fiN tale che e e' primo con N
	m=[3,9,1,13]
	couple=cl.trovasol(e,1,fiN)
	print(findpub(N,fiN,100))
	print(keys(e,fiN,N))
	print(crypt(m,e))
	print(decrypt(m,couple,N,e))
	#decrypt(m,couple,N,e)


main()
