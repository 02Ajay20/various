print('''Este programa determina el aumento de sueldo de un empleado.
teniendo en cuenta que a los empleados 1 y 2 se les aumenta un 5% y a los 3 y 4 el 12%
''')

employee = int(input("Elige uno de los empleados del 1 al 4: "))

if employee == 1:
  salary = 1000000
  increment = salary*0.05
  new_salary = increment + salary
  print(f"salario anterior: {salary}")
  print(f"el inclemento es: {increment}\nel nuevo sueldo es: {new_salary}")
elif employee == 2:
  salary = 1050000
  increment = salary*0.05
  new_salary = increment + salary
  print(f"salario anterior: {salary}")
  print(f"el inclemento es: {increment}\nel nuevo sueldo es: {new_salary}")
elif employee == 3:
  salary = 1102500
  increment = salary*0.12
  new_salary = increment + salary
  print(f"salario anterior: {salary}")
  print(f"el inclemento es: {increment}\nel nuevo sueldo es: {new_salary}")
elif employee == 4:
  salary = 1234800
  increment = salary*0.12
  new_salary = increment + salary
  print(f"salario anterior: {salary}")
  print(f"el inclemento es: {increment}\nel nuevo sueldo es: {new_salary}")