# Created by bdob at 21/9/2021
# language: es
@VP9
Característica: Filtrar reportes
  Como Administrador
  deseo filtrar todos los reportes de problemas por categoría, estado y sector
  para priorizar problemas y dar un seguimiento eficiente de cada reporte.

  Escenario: : Filtrar reportes por categoría
    Dado que Isac tiene una cuenta de administrador
    Y existen reportes listados
    Cuando selecciona una categoría para filtrar
    Entonces la tabla solo debe mostrar reportes de esa categoría para priorizarlos acorde a sus preferencias

  Escenario: : Filtrar reportes por estado
    Dado que Isac tiene una cuenta de administrador
    Y existen reportes listados
    Cuando selecciona un estado para filtrar
    Entonces la tabla solo debe mostrar reportes con ese estado para priorizarlos acorde a sus preferencias

  Escenario: : Filtrar reportes por sector
    Dado que Isac tiene una cuenta de administrador
    Y existen reportes listados
    Cuando selecciona un sector para filtrar
    Entonces la tabla solo debe mostrar reportes con de ese sector para priorizarlos acorde a sus preferencias