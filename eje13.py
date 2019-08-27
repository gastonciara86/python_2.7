name=raw_input("Nombre:")
age=int(raw_input("Edad:"))
if age>=5 and age<=10  or age>=65:
    boleto=80
    porcentaje_descuento=40
    valor_descuento=boleto*porcentaje_descuento/100
    importe_boleto=boleto-valor_descuento
    print "DESCUENTO DEL 40%"
    print "Nombre:",name,"|","Importe del Pasaje:",importe_boleto,"pesos|"
else :
    boleto=80
    print "Nombre:",name,"|","Importe del Pasaje:",boleto