from sys import argv

file1=open(argv[1])
file2=open(argv[2])

lines1=file1.read()
lines2=file2.read()

sol1=list(map(lambda x:round(float(x), 3), filter(None, lines1.split())))
sol2=list(map(lambda x:round(float(x), 3), filter(None, lines2.split())))

if len(sol1)!=len(sol2):
	print('Number of lines mismatch. Found {} numbers in {} and {} numbers in {}'.format(len(sol1), argv[1], len(sol2), argv[2]))
	exit(1)

flag=False
for i in range(len(sol1)):
	if sol1[i]!=sol2[i]:
		print('Mismatch of {} at line {}:'.format('values' if i%2==0 else 'actions', i//2))
		print('in {} = {} , in {} = {}'.format(argv[1], sol1[i], argv[2], sol2[i]))
		flag=True
