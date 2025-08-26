from bottle import Bottle, run, template, redirect
import os

app = Bottle()

# Simulación de estado de dispositivos
devices = {
    'light': False,
    'fan': False,
    'heater': False
}

@app.route('/')
def index():
    return template('index', devices=devices)

@app.route('/toggle/<device>')
def toggle_device(device):
    if device in devices:
        devices[device] = not devices[device]
    redirect('/')

# Ejecutar la app
if __name__ == '__main__':
    # Asegura que Bottle encuentre la carpeta de vistas
    os.environ['BOTTLE_VIEW_PATH'] = './views'
    run(app, host='localhost', port=8080, debug=True)
