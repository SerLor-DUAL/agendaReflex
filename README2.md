# 📂 Estructura del Proyecto - Control de Usuarios con Reflex y PostgreSQL

Este proyecto es una aplicación web desarrollada en **Reflex** (antes Pynecone) para el **control de usuarios**.  
Permite registrar **entradas y salidas** conectándose a una base de datos **PostgreSQL**.

---

## 🏗️ Estructura de Carpetas
my_control_app/
├── .web/
├── assets/
├── my_control_app/
│ ├── init.py
│ ├── my_control_app.py
│ ├── pages/
│ │ ├── init.py
│ │ ├── login.py
│ │ ├── dashboard.py
│ ├── components/
│ │ ├── init.py
│ │ ├── navbar.py
│ │ └── user_form.py
│ ├── models/
│ │ ├── init.py
│ │ └── user.py
│ ├── state/
│ │ ├── init.py
│ │ └── user_state.py
│ └── utils/
│ ├── init.py
│ └── db.py
├── rxconfig.py
└── README.md

---

## 📂 Descripción de Carpetas y Archivos

### 🔹 Raíz del proyecto
- **`.web/`** → Carpeta generada automáticamente por Reflex. Contiene el frontend compilado (no se edita manualmente).  
- **`assets/`** → Archivos estáticos públicos: imágenes, fuentes, estilos, íconos, etc.  
- **`rxconfig.py`** → Configuración principal de la aplicación. Aquí defines:
  - `app_name`
  - conexión a **PostgreSQL**
  - ajustes globales  

---

### 🔹 `agendaReflex/` (paquete principal)
Carpeta con toda la lógica de la aplicación.

Aquí deben importarse **páginas, componentes, modelos y estados**.

---

## 📄 `pages/` → Páginas de la aplicación

Cada archivo define una página con el decorador `@rx.page()`.



## 🎨 `components/` → Componentes reutilizables

Pequeñas piezas de UI que se usan en varias páginas.


## 🗄️ `models/` → Modelos de base de datos

Clases ORM (SQLModel/SQLAlchemy) para representar tablas en PostgreSQL.


## ⚙️ `state/` → Lógica y estados

Define la lógica de negocio y los eventos que actualizan la interfaz.


## 🛠️ `utils/` → Funciones auxiliares

Funciones de apoyo, helpers y servicios.

