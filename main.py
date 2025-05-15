from flask import Flask, render_template, request, jsonify, redirect
app=Flask(__name__)

usuario=[]
id_contador=1

@app.route ("/", methods=['GET', 'POST'])
def crud():
    global id_contador
    if request.method=="POST":
        nombre=request.form ["nombre"] 
        correo=request.form ["correo"]
        usuario.append({"id": id_contador, "nombre": nombre, "correo": correo})
        id_contador+=1
    return render_template ("crud.html", usuario=usuario)












if __name__=="__main__":
    app.run(debug=True)