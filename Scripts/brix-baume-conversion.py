#Mum's Brix to Baume Converter with input
print("Welcome to the Brix to Baumé converter.")
while True:      
    try:
        brix = float(input("Please enter the refractometer reading in brix: "))
        break    
    except ValueError:
        print("Please enter a number value!")

baume = (brix + 1.6)/1.905
print(f"{brix}\u00b0 brix is {baume:.4}\u00b0 in baumé.")

if baume >= 10:
    print("These grapes are ready for harvest!")    
else: 
    print("The baumé level is still too low for harvest.")