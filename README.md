# 🏨 Sistema de Gestión Hotelera (SGH) - Proyecto Web Integrado

## 📌 Introducción

### 📋 Descripción breve del proyecto
El presente proyecto plantea el desarrollo de un **Sistema de Gestión Hotelera** basado en tecnologías web integradas, con el objetivo de optimizar los procesos operativos de **reservas, administración de habitaciones, gestión de clientes y control financiero**. La solución sigue una **arquitectura cliente-servidor**, con acceso vía navegador tanto para el **personal del hotel** como para los **clientes**.

### 🎯 Objetivos del proyecto

#### Objetivo general
Desarrollar un sistema web integral que permita gestionar de forma automatizada las funciones operativas y administrativas de un hotel, mejorando la eficiencia, el control y la atención al cliente.

#### Objetivos específicos
- Implementar reservas en línea con control de disponibilidad en tiempo real.
- Gestionar procesos de check-in y check-out de forma digital.
- Diseñar una interfaz responsive para múltiples dispositivos.
- Generar reportes de ocupación, ingresos y estadísticas administrativas.

### 📈 Importancia y relevancia
El sector hotelero requiere soluciones modernas para adaptarse a la **digitalización**. Este proyecto responde a la necesidad de herramientas accesibles, automatizadas y eficientes para **hoteles pequeños y medianos**, mejorando la atención al cliente y los flujos internos.

---

## 🧠 Antecedentes

### 🔬 Innovaciones tecnológicas
- **Blockchain**: Seguridad y transparencia en reservas/pagos.
- **AR/VR**: Tours virtuales y entrenamiento de personal.
- **Chatbots**: Atención al cliente 24/7 y asistentes virtuales.

### 🔥 Tendencias actuales
- **Check-in sin contacto**: Ahorro de tiempo y seguridad.
- **Sostenibilidad**: Gestión inteligente de recursos.
- **Conexión móvil**: Reservas, servicios y pagos desde smartphones.

### ⚠️ Desafíos
- Integración con sistemas heredados.
- Seguridad informática (ciberseguridad).
- Capacitación del personal y gestión del cambio.

### 📦 Proyecto similar: Kipsu
**Kipsu** es una plataforma usada en LATAM (México, Brasil, Argentina) para comunicación en tiempo real entre hoteles y huéspedes. Se destaca por:
- Comunicación directa y automatización de respuestas.
- Recopilación de feedback.
- Integración con PMS y redes sociales.

---

## 🧾 Justificación del Proyecto

El SGH automatiza tareas como reservas, check-in/out y facturación, mejorando la **eficiencia operativa** y reduciendo errores humanos. Adicionalmente, permite:
- Uso de **precios dinámicos**.
- Cumplimiento legal y **seguridad de datos**.
- Integración con **pagos móviles** y tecnologías inteligentes.

---

## ⚙️ Descripción Técnica

### 🔧 Backend
**Framework:** Django (Python), usando el patrón **MTV**:
- **Model:** Define entidades como Clientes, Habitaciones, Reservas.
- **View:** Procesa la lógica de negocio.
- **Template:** HTML, CSS, Bootstrap con Django Template Language.

### 🌐 Ruteo y navegación
```python
# urls.py
path('', views.index, name='inicio')
