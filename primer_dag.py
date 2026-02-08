# dags/mi_primer_dag.py

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Función de Python: Representa la lógica de negocio o procesamiento de datos
def saludar():
    # Resultado esperado en Logs: "¡Hola desde Airflow!"
    print("¡Hola desde Airflow!")
    return "Saludo completado"

# 1. DEFINICIÓN DEL DAG (Configuración del Orquestador)
dag = DAG(
    'saludo_diario',
    description='DAG que saluda cada día',
    schedule_interval=timedelta(days=1),  # El Scheduler lo activará cada 24 horas
    start_date=datetime(2024, 1, 1),      # Fecha de inicio histórica
    catchup=False,                        # Evita ejecutar de forma retroactiva desde 2024
    tags=['ejemplo', 'saludo']
)

# 2. DEFINICIÓN DE TAREAS

# Tarea 1: Uso de comandos del sistema operativo (Ubuntu/Bash)
tarea_bash = BashOperator(
    task_id='tarea_bash',
    bash_command='echo "Ejecutando tarea bash a las $(date)"',
    # RESULTADO ESPERADO: Imprime en consola la fecha actual del sistema.
    # Ejemplo: "Ejecutando tarea bash a las Dom Feb 8 16:05:00 -03 2026"
    dag=dag
)

# Tarea 2: Ejecución de lógica Python (donde iría el análisis de datos)
tarea_python = PythonOperator(
    task_id='tarea_python',
    python_callable=saludar,
    # RESULTADO ESPERADO: Ejecuta la función 'saludar'.
    # En la interfaz de Airflow, la tarea se marcará en verde (Success).
    dag=dag
)

# Tarea 3: Simulación de tiempo de espera o delay de proceso
tarea_esperar = BashOperator(
    task_id='tarea_esperar',
    bash_command='sleep 5',
    # RESULTADO ESPERADO: El DAG se mantendrá en estado 'Running' por 5 segundos exactos
    # antes de finalizar con éxito.
    dag=dag
)

# 3. ORQUESTACIÓN (Flujo de trabajo)
# Establece la dependencia: No se puede saludar sin antes haber ejecutado el comando Bash,
# y no se puede terminar el proceso sin esperar los 5 segundos.
tarea_bash >> tarea_python >> tarea_esperar

# NOTA TÉCNICA DE AMBIENTE (2026):
# Este código fue diseñado para Python 3.12/3.14. 
# El flujo lógico es correcto, pero la ejecución depende de la activación 
# del Scheduler en el entorno virtual (venv) de Ubuntu (WSL).