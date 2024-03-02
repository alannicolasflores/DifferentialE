import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
df = pd.read_csv('optimization_results.csv')

# Analizar y graficar los resultados objetivos y las violaciones por generación
def analizar_graficar_resultados(df):
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))

    # Filtrar por tipo de dato para análisis
    df_comparacion = df[df['Tipo'] == 'Comparacion']
    df_actualizacion = df[df['Tipo'] == 'Actualizacion']
    df_trial_vector = df[df['Tipo'] == 'TrialVector']  # Asumiendo que tienes datos para el vector de prueba etiquetado como 'TrialVector'

    # Graficar resultados objetivos por generación
    ax[0].plot(df_comparacion['Generacion'], df_comparacion['Resultado'], 'r-', label='Comparacion')
    ax[0].plot(df_actualizacion['Generacion'], df_actualizacion['Resultado'], 'g-', label='Actualizacion')
    ax[0].plot(df_trial_vector['Generacion'], df_trial_vector['Resultado'], 'b-', label='Trial Vector')
    ax[0].set_xlabel('Generacion')
    ax[0].set_ylabel('Resultado')
    ax[0].set_title('Resultados Objetivos por Generacion')
    ax[0].legend()

    # Graficar violaciones por generación
    ax[1].plot(df_comparacion['Generacion'], df_comparacion['Violaciones'], 'r-', label='Comparacion')
    ax[1].plot(df_actualizacion['Generacion'], df_actualizacion['Violaciones'], 'g-', label='Actualizacion')
    ax[1].plot(df_trial_vector['Generacion'], df_trial_vector['Violaciones'], 'b-', label='Trial Vector')
    ax[1].set_xlabel('Generacion')
    ax[1].set_ylabel('Violaciones')
    ax[1].set_title('Violaciones por Generacion')
    ax[1].legend()

    plt.tight_layout()
    plt.show()

analizar_graficar_resultados(df)
