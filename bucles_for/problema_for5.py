print("Este algoritmo muestra los digitos de la susecion de fibonacci")
user_num = int(input("Cuantos numeros desea digitar: "))
fibonacci1 = 1
fibonacci2 = 2
fibo_suma = 0

for i in range(1,user_num+1):
  print(fibonacci1)
  fibo_suma = fibonacci1 + fibonacci2

  fibonacci1 = fibonacci2
  fibonacci2 = fibo_suma