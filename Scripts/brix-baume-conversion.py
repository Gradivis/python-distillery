#Mum's Brix to Baume Converter with input
brix = int(input("Enter reading in brix: "))
baume = (brix + 1.6)/1.905
print(f"{brix}\u00b0 brix is {baume:.4}\u00b0 in baumé.")

if baume >= 10:
    print("These grapes are ready for harvest!")
else: 
    print("The baumé level is still to low for harvest.")