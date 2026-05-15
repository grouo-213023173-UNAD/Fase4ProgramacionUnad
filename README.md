# Fase4ProgramacionUnad

Realización de tarea #4 del curso de programacion UNAD

# Sistema Integral de Gestión - Software FJ

## Descripción

Este proyecto fue desarrollado en Python utilizando Programación Orientada a Objetos (POO).

El sistema permite gestionar:

- Clientes
- Servicios
- Reservas

La aplicación funciona sin bases de datos, utilizando únicamente objetos, listas y archivos de logs.

---

## Tecnologías utilizadas

- Python 3.12
- Git
- GitHub
- Programación Orientada a Objetos

---

## Características del sistema

- Manejo de clientes
- Gestión de reservas
- Servicios especializados
- Validaciones robustas
- Manejo avanzado de excepciones
- Registro de eventos y errores en logs
- Herencia
- Polimorfismo
- Encapsulación
- Abstracción

---

## Estructura del proyecto

```text
Fase_4_programacion/
│
├── main.py
│
├── models/
│   ├── cliente.py
│   ├── reserva.py
│   ├── servicio.py
│   │
│   └── servicios/
│       ├── reserva_sala.py
│       ├── alquiler_equipo.py
│       └── asesoria.py
│
├── exceptions/
│   └── custom_exceptions.py
│
├── utils/
│   └── logger.py
│
├── data/
│   └── logs.txt
│
└── README.md
```
