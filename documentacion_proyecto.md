# Documentación del Proyecto: Microservicio de Reconocimiento Facial

## 1. Introducción
El presente proyecto consiste en la implementación de un sistema de reconocimiento facial biométrico basado en una arquitectura de microservicios. El objetivo principal es proporcionar una solución desacoplada, escalable y eficiente para la verificación de identidad mediante el análisis comparativo de imágenes, integrando tecnologías modernas de Inteligencia Artificial (IA) y contenedores.

## 2. Arquitectura del Sistema
La solución se divide en tres capas principales que trabajan de forma coordinada:
*   **Frontend (Capa de Presentación):** Una interfaz web ligera que gestiona la interacción con el hardware del usuario (cámara) y la subida de archivos.
*   **Microservicio de IA (Capa Lógica):** Un motor basado en Python que procesa las imágenes y realiza el cálculo de similitud.
*   **PostgreSQL (Capa de Datos):** Un contenedor de base de datos preparado para almacenar registros de usuarios o logs de acceso (escalable según necesidades futuras).

## 3. Tecnologías Utilizadas

### 3.1. DeepFace y Facenet
El núcleo de la inteligencia artificial reside en la librería **DeepFace**. Para este proyecto, se ha configurado el modelo **Facenet**, desarrollado originalmente por Google. Facenet destaca por su capacidad de mapear rostros en un espacio euclídeo donde la "distancia" entre puntos representa directamente la similitud facial. Como backend de detección, se utiliza **OpenCV**, lo que garantiza un equilibrio entre velocidad y precisión.

### 3.2. FastAPI
El microservicio está construido sobre **FastAPI**, un framework de alto rendimiento para Python. Su naturaleza asíncrona permite manejar múltiples peticiones simultáneamente sin bloquear el hilo principal, algo crucial cuando se realizan tareas pesadas de IA. Además, facilita la comunicación segura mediante políticas de CORS configurables.

### 3.3. Docker y Orquestación
Todo el sistema está encapsulado en contenedores mediante **Docker**. Esto soluciona el problema de "en mi máquina funciona", permitiendo que las librerías complejas (como TensorFlow) se instalen en un entorno controlado y reproducible. Gracias a **Docker Compose**, podemos levantar toda la infraestructura (base de datos y API) con un solo comando, gestionando automáticamente las redes internas y los puertos.

## 4. Funcionamiento Detallado

### 4.1. El Proceso de Verificación
Cuando un usuario intenta acceder, el sistema realiza los siguientes pasos:
1.  **Captura WebRTC:** Utilizando la API `navigator.mediaDevices.getUserMedia`, el navegador accede a la cámara y muestra el flujo de vídeo.
2.  **Conversión a Blob:** El fotograma de la cámara se dibuja en un `<canvas>` oculto y se convierte en un objeto binario (Blob).
3.  **Transmisión:** Ambas imágenes (la de registro y la capturada) se envían mediante una petición POST `multipart/form-data` al microservicio.
4.  **Procesamiento de IA:** El microservicio guarda temporalmente las imágenes, las pasa por la red neuronal de Facenet y calcula la "Distancia Coseno".
5.  **Resultado:** Si la distancia es inferior al umbral de seguridad, se devuelve un resultado `verified: true`.

### 4.2. Frontend con Personalidad
Se ha diseñado una interfaz de usuario (UI) basada en principios de **diseño agradable y minimalista**. En lugar de una estética técnica agresiva, se optó por un tema claro con colores Indigo, bordes redondeados y una guía facial. Esto reduce la fricción del usuario y mejora la experiencia de uso (UX), haciendo que una tecnología compleja se sienta accesible.

## 5. Ventajas de esta Solución
Este enfoque ofrece múltiples beneficios:
*   **Desacoplamiento:** El frontend no conoce los detalles de la IA; solo envía imágenes y recibe un JSON. Esto permite actualizar la lógica de reconocimiento sin tocar el cliente.
*   **Escalabilidad:** Al estar en Docker, se pueden levantar múltiples instancias del microservicio facial para manejar una carga mayor de usuarios.
*   **Seguridad:** El procesamiento se realiza en el servidor (contenedor), manteniendo las imágenes fuera del alcance de scripts maliciosos en el cliente.

Este proyecto demuestra cómo la integración de IA avanzada y arquitecturas modernas puede simplificar tareas complejas y proporcionar una base sólida para sistemas de seguridad biométrica.
