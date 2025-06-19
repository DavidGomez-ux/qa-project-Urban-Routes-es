🚕 PROYECTO URBAN ROUTES
Bienvenido al proyecto Urban Routes, un conjunto de pruebas automatizadas creadas para verificar que todo funcione como debe al solicitar un taxi desde la plataforma.
Desde elegir la tarifa ideal, ingresar los datos del pasajero, hasta añadir comodidades como mantas y helados… este proyecto simula el recorrido completo como si fueras el usuario real.

⸻

🧰 REQUISITOS

Para que este proyecto funcione correctamente, asegúrate de contar con lo siguiente:
	•	Python
	•	Selenium
	•	Pytest
	•	Acceso a un servidor funcional de Urban Routes

⸻

⚙️ INSTALACIÓN

Antes de empezar, asegúrate de tener:
	•	Python configurado en tu equipo
	•	Pytest incorporado en tu entorno de desarrollo (como PyCharm)
	•	Git instalado para la gestión del repositorio
	•	Los paquetes necesarios para automatización (Selenium y Requests)
	•	El repositorio clonado localmente
	•	ChromeDriver instalado para controlar el navegador 
 ### Que contiene el proyecto
 Este archivo contiene las pruebas automatizadas principales que validan el flujo completo de la plataforma Urban Routes. A través de estas pruebas se comprueba el correcto funcionamiento del proceso para pedir un taxi, desde el inicio hasta la solicitud final.

Funcionalidades automatizadas:
	•	Seleccionar origen y destino para una ruta.
	•	Elegir la tarifa (por ejemplo, tarifa confort).
	•	Registrar un número de teléfono y validar su confirmación.
	•	Agregar un método de pago con tarjeta.
	•	Escribir un mensaje al conductor.
	•	Solicitar servicios adicionales, como:
	•	Mantas y pañuelos.
	•	Helados.
	•	Buscar un taxi disponible y confirmar que el proceso esté visible en pantalla.

Estas pruebas aseguran que el flujo del usuario funcione correctamente y sin errores, simulando la interacción real con la aplicación desde el navegador.
### Data,Py
Este archivo contiene todos los datos de prueba y configuraciones base necesarios para la ejecución de los test automatizados del proyecto Urban Routes.

Contenido principal:
	•	Direcciones de origen y destino utilizadas en las pruebas.
	•	Número de teléfono simulado para pruebas de autenticación.
	•	Datos de tarjeta de crédito, como número y código de seguridad.
	•	Mensajes personalizados para el conductor.
	•	URL del servidor de pruebas donde corre la aplicación Urban Routes.

Este archivo centraliza los datos usados en las pruebas, permitiendo mantener el código limpio y facilitar cambios sin tener que modificar múltiples archivos.
### Instrucciones para hacer ejecutar las pruebas automatizadas.
Cómo ejecutar las pruebas:
	•	Para correr todas las pruebas: usar el comando pytest.
	•	Para ejecutar una prueba específica: usar pytest nombre_del_archivo.py.
	•	Para ver un reporte más detallado: usar pytest -v.

Casos de prueba incluidos:
	•	Ingreso de direcciones
	•	Selección de tarifa y modo personal
	•	Confirmación de número telefónico
	•	Agregado de método de pago
	•	Selección de manta, pañuelos y helados
	•	Envío de mensaje al conductor
	•	Confirmación del estado “buscando” al solicitar taxi

Notas adicionales:
	•	Las pruebas requieren conexión a internet.
	•	Algunas validaciones como el código telefónico se simulan por medio de funciones auxiliares.
	•	Se recomienda usar el navegador Google Chrome actualizado.
 * NOMBRE EDUARDO DAVID GOMEZ MIRANDA//COHORTE NUMERO 29

