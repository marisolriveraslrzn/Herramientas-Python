# TareasModular-CherryPy

## Descripción
Backend modular con CherryPy para gestionar tareas. Ideal para enseñar arquitectura orientada a objetos, sesiones y rendimiento web.

## Características
- Arquitectura modular (MVC simplificado)
- Servidor multihilo con CherryPy
- Manejo de sesiones en memoria
- Integración con frontend externo (HTML estático o SPA)
- Código limpio y extensible

## Diagrama de clases

+-------------+ +-------------------+ | Task |<----->| TaskController | +-------------+ +-------------------+ | -title | | -tasks: list | | -done | | +add(title) | | +toggle() | | +toggle(i) | +-------------+ | +index() | +-------------------+



## Actividad: “Organiza tu semana”
1. Agrega tareas con prioridad y fecha límite.
2. Integra frontend con AJAX o Fetch API.
3. Simula usuarios con sesiones separadas.
4. Compara rendimiento con Flask usando `timeit` o `ab`.

## Comparación con Flask

| Característica         | CherryPy               | Flask                  |
|------------------------|------------------------|------------------------|
| Arquitectura modular   | Nativa (clases + rutas)| Manual (Blueprints)    |
| Multihilo              | Sí                     | Depende del servidor   |
| Sesiones               | RAM / archivo / DB     | Cookies / extensiones  |
| Rendimiento (local)    | 🔥 Rápido en RAM        | ⚡ Ligero pero depende  |
| Curva de aprendizaje   | Media                  | Baja                   |

## Ejecución
```bash
py app.py
```

Prueba accediendo directamente a:
```bash
http://127.0.0.1:8080/tasks
```