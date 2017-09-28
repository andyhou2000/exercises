shares = 2000
shares = int(shares)

ppbuy = 40.00
ppbuy = float(ppbuy)

broker = 0.03
broker = float(broker)

ppsell = 42.75
ppsell = float(ppsell)

priceBuy = shares * ppbuy
priceBuy = float(priceBuy)

brokerBuyCom = (ppbuy * shares * broker)
brokerBuyCom = float(brokerBuyCom)

brokerSellCom = (ppsell * shares * broker)
brokerSellCom = float(brokerSellCom)

priceSell = shares * ppsell
priceSell = float(priceSell)

profit = priceSell - priceBuy - brokerBuyCom - brokerSellCom
profit = float(profit)

print("Joe paid $%.2f"%priceBuy, "for the stocks.")

print("Joe paid $%.2f"%brokerBuyCom, "in commission upon purchase.")

print("Joe sold the stocks for $%.2f"%priceSell, ".")

print("Joe paid $%.2f"%brokerSellCom, "in commission upon selling.")

print("Joe's total profit is: $%.2f"%profit, ".")