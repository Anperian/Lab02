list = ["Fisiología", "Psicometría", "Psicopatología", "Estadística", "Neuropsicología", "Análisis"] #Lista 1
list.append("Lógica")
list.append("Metodología")
list.append("Psicometría")
list.append("Evaluación")
list.append("Epistemología")
list.append("Psicometría")
list.reverse()
print(list)
print(f"La cantidad total de ítems es: {len(list)}")
print(f"La cantidad de veces que se repite un curso es: {list.count('Psicometría')}")
list.pop(0)
print(list)
list2 = []
list2.append(2.5)
list2.append(30)
list2.append(20.5)
list2.append(20)
list2.append(12.3)
list2.append(40)
list2.append("A")
list2.append("B")
list2.append("C")
print(list2)
print(f"La suma de ambas listas es: {list+list2}")