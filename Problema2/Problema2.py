import os
import math
import pandas as pd

ruta = os.path.join(os.path.dirname(__file__), "velocidad_internet_ucu")
df = pd.read_csv(ruta)

print("Edificios disponibles en el dataset:")
print(df["Edificio"].unique())

# Filtro Edicicios central y semprun (Aca tengo todas las velocidades para los edicicions central y semprun)
df_filtrado = df[df["Edificio"].isin(["Central", "Semprún"])]

# Separar por edificio
df_central = df[df["Edificio"] == "Central"]
df_semprun = df[df["Edificio"] == "Semprún"]

# Calcular estadísticos para Central
media_central = df_central["Velocidad Mb/s"].mean() #Calcula el promedio de los valores de la columna "Velocidad Mb/s" para el edificio Central
std_central = df_central["Velocidad Mb/s"].std() #Calcula el desvío estándar muestral (σ estimado) de la columna.
n_central = len(df_central)

# Calcular estadísticos para Semprún
media_semprun = df_semprun["Velocidad Mb/s"].mean() #Calcula el promedio de los valores de la columna "Velocidad Mb/s" para el edificio Semprún
std_semprun = df_semprun["Velocidad Mb/s"].std() #Calcula el desvío estándar muestral (σ estimado) de la columna.
n_semprun = len(df_semprun)

# Mostrar resultados
print("Estadísticos descriptivos de velocidad por edificio:\n")

print(f"Central:")
print(f"  Media: {media_central:.2f} Mb/s")
print(f"  Desvío estándar: {std_central:.2f} Mb/s")
print(f"  Cantidad de mediciones: {n_central}")

print(f"\nSemprún:")
print(f"  Media: {media_semprun:.2f} Mb/s")
print(f"  Desvío estándar: {std_semprun:.2f} Mb/s")
print(f"  Cantidad de mediciones: {n_semprun}")

# H₀: μ₁ = μ₂ → las medias son iguales (no hay diferencia)
# H₁: μ₁ < μ₂ → la media en Central es menor (test unilateral a la izquierda)

#Formula t:

#Numerador:
numerador = media_central - media_semprun
# Denominador (error estándar combinado)
denominador = math.sqrt((std_central**2 / n_central) + (std_semprun**2 / n_semprun))

# Estadístico t
t = numerador / denominador

print(f"\nEstadístico t: {t:.4f}")

