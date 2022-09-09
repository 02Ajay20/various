'''
a un trabajador se le pagan un sueldo y de ese sueldo se le restan seguro social, pension y ahorro
cuanto gana en total? eso es lo que resuelve este algoritmo
'''

pago = 1000000

seguro_social = pago/100*4
pension = pago/100*5
ahorro = pago/100*7

total = pago - seguro_social - pension - ahorro
print(f'''Descuento por seguro social: {seguro_social}
Descuento por pension: {pension}
Descuento por ahorro: {ahorro}\n
Pago total al trabajador: {total}''')