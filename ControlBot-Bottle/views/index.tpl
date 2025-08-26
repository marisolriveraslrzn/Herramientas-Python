<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ControlBot-Bottle</title>
    <style>
        body { font-family: sans-serif; background: #f0f0f0; padding: 20px; }
        .device { margin: 10px 0; padding: 10px; background: #fff; border-radius: 5px; }
        .on { color: green; }
        .off { color: red; }
        a { text-decoration: none; color: blue; }
    </style>
</head>
<body>
    <h1>🔌 Control de Dispositivos IoT</h1>
    % for name, state in devices.items():
        <div class="device">
            <strong>{{name.capitalize()}}</strong>: 
            <span class="{{'on' if state else 'off'}}">
                {{'Encendido' if state else 'Apagado'}}
            </span>
            — <a href="/toggle/{{name}}">Cambiar estado</a>
        </div>
    % end
</body>
</html>
