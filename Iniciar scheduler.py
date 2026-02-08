# Iniciar scheduler (en terminal separado)
from sched import scheduler


airflow scheduler

# Iniciar webserver
airflow webserver --port 8080

# Ejecutar DAG manualmente
airflow dags unpause saludo_diario
airflow dags trigger saludo_diario
Ver resultados:

# Ver logs de ejecución
# Visitar http://localhost:8080 en navegador
# Ir a DAGs → saludo_diario → Graph View para ver flujo
# Ir a Tree View para ver historial de ejecuciones