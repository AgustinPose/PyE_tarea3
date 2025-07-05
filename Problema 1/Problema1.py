
import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("./Problema 1/muestra_ech.csv")

# -----------------------------------------------
# Punto 1: Calcular ingreso per cápita
# -----------------------------------------------
df["ingreso_pc"] = df["ingreso"] / df["personas_hogar"]

# -----------------------------------------------
# Punto 2: Clasificar hogares en quintiles
# -----------------------------------------------
df["quintil"] = pd.qcut(df["ingreso_pc"], 5, labels=[1, 2, 3, 4, 5])

# -----------------------------------------------
# Punto 3: Filtrar los hogares del quintil superior
# -----------------------------------------------
df_quintil_superior = df[df["quintil"] == 5]

# -----------------------------------------------
# Punto 4: Tabla de frecuencias observadas por departamento
# -----------------------------------------------
frecuencias_observadas = df_quintil_superior["departamento"].value_counts().sort_index()
frecuencias_df = frecuencias_observadas.reset_index()
frecuencias_df.columns = ["Departamento", "Frecuencia Observada"]

# Mostrar resultados
print("Primeras filas del dataset original:")
print(df.head().to_string(index=False))

print("\nCantidad de hogares por quintil:")
print(df["quintil"].value_counts().sort_index().to_string(index=False))

print("\nFrecuencias observadas en el quintil superior (20% más rico) por departamento:")
print(frecuencias_df.to_string(index=False))
