def change ():
     expense = 23.75
     money = 100
     vuelto = money - expense
     pesos = int(vuelto)
     centavos = vuelto - pesos
     resultado_centavo = int(centavos*100)
     print (f"Ingresar gasto:")
     print (f"Dinero recibido:")
     print (" ")
     print ("Vuelto")
     print (" ")
     print (f"pesos:{pesos}")
     print (f"centavos:{resultado_centavo}")
