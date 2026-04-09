# FaceID AI - Microservicio de Reconocimiento Facial

Este proyecto es una solución completa de verificación biométrica que utiliza Inteligencia Artificial para comparar rostros en tiempo real. Está diseñado siguiendo una arquitectura de microservicios, utilizando **Python (FastAPI + DeepFace)** y desplegado mediante **Docker**.

## 🚀 Inicio Rápido

1.  **Levantar la infraestructura (Docker):**
    Asegúrate de tener Docker instalado y ejecuta el siguiente comando en la raíz del proyecto:
    ```bash
    docker-compose up -d --build
    ```
    *Esto levantará la API en el puerto `8181` y la base de datos PostgreSQL en el `5433`.*

2.  **Abrir la Interfaz Web:**
    Simplemente abre el archivo `index.html` en tu navegador favorito.
    *   Sube una foto de registro.
    *   Usa la cámara para verificar tu identidad.

---

## 📘 Documentación del Proyecto

### 1. Introducción
El presente proyecto consiste en la implementación de un sistema de reconocimiento facial biométrico basado en una arquitectura de microservicios. El objetivo principal es proporcionar una solución desacoplada, escalable y eficiente para la verificación de identidad mediante el análisis comparativo de imágenes, integrando tecnologías modernas de Inteligencia Artificial (IA) y contenedores.

### 2. Arquitectura del Sistema
La solución se divide en tres capas principales que trabajan de forma coordinada:
*   **Frontend (Capa de Presentación):** Una interfaz web ligera que gestiona la interacción con el hardware del usuario (cámara) y la subida de archivos.
*   **Microservicio de IA (Capa Lógica):** Un motor basado en Python que procesa las imágenes y realiza el cálculo de similitud.
*   **PostgreSQL (Capa de Datos):** Un contenedor de base de datos preparado para almacenar registros de usuarios o logs de acceso.

### 3. Tecnologías Utilizadas

#### 3.1. DeepFace y Facenet
El núcleo de la inteligencia artificial reside en la librería **DeepFace**. Se utiliza el modelo **Facenet** (Google), que mapea rostros en un espacio euclídeo donde la "distancia" representa la similitud. El backend de detección es **OpenCV**, garantizando rapidez y precisión.

#### 3.2. FastAPI
Framework de alto rendimiento para Python. Su naturaleza asíncrona permite manejar tareas pesadas de IA sin bloquear el sistema, facilitando la comunicación segura mediante CORS.

#### 3.3. Docker y Orquestación
Todo el sistema está encapsulado en contenedores, lo que garantiza que las librerías complejas (como TensorFlow) funcionen en cualquier entorno. Gracias a **Docker Compose**, la gestión de redes y puertos es automática.

### 4. Funcionamiento Detallado

#### 4.1. El Proceso de Verificación
1.  **Captura WebRTC:** El navegador accede a la cámara mediante la API correspondiente.
2.  **Conversión a Blob:** El fotograma se dibuja en un canvas y se convierte en binario.
3.  **Transmisión:** Se envían ambas imágenes mediante una petición POST al microservicio.
4.  **Procesamiento de IA:** DeepFace calcula la "Distancia Coseno" entre ambos rostros.
5.  **Resultado:** Si la distancia es baja, se devuelve `verified: true`.

#### 4.2. UI con Personalidad
Se ha diseñado una interfaz de usuario minimalista basada en una estética clara y amigable. Incluye guías faciales y feedback inmediato para mejorar la experiencia del usuario final.

### 5. Ventajas
*   **Desacoplamiento:** La IA es independiente del cliente.
*   **Escalabilidad:** Fácil de replicar en entornos de alta carga.
*   **Seguridad:** Procesamiento centralizado en contenedores controlados.

---
*Desarrollado como parte de la práctica de Despliegue de Aplicaciones Web.*
