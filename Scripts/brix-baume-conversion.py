#Mum's Brix to Baume Converter with input
def is_ripe(baume):
	'''
	This fucntion will parse the baume conversion 
	and determine whether grapes are right or not.
	INPUT: Baume Calculation
	'''
    if baume >= 10:
        print('Grapes are ready to pick!')
    elif baume < 10:
        print('Whoops, not ready to pick yet!')

print("Welcome to the Brix to Baumé converter.")
while True:      
    try:
        brix = float(input("Please enter the refractometer reading in brix: "))
        break    
    except ValueError:
        print("Please enter a number value!")

baume = (brix + 1.6)/1.905
print(f"{brix}\u00b0 brix is {baume:.4}\u00b0 in baumé.")
is_ripe(baume)


    