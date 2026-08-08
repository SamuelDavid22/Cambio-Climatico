from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

DATABASE = "ecoaccion.db"

def crear_bd():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS historial(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        puntos INTEGER,
        nivel TEXT
    )
    """)
    con.commit()
    con.close()

crear_bd()

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/huella")
def huella():
    return render_template("huella.html")

@app.route("/historial")
def historial():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("SELECT fecha,puntos,nivel FROM historial ORDER BY id DESC")
    datos = cur.fetchall()
    con.close()
    return render_template("historial.html", historial=datos)

@app.route("/resultado", methods=["POST"])
def resultado():
    transporte=request.form["transporte"]
    energia=request.form["energia"]
    agua=request.form["agua"]
    recicla=request.form["recicla"]

    puntos=0
    t={"carro":40,"moto":30,"bus":20,"bicicleta":5,"caminar":0}
    puntos+=t.get(transporte,0)
    puntos+=30 if energia=="alto" else 20 if energia=="medio" else 10
    puntos+=20 if agua=="alto" else 10 if agua=="medio" else 5
    if recicla=="no":
        puntos+=10

    if puntos<=30:
        nivel,color,mensaje="Bajo","success","🌱 ¡Excelente trabajo! Tus hábitos ayudan a proteger el planeta."
    elif puntos<=60:
        nivel,color,mensaje="Medio","warning","🌿 Tu impacto ambiental es moderado. Todavía puedes mejorar."
    else:
        nivel,color,mensaje="Alto","danger","🌍 Tu huella de carbono es alta. Es importante cambiar algunos hábitos."

    recomendaciones=[]
    if transporte=="carro":
        recomendaciones.append("🚗 Usa transporte público o bicicleta algunos días.")
    elif transporte=="moto":
        recomendaciones.append("🏍 Reduce los recorridos en moto.")
    elif transporte=="bus":
        recomendaciones.append("🚌 Buen trabajo usando transporte público.")
    elif transporte=="bicicleta":
        recomendaciones.append("🚲 Excelente elección.")
    else:
        recomendaciones.append("🚶 Caminar ayuda al planeta.")

    recomendaciones.append("💡 Reduce el consumo de energía." if energia!="bajo" else "⚡ Buen consumo de energía.")
    recomendaciones.append("🚿 Ahorra agua." if agua!="bajo" else "🌊 Buen consumo de agua.")
    recomendaciones.append("♻️ Sigue reciclando." if recicla=="si" else "🗑 Empieza a reciclar.")

    con=sqlite3.connect(DATABASE)
    cur=con.cursor()
    cur.execute("INSERT INTO historial(puntos,nivel) VALUES(?,?)",(puntos,nivel))
    con.commit()
    con.close()

    return render_template("dashboard.html",
                           puntos=puntos,
                           nivel=nivel,
                           color=color,
                           mensaje=mensaje,
                           recomendaciones=recomendaciones)

if __name__=="__main__":
    app.run(debug=True)
