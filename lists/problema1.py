n = int(input("ingresa cantidad: "))
lista = []
# par = []
# impar = []
# pos_par = []
# pos_impar = []

cont_par = 0 
cont_impar = 0
cont_p_par = 0 #p significa posicion
cont_p_impar = 0 

acum_par = 0
acum_impar = 0
acum_p_par = 0
acum_p_impar = 0

for i in range(0,n):
  x = int(input("ingresa un numero: "))
  lista.append(x)

  if x % 2 == 0:
    acum_par += x
    cont_par += 1
  else:
    acum_impar += x
    cont_impar += 1
  
for j in range(0,n):
  if j % 2 == 0:
    acum_p_par += lista[j]
    cont_p_par += 1
  else:
    acum_p_impar += lista[j]
    cont_p_impar += 1

prom_p_par = acum_p_par/cont_p_impar
prom_p_impar = acum_p_impar/cont_p_impar
if cont_par != 0:
  prom_par = acum_par/cont_par
  print("el promedio par",prom_par)
if cont_impar != 0:
  prom_impar = acum_impar/cont_impar
  print("el promedio impar",prom_impar)
print("el promedio position par",prom_p_par)
print("el promedio position impar",prom_p_impar)

print(lista)