#una empresa telefonica cobra una tarifa de 20% por llamada mas lo que valga la llamada

monto_inicial = 1000
print(f"Tu monto es de: {monto_inicial}")

# cobro = int(input("costo de la llamada: "))
minutos = int(input("minutos de la llamada: "))
cobro = minutos * 100
recargo = cobro * .2
pago_total = cobro + recargo
monto_final = monto_inicial - pago_total

print(f'''\nCobro de llamada: {cobro}
recargo del 20%: {recargo}
El pago total es de: {pago_total}
''')
print(f"ahora tu monto es de: {monto_final}")