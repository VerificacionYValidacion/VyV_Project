# Created by rivas at 17/8/2021
# language: es

Característica: Reporte de problemas o incidentes
  # Enter feature description here
  Como usuario
  deseo reportar un problema o incidente sucedido en mi ciudad especificando el lugar, el tipo de incidente y cualquier dato que me permita explicar el acontecimiento sucedido
  para que las autoridades locales se informe del problema o incidente y puedan tomar acciones al respecto.

  Esquema del escenario: Formulario de reporte de problemas o incidentes
    Dado que el señor Bryan tiene una sesión activa
    Cuando en la pantalla Inicio selecciona la opción de Reportar
    Y especifica lo siguiente: el "sector", "dirección","tipo","evidencia","descripción" del problema o incidente
    Y selecciona el botón "Enviar"
    Entonces estos datos deben ser guardados
    Y el señor Bryan debe visualizar el mensaje "Reporte enviado" en color verde
    Pero si el formulario está incompleto, el señor Bryan debe visualizar el mensaje "Debe llenar todos los campos" en color rojo

    Ejemplos:
      |  |  # Enter scenario name here
