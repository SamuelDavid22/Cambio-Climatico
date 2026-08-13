from flask import Flask, render_template, request

app = Flask(__name__)


# ==========================
# HISTORIAL
# ==========================

historial_datos = []


# ==========================
# Página principal
# ==========================

@app.route("/")
def inicio():
    return render_template("index.html")


# ==========================
# Calculadora
# ==========================

@app.route("/huella")
def huella():
    return render_template("huella.html")


# ==========================
# IA Ambiental
# ==========================

@app.route("/ia", methods=["GET", "POST"])
def ia():

    respuesta = None
    pregunta = ""

    if request.method == "POST":

        pregunta = request.form.get("pregunta", "").strip()

        if pregunta:

            texto = pregunta.lower()

            # ==========================
            # Recomendaciones de IA
            # ==========================

            if (
                "agua" in texto
                or "ducha" in texto
                or "llave" in texto
            ):

                respuesta = (
                    "💧 Para cuidar el agua, intenta reducir "
                    "el tiempo de tus duchas, cerrar la llave "
                    "mientras te cepillas los dientes y reutilizar "
                    "agua cuando sea posible."
                )

            elif (
                "luz" in texto
                or "electricidad" in texto
                or "energia" in texto
                or "energía" in texto
                or "aparato" in texto
            ):

                respuesta = (
                    "💡 Para ahorrar energía, apaga las luces "
                    "que no estés utilizando, desconecta los "
                    "aparatos que no necesites y aprovecha "
                    "la luz natural."
                )

            elif (
                "carro" in texto
                or "auto" in texto
                or "moto" in texto
                or "transporte" in texto
            ):

                respuesta = (
                    "🚲 Para reducir las emisiones, intenta "
                    "caminar, utilizar bicicleta o transporte "
                    "público cuando sea posible. También puedes "
                    "compartir el vehículo."
                )

            elif (
                "reciclar" in texto
                or "reciclaje" in texto
                or "basura" in texto
                or "residuos" in texto
                or "plastico" in texto
                or "plástico" in texto
            ):

                respuesta = (
                    "♻️ Separa correctamente los residuos y "
                    "reutiliza los materiales siempre que puedas. "
                    "Recuerda separar papel, cartón, plástico, "
                    "vidrio y residuos orgánicos."
                )

            elif (
                "comida" in texto
                or "alimentacion" in texto
                or "alimentación" in texto
                or "carne" in texto
                or "alimento" in texto
            ):

                respuesta = (
                    "🥦 Intenta evitar desperdiciar alimentos, "
                    "compra solamente lo necesario y aprovecha "
                    "las sobras. También puedes incluir más "
                    "alimentos de origen vegetal."
                )

            elif (
                "arbol" in texto
                or "árbol" in texto
                or "plantas" in texto
                or "naturaleza" in texto
                or "bosque" in texto
            ):

                respuesta = (
                    "🌳 Cuida las zonas verdes, evita arrojar "
                    "basura en espacios naturales y participa "
                    "en actividades de reforestación cuando "
                    "sea posible."
                )

            else:

                respuesta = (
                    "🌍 Puedes comenzar reduciendo el consumo "
                    "innecesario, ahorrando agua y energía, "
                    "reciclando y utilizando medios de transporte "
                    "sostenibles cuando sea posible."
                )

            # ==========================
            # GUARDAR EN HISTORIAL
            # ==========================

            historial_datos.append({
                "tipo": "ia",
                "pregunta": pregunta,
                "respuesta": respuesta
            })

    return render_template(
        "ia.html",
        pregunta=pregunta,
        respuesta=respuesta
    )


# ==========================
# Historial
# ==========================

@app.route("/historial")
def historial():

    return render_template(
        "historial.html",
        historial=historial_datos
    )


# ==========================
# Resultado de huella
# ==========================

@app.route("/resultado", methods=["POST"])
def resultado():

    transporte = request.form["transporte"]
    energia = request.form["energia"]
    agua = request.form["agua"]
    recicla = request.form["recicla"]

    puntos = 0

    # ==========================
    # Transporte
    # ==========================

    if transporte == "carro":
        puntos += 40

    elif transporte == "moto":
        puntos += 30

    elif transporte == "bus":
        puntos += 20

    elif transporte == "bicicleta":
        puntos += 5

    elif transporte == "caminar":
        puntos += 0

    # ==========================
    # Energía
    # ==========================

    if energia == "alto":
        puntos += 30

    elif energia == "medio":
        puntos += 20

    else:
        puntos += 10

    # ==========================
    # Agua
    # ==========================

    if agua == "alto":
        puntos += 20

    elif agua == "medio":
        puntos += 10

    else:
        puntos += 5

    # ==========================
    # Reciclaje
    # ==========================

    if recicla == "no":
        puntos += 10

    # ==========================
    # Nivel
    # ==========================

    if puntos <= 30:

        nivel = "Bajo"
        color = "success"

        mensaje = (
            "🌱 ¡Excelente trabajo! Tus hábitos ayudan "
            "a proteger el planeta."
        )

    elif puntos <= 60:

        nivel = "Medio"
        color = "warning"

        mensaje = (
            "🌿 Tu impacto ambiental es moderado. "
            "Todavía puedes mejorar."
        )

    else:

        nivel = "Alto"
        color = "danger"

        mensaje = (
            "🌍 Tu huella de carbono es alta. "
            "Es importante cambiar algunos hábitos."
        )

    # ==========================
    # Recomendaciones
    # ==========================

    recomendaciones = []

    if transporte == "carro":

        recomendaciones.append(
            "🚗 Intenta utilizar transporte público, bicicleta "
            "o compartir el vehículo algunos días."
        )

    elif transporte == "moto":

        recomendaciones.append(
            "🏍 Reduce los recorridos en moto cuando sea posible."
        )

    elif transporte == "bus":

        recomendaciones.append(
            "🚌 ¡Buen trabajo! El transporte público "
            "genera menos emisiones."
        )

    elif transporte == "bicicleta":

        recomendaciones.append(
            "🚲 Excelente elección. La bicicleta no genera "
            "emisiones contaminantes."
        )

    elif transporte == "caminar":

        recomendaciones.append(
            "🚶 Caminar es una de las mejores opciones "
            "para cuidar el planeta."
        )

    if energia == "alto":

        recomendaciones.append(
            "💡 Apaga las luces y desconecta los aparatos "
            "que no estés utilizando."
        )

    elif energia == "medio":

        recomendaciones.append(
            "🔋 Puedes seguir reduciendo tu consumo eléctrico "
            "utilizando bombillos LED."
        )

    else:

        recomendaciones.append(
            "⚡ Muy bien. Tu consumo eléctrico es bajo."
        )

    if agua == "alto":

        recomendaciones.append(
            "🚿 Reduce el tiempo de las duchas y cierra "
            "la llave cuando no la uses."
        )

    elif agua == "medio":

        recomendaciones.append(
            "💧 Intenta reutilizar agua para limpiar "
            "o regar plantas."
        )

    else:

        recomendaciones.append(
            "🌊 Excelente manejo del consumo de agua."
        )

    if recicla == "si":

        recomendaciones.append(
            "♻️ Continúa reciclando y separando "
            "correctamente los residuos."
        )

    else:

        recomendaciones.append(
            "🗑 Empieza a separar plástico, vidrio, "
            "papel y cartón para reciclar."
        )

    # ==========================
    # GUARDAR RESULTADO
    # ==========================

    historial_datos.append({
        "tipo": "huella",
        "puntos": puntos,
        "nivel": nivel,
        "color": color
    })

    return render_template(
        "dashboard.html",
        puntos=puntos,
        nivel=nivel,
        color=color,
        mensaje=mensaje,
        recomendaciones=recomendaciones
    )


# ==========================
# Ejecutar aplicación
# ==========================

if __name__ == "__main__":
    app.run(debug=True)
