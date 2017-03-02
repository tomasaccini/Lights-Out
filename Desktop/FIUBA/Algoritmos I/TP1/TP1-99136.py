import random
luz_prendida = "O"
luz_apagada = "-"
cantidad_niveles = 5
modo_predeterminado = 1
modo_aleatorio = 2
tamaño_minimo_tablero = 5
tamaño_maximo_tablero = 10
puntaje_luz_prendida_al_reinciar = -50
puntaje_ganar_nivel = 500
puntaje_perder_nivel = -300
lista_coordenadas_nivel_1 = [[1,1,luz_prendida],[1,2,luz_prendida],[1,3,luz_apagada],[1,4,luz_prendida],[1,5,luz_prendida],[2,1,luz_prendida],[2,2,luz_apagada],[2,3,luz_prendida],[2,4,luz_apagada],[2,5,luz_prendida],[3,1,luz_apagada],[3,2,luz_prendida],[3,3,luz_prendida],[3,4,luz_prendida],[3,5,luz_apagada],[4,1,luz_prendida],[4,2,luz_apagada],[4,3,luz_prendida],[4,4,luz_apagada],[4,5,luz_prendida],[5,1,luz_prendida],[5,2,luz_prendida],[5,3,luz_apagada],[5,4,luz_prendida],[5,5,luz_prendida]]
lista_coordenadas_nivel_2 = [[1,1,luz_apagada],[1,2,luz_prendida],[1,3,luz_apagada],[1,4,luz_prendida],[1,5,luz_apagada],[2,1,luz_prendida],[2,2,luz_prendida],[2,3,luz_apagada],[2,4,luz_prendida],[2,5,luz_prendida],[3,1,luz_apagada],[3,2,luz_prendida],[3,3,luz_apagada],[3,4,luz_prendida],[3,5,luz_apagada],[4,1,luz_prendida],[4,2,luz_apagada],[4,3,luz_prendida],[4,4,luz_apagada],[4,5,luz_prendida],[5,1,luz_prendida],[5,2,luz_apagada],[5,3,luz_prendida],[5,4,luz_apagada],[5,5,luz_prendida]]
lista_coordenadas_nivel_3 = [[1,1,luz_prendida],[1,2,luz_apagada],[1,3,luz_apagada],[1,4,luz_apagada],[1,5,luz_prendida],[2,1,luz_prendida],[2,2,luz_prendida],[2,3,luz_apagada],[2,4,luz_prendida],[2,5,luz_prendida],[3,1,luz_apagada],[3,2,luz_apagada],[3,3,luz_prendida],[3,4,luz_apagada],[3,5,luz_apagada],[4,1,luz_prendida],[4,2,luz_apagada],[4,3,luz_prendida],[4,4,luz_apagada],[4,5,luz_apagada],[5,1,luz_prendida],[5,2,luz_apagada],[5,3,luz_prendida],[5,4,luz_prendida],[5,5,luz_apagada]]
lista_coordenadas_nivel_4 = [[1,1,luz_prendida],[1,2,luz_prendida],[1,3,luz_apagada],[1,4,luz_prendida],[1,5,luz_prendida],[2,1,luz_apagada],[2,2,luz_apagada],[2,3,luz_apagada],[2,4,luz_apagada],[2,5,luz_apagada],[3,1,luz_prendida],[3,2,luz_prendida],[3,3,luz_apagada],[3,4,luz_prendida],[3,5,luz_prendida],[4,1,luz_apagada],[4,2,luz_apagada],[4,3,luz_apagada],[4,4,luz_apagada],[4,5,luz_prendida],[5,1,luz_prendida],[5,2,luz_prendida],[5,3,luz_apagada],[5,4,luz_apagada],[5,5,luz_apagada]]
lista_coordenadas_nivel_5 = [[1,1,luz_apagada],[1,2,luz_prendida],[1,3,luz_apagada],[1,4,luz_apagada],[1,5,luz_prendida],[2,1,luz_apagada],[2,2,luz_apagada],[2,3,luz_apagada],[2,4,luz_prendida],[2,5,luz_prendida],[3,1,luz_apagada],[3,2,luz_apagada],[3,3,luz_apagada],[3,4,luz_apagada],[3,5,luz_apagada],[4,1,luz_prendida],[4,2,luz_prendida],[4,3,luz_apagada],[4,4,luz_apagada],[4,5,luz_apagada],[5,1,luz_prendida],[5,2,luz_prendida],[5,3,luz_apagada],[5,4,luz_apagada],[5,5,luz_apagada]]

def verificador_input_numerico(mensaje, minimo, maximo):
	""" Recibe un mensaje (cadena), un numero minimo y un numero maximo (enteros). Muestra el mensaje recibido por parametro por pantalla y espera hasta que el usuario 
	ingrese un numero entero que este entre los valores minimo y maximo (incluidos). En caso de no ingresar un numero, o que el ingresado este fuera del rango, vuelve a pedirlo.
	Finalmente devuelve el numero ingresado por el usuario."""
	numero = ""
	while not numero.isdigit():
		numero = input(mensaje)
		if numero.isdigit():
			if int(numero) < minimo or int(numero) > maximo:
				numero = ""
	return int(numero)

def imprimir_tablero(lista_coordenadas,tamaño_matriz):
	""" Recibe una lista con las coordenadas del juego (cada componente de la lista que recibe son listas con 3 componentes, de la forma [fila, columna, estado de la luz]),
	y el tamaño de la matriz. Imprime el tablero con las cabeceras y el caracter guardado en luz_prendida en caso que la luz este encendida, y en el caracter guardado en luz_apagada en caso que 
	la luz este apagada."""
	#Carga la cabecera de las columnas
	for i in range(0,tamaño_matriz+1):
		print(i, end = "  ")
	print()
	for i in range(1,tamaño_matriz+1):
		#Carga las cabeceras de las filas
		if i < 10:
			#Cuando el numero de la columna es de un digito, dejo dos espacios
			print(i, end = "  ")
		else:
			#Cuando el numero de la columna es de dos digitos (10), dejo un solo espacio para corregir el caracter extra
			print(i, end = " ")
		#Carga el resto de la fila (todas las coordenadas)
		for j in range(1,tamaño_matriz+1):
			if [i,j,luz_prendida] in lista_coordenadas:
				print(luz_prendida, end = "  ")
			else:
				print(luz_apagada, end = "  ")
		print()

def cantidad_luces_apagadas(lista_coordenadas):
	""" Recibe una lista de coordenadas y devuelve la cantidad de luces apagadas que tiene dicho tablero. """
	luces_apagadas = 0
	for coord in lista_coordenadas:
		if coord[2] == luz_apagada:
			luces_apagadas += 1
	return luces_apagadas

def invertidor_en_cruz(lista_coordenadas,fila,columna,tamaño_matriz):
	""" Recibe una lista con las coordenadas del juego (cada componente de la lista que recibe son listas con 3 componentes, de la forma [fila, columna, estado de la luz]),
	dos numeros enteros que representan fila y columna (esta sera la coordenada centro). Modifica las luces de una posicion dada y sus contiguas. """
	invertir_espacio(lista_coordenadas,fila,columna)
	if fila != tamaño_matriz:
		invertir_espacio(lista_coordenadas,fila+1,columna)
	if columna != tamaño_matriz:
		invertir_espacio(lista_coordenadas,fila,columna+1)
	if fila != 1:
		invertir_espacio(lista_coordenadas,fila-1,columna)
	if columna != 1:
		invertir_espacio(lista_coordenadas,fila,columna-1)

def invertir_espacio(lista_coordenadas,fila,columna):
	""" Recibe una lista con las coordenadas del juego (cada componente de la lista que recibe son listas con 3 componentes, de la forma [fila, columna, estado de la luz]) y 
	dos numeros enteros que representan fila y columna de una coordenada. Modifica la lista recibida, y cambia el estado de dicha coordenada (luz_prendida por luz_apagada y viceversa)."""
	if [fila,columna,luz_prendida] in lista_coordenadas:
		indice = lista_coordenadas.index([fila,columna,luz_prendida])
		lista_coordenadas[indice] = [fila,columna,luz_apagada]
	elif [fila,columna,luz_apagada] in lista_coordenadas:
		indice = lista_coordenadas.index([fila,columna,luz_apagada])
		lista_coordenadas[indice] = [fila,columna,luz_prendida]

def cargar_nivel_aleatoriamente(tamaño_matriz):
	""" Recibe el tamanio del tablero y crea una lista de coordenadas vacia la cual es llenada aleatoriamente con todas las coordenadas con el formato [fila, columna, estado de la luz], asignando un estado de la luz al azar.
	Devuelve una tupla con el mismo contenido que la lista de coordenadas."""
	lista_coordenadas = []
	for i in range(1,tamaño_matriz+1):
		for j in range(1,tamaño_matriz+1):
			if random.randint(0,1) == 0:
				lista_coordenadas.append([i,j,luz_apagada])
			else:
				lista_coordenadas.append([i,j,luz_prendida])
	return lista_coordenadas

def cargar_nivel_predeterminado(nivel):
	""" Recibe el nivel del juego (1 al 5) y devuelve la lista de coordenadas predeterminada para dicho nivel """
	if nivel == 1:
		return lista_coordenadas_nivel_1
	elif nivel == 2:
		return lista_coordenadas_nivel_2
	elif nivel == 3:
		return lista_coordenadas_nivel_3
	elif nivel == 4:
		return lista_coordenadas_nivel_4
	elif nivel == 5:
		return lista_coordenadas_nivel_5

def juego(modo):
	""" Recibe un modo de juego representado como 1 o 2 (enteros) (1 por predeterminado y 2 aleatorio). En caso que el modo de juego sea aleatorio, pide el tamaño del tablero al usuario.
	En conjunto con el resto de las funciones, imprime el tablero inicial, pide al usuario coordenadas e imprime los cambios, hasta que se quede sin movimientos o gane los 5 niveles. """
	lista_coordenadas = list([])
	puntaje_total = 0
	nivel = 1
	if modo == modo_predeterminado:
		tamaño_matriz = tamaño_minimo_tablero
	else:
		tamaño_matriz = verificador_input_numerico("Ingrese el tamaño de la matriz (de 5 a 10 inclusive): ",tamaño_minimo_tablero,tamaño_maximo_tablero)
	while nivel <= cantidad_niveles:
		movimientos = tamaño_matriz * 3
		puntaje_nivel = 0
		if modo == modo_predeterminado:
			#Completo la lista con las luces predeterminadas
			lista_coordenadas = cargar_nivel_predeterminado(nivel)
		else:
			#Completo la lista aletoriamente y guardo la disposicion original del nivel en caso de que el usuario resetee.
			lista_coordenadas = cargar_nivel_aleatoriamente(tamaño_matriz)
		coordenadas_del_nivel = tuple(lista_coordenadas)
		print("\nBienvenido al nivel {}\n".format(nivel))
		imprimir_tablero(lista_coordenadas, tamaño_matriz)
		luces_apagadas = cantidad_luces_apagadas(lista_coordenadas)
		while movimientos > 0 and luces_apagadas != tamaño_matriz * tamaño_matriz:
			print("\nMovimientos restantes: {}".format(movimientos))
			print("\nSeleccione la coordenada a cambiar en el tablero, o siga las instrucciones para resetear el nivel")
			fila = verificador_input_numerico("Ingrese el numero de fila de 1 a {}, o 0 para resetear el nivel: ".format(tamaño_matriz), 0, tamaño_matriz)
			columna =  verificador_input_numerico("Ingrese el numero de columna de 1 a {}, o 0 para resetear el nivel: ".format(tamaño_matriz), 0, tamaño_matriz)
			print()
			#Con que el usuario haya ingresado al menos un 0, se resetea el nivel.
			if fila == 0 or columna == 0:
				print("Has reiniciado el nivel!")
				movimientos = tamaño_matriz * 3
				lista_coordenadas = list(coordenadas_del_nivel)
				puntaje_nivel += (tamaño_matriz * tamaño_matriz - luces_apagadas) * puntaje_luz_prendida_al_reinciar
				imprimir_tablero(lista_coordenadas, tamaño_matriz)
				luces_apagadas = cantidad_luces_apagadas(lista_coordenadas)
				print("Puntaje de este nivel: {}. Puntaje total: {}.".format(puntaje_nivel,puntaje_total))
				continue
			invertidor_en_cruz(lista_coordenadas,fila,columna,tamaño_matriz)
			imprimir_tablero(lista_coordenadas, tamaño_matriz)
			luces_apagadas = cantidad_luces_apagadas(lista_coordenadas)
			movimientos -= 1
		"""Puse primero la condicion de que apago todo el tablero, porque puede ser que en el ultimo movimiento haya apagado todas, y asi entraria en la primera condicion
		a pesar de tener 0 movimientos. Si no completo el tablero, y le quedan movimientos, entonces el jugador resetio el nivel."""
		if luces_apagadas == tamaño_matriz * tamaño_matriz:
			puntaje_nivel += puntaje_ganar_nivel
			print("Felicitaciones, ganaste el {} nivel.".format(nivel))
			nivel += 1
		elif movimientos == 0:
			puntaje_nivel += puntaje_perder_nivel
			puntaje_total += puntaje_nivel
			break
		puntaje_total += puntaje_nivel
		print("Puntaje de este nivel: {}. Puntaje total: {}.".format(puntaje_nivel,puntaje_total))
	#Una vez que sale del while mas grande, si la variable nivel es mayor a la cantidad de niveles, entonces el usuario ha ganado el juego. En caso contrario, perdio y vuelve al menu principal
	if nivel > cantidad_niveles:
		print("Felicitaciones. Ganaste el juego! Tu puntaje total fue {}.\n\n".format(puntaje_total))
	else:
		print("Te quedaste sin movimientos. Perdiste! Tu puntaje fue de {} puntos. Intentalo nuevamente.\n".format(puntaje_total))

def menu_principal():
	""" Funcion de presentacion del juego. Imprime un mensaje de bienvenida, y pide al usuario que ingrese un modo de juego (predeterminado o aleatorio) o bien que salga del juego. """
	while True:
		print("Bienvenido a Luces Fuera.")
		modo_juego = verificador_input_numerico("\nIngrese un 1 para ingresar al modo predeterminado (5x5), un 2 para el modo aleatorio (tamaño a definir por el usuario), o un 0 para salir \n\r", 0, 2)
		if modo_juego == 0:
			break
		else:
			juego(modo_juego)

menu_principal()