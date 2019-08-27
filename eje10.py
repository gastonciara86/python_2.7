num=int(raw_input("Ingrese Segundos:"))
day=num/86400
hr=num/3600
Min=((num-(hr*3600))/60)
seg=num-((hr*3600)+(Min*60))
print day, "dia", hr, "hr", Min ,"Min", seg , "seg"
