# Created by bdob at 3/9/2021
# language: es

@VP-3
Característica: : Listar problemas reportados
  Como Administrador
  deseo visualizar los reportes de problemas o incidentes enviados por los ciudadanos
  para dar un seguimiento y tomar acción al respecto.


  Escenario: Seguimiento de problemas en estado "pendiente"
    Dado que Isac tiene una cuenta de administrador
    Y existen reportes con estado "pendiente"
    Cuando cambia el estado de un reporte "pendiente" a "en proceso"
    Entonces el nuevo estado del reporte será "en proceso"

  Escenario: Seguimiento de problemas en estado "en proceso"
    Dado que Isac tiene una cuenta de administrador
    Y existen reportes con estado "en proceso"
    Cuando cambia el estado de un reporte "en proceso" a "finalizado"
    Entonces el nuevo estado del reporte será "finalizado"