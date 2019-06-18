def check(filename):
	a=b=c=d=0
	f=open(filename, "r")
	o= open("Output_file.txt","w+")
	if f.mode == 'r':
		contents =f.read()
		T = contents[0]
		l = len(contents)
		row = []
		for (i) in (range(l)):
			if(contents[i]==T):
				pass
			if (contents[i]=="A"):
				a=a+1
			if (contents[i]=="B"):
				b=b+1
			if (contents[i]=="."):
				c=c+1
			if (contents[i]=="\n") or (i==(l-1)):
				d=d+1
				if(d==1):
					pass
				else:
					if((b==0) or (c==0)):
						o.write("Case # %i : N" %(d-1))
						print("Case # %i : N" %(d-1))
						a=b=c=0
					elif(b>=c):
						o.write("Case # %i : Y" %(d-1))
						print("Case # %i : Y" %(d-1))
						a=b=c=0
					elif(b<c):
						o.write("Case # %i : N" %(d-1))
						print("Case # %i : N" %(d-1))
						a=b=c=0	

check("leapfrog_ch_.txt")



