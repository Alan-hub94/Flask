from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('list.html')#Creo un path para que me redireccione a la lista de lenguajes.

@app.route("/lenguajes")#Creo un nuevo path para que me muestre la lista.
def lenguajes():
    return render_template('lenguajes.html')

@app.route("/about")            #--
def about():                    #   -->Esto nada que ver, era solo para practicar y para ver si funcionaba primero con esto
    return "<h1> hola </h1>"    #--

if __name__== "__main__":
    app.run(debug=True) #para que no te desconectes del servidor y solo actualicecd la pagina, me refiero al "debug=True"


