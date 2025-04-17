#Diego Rojas
#25/03/25
#que hago

pesos = int(input("Cuanto me queda en pesos colombianos?"))
soles = int(input("Cuanto me queda en pesos peruanos?"))
reales = int(input("Cuanto me queda en pesos brasil?"))

total = pesos * 0.00025 + soles * 0.28 + reales * 0.21
print(total)