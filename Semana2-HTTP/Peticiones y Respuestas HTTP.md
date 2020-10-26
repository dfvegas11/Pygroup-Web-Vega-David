# Tipos de peticiones HTTP

Los métodos HTTP permiten comunicar al servidor lo que se quiere realizar con un resource bajo una URL.

## ** GET: **
Es la madre de todas las peticiones de HTTP. Este método de petición existía ya en los inicios de la 
world wide web y se utiliza para solicitar unrecurso, como un archivo HTML, del servidor web. 
Todas las peticiones que usan el método GET, deberán recuperar únicamente datos.

## ** HEAD: **
Se utiliza para solicitar que el servidor solo envíe el encabezado de la respuesta, sin el archivo. 
Esta alternativa es conveniente cuando se han de transferir archivos muy voluminosos, ya que, con esta petición,
el cliente conoce primero el tamaño del archivo para luego poder decidir si acepta recibirlo o no.

## ** OPTIONS: **
Representa una solicitud de información acerca de las opciones de comunicación disponibles en el canal de 
solicitud/respuesta identificada por el Request-URI. En otras palabras, éste método es el que utilizamos para 
describir las opciones de comunicación existentes de un recurso destino.

## ** POST: **
Es usado cuando se requiere enviar información al servidor como, por ejemplo, un archivo de actualización, 
información de formulario, etc. En otras palabras, éste método se usa cuando se necesita enviar una entidad para 
algún recurso determinado.

## ** PUT: **
Utilizado normalmente para actualizar contenidos, pero también pueden crearlos. Solicita que el servidor almacene 
el cuerpo de la entidad en una ubicación específica dada por el URL.

## ** DELETE: **
Se utiliza para solicitar al servidor que elimine un archivo en una ubicación específica dada por la URL.

## ** TRACE: **
Este método solicita al servidor que introduzca en la respuesta todos los datos que reciba en el mensaje de petición. 
Se utiliza con fines de depuración y diagnóstico ya que el cliente puede ver lo que llega al servidor y de esta forma 
ver todo lo que añaden al mensaje los servidores intermedios. Es un método muy utilizado para la depuración y también 
para el desarrollo.

## ** CONNECT: **
Es usado por el cliente para establecer una conexión de red con un servidor web mediante HTTP misma que se establece 
en forma de un túnel.

## ** PATCH: **
Su función es la misma que PUT, el cual sobreescribe completamente un recurso. Se utiliza para actualizar, de manera
parcial una o varias partes. Está orientado también para el uso con proxy.

# Códigos de respuesta HTTP

Es un número que indica que ha pasado con la petición, el resto del contenido de la respuesta dependerá del valor 
de este código.
Cada código tiene un significado concreto, sin embargo el número de los códigos están elegidos de tal 
forma que según si pertenece a una centena u otra se pueda identificar el tipo de respuesta que ha dado el servidor:

1. ** Códigos con formato 1xx: ** Respuestas informativas. Indica que la petición ha sido recibida y se está procesando.
Ejemplos:
- 100 Continue: El navegador puede continuar realizando su petición.
- 101 Switching Protocols: El servidor acepta el cambio de protocolo propuesto por el navegador.
- 102 Processing: El servidor está procesando la petición del navegador pero todavía no ha terminado.
- 103 Checkpoint: Se va a reanudar una petición POST o PUT que fue abortada previamente.

1. Códigos con formato 2xx: Respuestas correctas. Indica que la petición ha sido procesada correctamente.
- 200 OK: Respuesta estándar para peticiones correctas.
- 201 Createds: La petición ha sido completada y ha resultado en la creación de un nuevo recurso.
- 202 Accepted: La petición ha sido aceptada para procesamiento, pero este no ha sido completado.
- 204 No Content: La petición se ha completado con éxito pero su respuesta no tiene ningún contenido.

1. Códigos con formato 3xx: Respuestas de redirección. Indica que el cliente necesita realizar más acciones para 
finalizar la petición.
- 300 Multiple Choices: Indica opciones múltiples para el URI que el cliente podría seguir.
- 301 Moved Permanently: Esta y todas las peticiones futuras deberían ser dirigidas a la URL dada.
- 303 See Other (desde HTTP/1.1): La respuesta a la petición puede ser encontrada bajo otra URI utilizando el método GET.
- 304 Not Modified: Indica que la petición a la URL no ha sido modificada desde que fue requerida por última vez.

1. Códigos con formato 4xx: Errores causados por el cliente. Indica que ha habido un error en el procesado de la 
petición a causa de que el cliente ha hecho algo mal.
- 400 Bad Request: El servidor no procesará la solicitud, porque no puede, o no debe, debido a algo que es percibido 
como un error del cliente
- 403 Forbidden: La solicitud fue legal, pero el servidor rehúsa responderla dado que el cliente no tiene los 
privilegios para realizarla.
- 404 Not Found: Recurso no encontrado. Se utiliza cuando el servidor web no encuentra la página o recurso solicitado.
- 410 Gone: Indica que el recurso solicitado ya no está disponible y no lo estará de nuevo.
- 411 Length Required: El servidor rechaza la petición del navegador porque no incluye la cabecera adecuada.
- 451 Unavailable for Legal Reasons: El contenido ha sido eliminado como consecuencia de una orden judicial o 
sentencia emitida por un tribunal.

1. Códigos con formato 5xx: Errores causados por el servidor. Indica que ha habido un error en el procesado de la 
petición a causa de un fallo en el servidor.
- 500 Internal Server Error.
- 501 Not Implemented: El servidor no soporta alguna funcionalidad necesaria para responder a la solicitud del navegador.
- 503 Service Unavailable: El servidor no puede responder a la petición del navegador porque está congestionado o está 
realizando tareas de mantenimiento.
- 505 HTTP Version Not Supported: El servidor no soporta o no quiere soportar la versión del protocolo HTTP utilizada 
en la petición del navegador.
- 510 Not Extended: La petición del navegador debe añadir más extensiones para que el servidor pueda procesarla.
- 512 Not updated: Este error prácticamente es inexistente en la red, pero indica que el servidor está en una operación 
de actualizado y no puede tener conexión.
- 521 Version Mismatch: Este error sale cuando la versión no es compatible con tu hardware.

