from flask import Flask, render_template, request
app = Flask (__name__)

@app.route('/')
def inicio ():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route ('/mensaje', methods=['POST'])
def mensaje():
    if request.method == 'POST': 
        Nombre = request.form['Nombre']
        Telefono = int(request.form['Telefono'])
        Correo = request.form['Correo']
        Asunto = request.form['Asunto']   
    return render_template('mensaje.html', res=Nombre, mes=Correo, res2=Telefono)
if __name__ =='__main__':
    app.run()   

