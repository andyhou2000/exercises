sugar = 1.5
sugar = float(sugar)

butter = 1.0
butter = float(butter)

flour = 2.75
flour = float(flour)

cookies = input("How many cookies: ")
cookies = int(cookies)

sugarNeeded = sugar * cookies / 48
sugarNeeded = float(sugarNeeded)

butterNeeded = butter * cookies / 48
butterNeeded = float(butterNeeded)

flourNeeded = flour * cookies / 48
flourNeeded = float(flourNeeded)

print("Sugar needed: %.4f"%sugarNeeded, "cups")
print("Butter needed: %.4f"%butterNeeded, "cups")
print("Flour needed: %.4f"%flourNeeded, "cups")