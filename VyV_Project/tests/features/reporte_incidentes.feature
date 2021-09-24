# Created by rivas at 17/8/2021
# language: es

@VP-2
Característica: Reportar problemas
  # Enter feature description here
  Como usuario
  deseo reportar un problema sucedido en mi ciudad especificando el lugar, el tipo de incidente
  y cualquier dato que me permita explicar el acontecimiento sucedido
  para que las autoridades locales se informe del problema o incidente y puedan tomar acciones al respecto.

  Escenario: Reportar un problema
    Dado que el señor Bryan tiene una sesión activa en la pantalla de Reportar
    Cuando reporta un problema con: el "sector", "dirección","categoría","evidencia","descripción" del problema
    Entonces el señor Bryan debe visualizar el mensaje "Reporte enviado" en color verde

