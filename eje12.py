Name=raw_input("Nombre:")
Carrera=raw_input("Carrera:")
City=raw_input ("Ciudad:")
if Carrera=="electromecanica" and City!="rio cuarto" :
    Cuota=2000
    porcentaje_descuento=15
    valor_descuento=Cuota*porcentaje_descuento/100
    importe_pagar=Cuota-valor_descuento
    print "|Obtiene Un Descuento Del 15%|"
    print "|Nombre:",Name , "|Carrera:",Carrera , "|Ciudad:",City, "|Importe a Pagar:",importe_pagar,"|"
else :
    Cuota=2000
    print "|Nombre:",Name, "|Carrera:",Carrera, "|Cudad:",City, "|Importe a Pagar:",Cuota,"|"