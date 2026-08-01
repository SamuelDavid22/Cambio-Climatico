# Cambio-Climatico
#Este es mi proyecto final sobre el cambio climatico
#Este es un codigo base solo funciona en la terminal


print("===================================")
print("      🌎 ECOACCIÓN IA 🌎")
print("===================================\n")

print("Responde las siguientes preguntas:\n")

transporte = input(
    "¿Cómo te transportas normalmente?"
    " (carro, moto, bus, bicicleta, caminando): "
).lower()

recicla = input(
    "¿Reciclas? (si, a veces, no): "
).lower()

horas = int(input(
    "¿Cuántas horas al día utilizas aparatos eléctricos?: "
))

print("\nAnalizando tus respuestas...\n")

# Calcular un puntaje sencillo
puntos = 0

# Transporte
if transporte == "carro":
    puntos += 3
elif transporte == "moto":
    puntos += 2
elif transporte == "bus":
    puntos += 1
elif transporte in ["bicicleta", "caminando"]:
    puntos += 0

# Reciclaje
if recicla == "no":
    puntos += 2
elif recicla == "a veces":
    puntos += 1

# Consumo eléctrico
if horas > 10:
    puntos += 3
elif horas > 6:
    puntos += 2
else:
    puntos += 1

print("========== RESULTADOS ==========")

if puntos <= 3:
    print("🌱 Tu impacto ambiental es BAJO.")
elif puntos <= 6:
    print("🌿 Tu impacto ambiental es MEDIO.")
else:
    print("🔥 Tu impacto ambiental es ALTO.")

print("\nRecomendaciones:")

if transporte in ["carro", "moto"]:
    print("- Usa bicicleta o transporte público cuando sea posible.")

if recicla != "si":
    print("- Empieza a separar los residuos para reciclar.")

if horas > 6:
    print("- Apaga los aparatos que no estés utilizando.")

print("- Reduce el uso de plásticos de un solo uso.")
print("- Ahorra agua siempre que puedas.")

print("\n🌎 ¡Cada pequeña acción ayuda a combatir el cambio climático!")
