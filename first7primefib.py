a=0
b=1
pcount=0
while (pcount<8):
	c=a+b
	a=b
	b=c
	pcheck=0
	for i in range (2,c):
		if c%i==0:
			pcheck=1
	if pcheck==0:
		print(c)
		pcount=pcount+1