def change ():
     expense = 23.75
     money = 100
     vuelto = money - expense
     pesos = int(vuelto)
     centavos = vuelto - pesos
     resultado_centavo = int(centavos*100)
     print (f"Ingresar gasto:{expense}")
     print (f"Dinero recibido: {money}")
     print (" ")
     print ("Vuelto")
     print (" ")
     print (f"pesos:{pesos}")
     print (f"centavos:{resultado_centavo}")
