# Created by bdob at 3/9/2021
# language: es

@VP-3
Característica: : Listar problemas reportados
  Como Administrador
  deseo visualizar los reportes de problemas o incidentes enviados por los ciudadanos
  para dar un seguimiento y tomar acción al respecto.


  Escenario: Seguimiento de problemas en estado "Pendiente"
    Dado que Isac tiene una cuenta de administrador
    Y existen reportes con estado "Pendiente"
    Cuando cambia el estado de un reporte "Pendiente" a "En proceso"
    Entonces Isac debe visualizar el mensaje "Estado modificado" en color verde

  Escenario: Seguimiento de problemas en estado "En Proceso"
    Dado que Isac tiene una cuenta de administrador
    Y existen reportes con estado "En Proceso"
    Cuando cambia el estado de un reporte "En Proceso" a "Finalizado"
    Entonces Isac debe visualizar el mensaje "Estado modificado" en color verde