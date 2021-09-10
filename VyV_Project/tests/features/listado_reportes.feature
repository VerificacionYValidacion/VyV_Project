# Created by bdob at 3/9/2021
# language: es

@VP-3
Característica: : Listar problemas reportados
  Como Administrador
  deseo visualizar los reportes de problemas o incidentes enviados por los ciudadanos
  para dar un seguimiento y tomar acción al respecto.

  #Seguimiento de problemas en estado "pendiente"
  Escenario: Seguimiento de problemas reportados
    Dado que Isac tiene una cuenta de administrador
    Y existen reportes con estado pendiente
    Cuando ingresa en la sección de "Reportes"
    #Entonces el nuevo estado será "en proceso"
    Entonces puede cambiar el estado de un reporte de la lista para darle seguimiento

  #Seguimiento de problemas en estado "en proceso"
  Escenario: Seguimiento de problemas reportados
    Dado que Isac tiene una cuenta de administrador
    Cuando ingresa en la sección de "Reportes"
    #Entonces el nuevo estado será "finalizado"
    Entonces puede cambiar el estado de un reporte de la lista para darle seguimiento