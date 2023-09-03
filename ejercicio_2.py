nombre = input("Ingrese Apellido y Nombre del Empleado: ")
ventas=int(input("ingrese las ventas del empleado: "))
sueldoBasico=80000
sueldoBruto = 0
comision=0

if ventas <= 10000:
    comision= 80000 * 0.05
    sueldoBruto= sueldoBasico + comision
elif ventas > 10000 and ventas <= 20000:
    comision= 80000 * 0.09
    sueldoBruto= sueldoBasico + comision
else:
    comision= 80000 * 0.15
    sueldoBruto= sueldoBasico + comision

print(nombre)    
print("Sueldo Basico: ", sueldoBasico)
print("Sueldo bruto: ", int(sueldoBruto))