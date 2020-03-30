from itertools import *

print("Hello world!")

for i, num in enumerate(range(54,65)):
	print("Number {0} is {1}".format(i,num))

stupid=0
while(True):
	dogName = input("Who is the best dog?")
	if dogName=="Laika":
		print("That's right! Oogibooboo!")
		break
	else:
		stupid += 1
		print("Errr hello??! You've got it wrong {0} time{1}\nTry again...".format(stupid, "" if stupid==1 else "s, dummy"))
		
print("Line added as part of Git set-up & testing.")