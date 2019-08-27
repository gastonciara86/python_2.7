Hr=int (raw_input("Ingrese Numero:"))
Min=int (raw_input("Ingrese Numero:"))
Seg=int (raw_input("Ingrese Numero:"))
if Hr<24 and Hr>-01:
        if Min<60 and Min>00:
                if Seg<60 and Seg>00:
                        print Hr,"hr",Min,"Min",Seg,"Seg"
else:
    print "No Corresponde Formato"