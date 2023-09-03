num=0
num_max=0
num_seg_max=0
pos_max=0
pos_seg=0
for x in range(0,10):
    if x == 0:
        num=int(input("ingrese 10 numeros en total: "))
        num_max=num
        pos_max= x + 1
    else:
        num=int(input("ingrese 10 numeros en total: "))
        if num > num_max:
            num_seg_max=num_max
            num_max=num
            pos_seg = pos_max
            pos_max= x + 1
        else: 
            if num > num_seg_max:
                num_seg_max = num
                pos_seg= x + 1

print("Numero maximo del conjunto es: ", num_max ," posicion: ", pos_max)
print("Numero secundario al maximo es: ", num_seg_max , "posicion: ", pos_seg)
