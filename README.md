# 📦 Proyecto FastAPI + Reflex + PostgreSQL

Este proyecto está construido con:

- ✅ **FastAPI** como backend (API REST)
- ✅ **SQLModel** como ORM de la BD
- ✅ **Relfex** como interfaz de usuario (frontend)
- ✅ **PostgreSQL** como base de datos relacional

---

## 📁 Estructura general del proyecto

```
agendaReflex/
│   ├── backend/                            # Toda la lógica del servidor
│   │   ├── api/                            # Endpoints
│   │   │   ├── routes/
│   │   │   │   ├── users.py                # Rutas de usuarios
│   │   │   │   ├── users_admin.py          # FEATURE TODO: Rutas de usuarios para el administrador
│   │   │   │   ├── events.py               # Rutas de eventos
│   │   │   │   ├── events_admin.py         # FEATURE TODO: Rutas de eventos para el administrador
│   │   │   │   └── auth.py                 # Login, registro, autenticación
│   │   │   └── dependencies/
│   │   │       ├── auth_guard.py           # FEATURE TODO: Añadir autenticación a través de terceros
│   │   │       └── auth_cookies.py         # Verificación JWT + COOKIES - Actua como Middleware de cookies

│   │   ├── db/                             # Conexión y consultas SQL a la base de datos
│   │   │   └── db_handler.py               # Controlador de la conexión y gestión de PostgreSQL

│   │   ├── models/                         # Modelos SQLModel para BD y validación
│   │   │   ├── user
|   |   |   |     ├── model.py              # Modelo de usuario según la BD
|   |   |   |     └── DTOs                  # Carpeta para los DTOs del usuario
|   |   |   |         ├── base.py           # DTO base para el resto
|   |   |   |         ├── create.py         # DTO para la creación de usuarios, hereda del DTO base
|   |   |   |         ├── update.py         # DTO para la modificación de usuarios, hereda del DTO base
|   |   |   |         ├── read.py           # DTO para la lectura de usuarios, hereda del DTO base
|   |   |   |         └── login.py          # DTO para el login de usuarios, hereda del DTO base
│   │   │   ├── event
|   |   |   |     ├── model.py              # Modelo de evento según la BD
|   |   |   |     └── DTOs                  # Carpeta para los DTOs del evento
|   |   |   |         ├── base.py           # DTO base para el resto
|   |   |   |         ├── create.py         # DTO para la creación de eventos, hereda del DTO base
|   |   |   |         ├── update.py         # DTO para la modificación de eventos, hereda del DTO base
|   |   |   |         └── read.py           # DTO para la lectura de eventos, hereda del DTO base

│   │   ├── services/                       # Lógica de negocio separada de la API (Es decir "Controladores")
│   │   │   ├── user_service.py             # CRUD y otros de usuarios
│   │   │   └── event_Service.py            # CRUD y otros de eventos

│   │   ├── utils/                          # Funciones auxiliares reutilizables
│   │   │   ├── jwt.py                      # Crear y verificar tokens JWT
│   │   │   ├── cors.py                     # Manjeo de peticiones seguras de origen cruzado (Middleware)
│   │   │   └── hashing.py                  # Hashing de contraseñas (bcrypt)

│   │   └── config.py                       # Configuración de clases que usan información de .env

│   ├── frontend/                           # Interfaz de usuario con Reflex
│   │   ├──  TODO   

│   ├── requirements.in                     # Lista las dependencias directas del proyecto, sin versiones estrictas.
│   ├── requirements.txt                    # Versión bloqueada con todas las dependencias y sub-dependencias.
│   └── .env                                # Variables secretas (BD, JWT_SECRET, etc.)
```

---

## Guía para gestionar paquetes con piptools

> Antes de usar `pip-compile`, asegúrate de tener `pip-tools` instalado:
>     - Ejecuta `pip install pip-tools`

1. **Cuando necesites añadir un nuevo paquete:**  
   - Añádelo en `requirements.in`  
   - Ejecuta `py -m piptools compile requirements.in` para actualizar `requirements.txt`  
   - Ejecuta `py -m pip install -r requirements.txt` para instalar el nuevo paquete  

2. **Para actualizar paquetes existentes:**  
   - Actualiza la versión en `requirements.in` (o elimina la versión para obtener la más reciente)  
   - Ejecuta `py -m piptools compile requirements.in`  
   - Ejecuta `py -m pip install -r requirements.txt`  

3. **Para instalar dependencias en una máquina nueva:**  
   - Simplemente ejecuta `py -m pip install -r requirements.txt`  

> Este sistema garantiza que:  
> - Las dependencias estén correctamente registradas  
> - Todas las sub-dependencias estén bloqueadas a versiones específicas  
> - El entorno sea reproducible en diferentes máquinas  
> - Tengas una distinción clara entre las dependencias directas (en `.in`) y todas las dependencias (en `.txt`)  

---

## ✅ Buenas prácticas internas

- Las rutas **solo deben recibir y responder** datos, sin lógica pesada.  
- Toda la lógica de negocio debe estar en los servicios.  
- Las consultas SQL deben estar separadas en archivos específicos.  
- Las rutas privadas deben usar `Depends(get_current_user)` de el auth_guard para protección.  
- No conectar directamente a la base de datos desde los endpoints.  
- No incluir lógica de negocio dentro de las rutas.  

---

Si tienes dudas, grita, no importa.  
Este README es nuestra brújula. 🧭
