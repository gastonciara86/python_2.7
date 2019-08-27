dayNoWork=int(raw_input("Dias No Trabajados:"))
age=int(raw_input("Anio de Ingreso:"))
agelabor=2000
if dayNoWork==0 :
    sueldo=3000
    porcentaje=30
    porcentaje_incremento=sueldo*porcentaje/100
    incremento_sueldo=sueldo+porcentaje_incremento
    print "Aumento de 30% por no Faltar"
    print "sueldo:",incremento_sueldo,"pesos"
elif age-agelabor>=5 :
    sueldo=3000
    porcentaje=30
    porcentaje_incremento=sueldo*porcentaje/100
    incremento_sueldo=sueldo+porcentaje_incremento
    print "Aumento por antiguedad"
    print "sueldo:",incremento_sueldo,"pesos"
else :
    sueldo=3000
    print "sueldo",sueldo,"pesos"

