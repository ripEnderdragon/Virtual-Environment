# Impor
from flask import Flask, render_template


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variabel yang memungkinkan penghitungan konsumsi energi peralatan
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    return (lights * light_coef + device * devices_coef)/ size * home_coef 

# Halaman pertama
@app.route('/')
def index():
    return render_template('index.html')

# Halaman kedua
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size,
                           )

# Halaman ketiga
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',
                            size = size, 
                            lights = lights                           
                           )

# Halaman keempat
@app.route('/input')
def input_1():
    return render_template(
                            'input.html',                         
                           )

# Perhitungan
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
app.run(debug=True)
