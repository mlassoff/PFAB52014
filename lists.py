family = ['Mark', 'Brett', 'Joan' , 'Rick' , 'Rose', 'Kerri' ] 
age = [ 40, 36, 72, 66, 96, 41 ] 
gpas = [ 3.44, 2.7, 2.9, 3.2, 4.0, 3.98]

print family[0]
print family[2]
print family[4]
#print family[7]  Out of bounds list error causes fatal exit

total = gpas[0] + gpas[1] + gpas[2] +gpas[3] + gpas[4] + gpas[5]
print "The average is " , total / 6

print age
age[0] = 39
print age

print gpas
del gpas[1]
print gpas

family.append("Connor")
family.append("Colleen")
family.sort()
print family
print family[0]


