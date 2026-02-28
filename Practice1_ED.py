#Practice 1
import pandas as pd
import matplotlib.pyplot as plt    #Librerias usadas
import os

# Load the data
script_dir = os.path.dirname(os.path.abspath(__file__))  # obtiene la ruta de la carpeta del script
# se leen los archivos CSV y se convierten en una tabla de pandas para poder usarse
exp1 = pd.read_csv(os.path.join(script_dir, "temp_356218_primer_experimento.csv"))
exp2 = pd.read_csv(os.path.join(script_dir, "temp_539439_segundo_experimento.csv"))


#STATISTICS
def get_stats(df, t_start, t_end):
    #toma solo las temperaturas en el rango de tiempo indicado
    data = df[(df["time_seconds"] >= t_start) & (df["time_seconds"] <= t_end)]["temperature_C"]
    # medidas estadisticas a calcular usando funciones de pandas
    datapoints= len(data)
    mean     = data.mean()
    variance = data.var(ddof=1)
    minimum  = data.min()
    maximum  = data.max()
    range_   = maximum - minimum
    return datapoints, mean, variance, minimum, maximum, range_


print("\nFirst experiment")

datapoints, mean, variance, mn, mx, rng = get_stats(exp1, 14.027, 61.110) #segundos en los cuales la temperatura se estabiliza
print("\nPhase ice cubes and water")
print(f"Number of data points: {datapoints}")
print(f"Mean: {round(mean, 4)}")
print(f"Variance: {round(variance, 4)}")
print(f"Range: {mn} to {mx} = {round(rng, 4)}")

datapoints,mean, variance, mn, mx, rng = get_stats(exp1, 83.148, 119.214) # segundos en la cual la temperatura se estabiliza
print("\nPhase boiling water")
print(f"Number of data points: {datapoints}")
print(f"Mean: {round(mean, 4)}")
print(f"Variance: {round(variance, 4)}")
print(f"Range: {mn} to {mx} = {round(rng, 4)}")

datapoints, mean, variance, mn, mx, rng = get_stats(exp1, 150.268, 180.0)  # segundos en la cual la temperatura se estabiliza
print("\nPhase environmental temperature")
print(f"Number of data points: {datapoints}")
print(f"Mean: {round(mean, 4)}")
print(f"Variance: {round(variance, 4)}")
print(f"Range: {mn} to {mx} = {round(rng, 4)}")


print("\n\nSecond experiment")

datapoints, mean, variance, mn, mx, rng = get_stats(exp2, 7.014, 61.110)  # segundos en la cual la temperatura se estabiliza
print("\nPhase hot water")
print(f"Number of data points: {datapoints}")
print(f"Mean: {round(mean, 4)}")
print(f"Variance: {round(variance, 4)}")
print(f"Range: {mn} to {mx} = {round(rng, 4)}")

datapoints, mean, variance, mn, mx, rng = get_stats(exp2, 69.124, 119.213)  # segundos en la cual la temperatura se estabiliza
print("\nPhase hot water + cold water")
print(f"Number of data points: {datapoints}")
print(f"Mean: {round(mean, 4)}")
print(f"Variance: {round(variance, 4)}")
print(f"Range: {mn} to {mx} = {round(rng, 4)}")

datapoints, mean, variance, mn, mx, rng = get_stats(exp2, 130.233, 180.0)  # segundos en la cual la temperatura se estabiliza
print("\nPhase hot water + cold water + hot water")
print(f"Number of data points: {datapoints}")
print(f"Mean: {round(mean, 4)}")
print(f"Variance: {round(variance, 4)}")
print(f"Range: {mn} to {mx} = {round(rng, 4)}")

print()


# GRAPH 1 – EXPERIMENT 1

fig1, ax1 = plt.subplots(figsize=(13, 6))

ax1.plot(exp1["time_seconds"], exp1["temperature_C"], color="blue", linewidth=1.5)

change_points_exp1 = [
    (0.001,   13.25, "Start\n(Ice Water)"),
    (60.109,   4.50, "Change to\nBoiling Water"),   #Momentos en los cuales se visualiza el cambio de fase
    (118.212, 92.50, "Change to\nRoom Temp"),
]

for t, temp, label in change_points_exp1:
    ax1.axvline(x=t, color="orange", linewidth=1.2, linestyle="--")
    ax1.scatter(t, temp, color="orange", zorder=5, s=70)
    offset_x = t - 30 if t > 100 else t + 2
    offset_y = temp - 12 if t > 100 else temp + 4
    ax1.annotate(label, xy=(t, temp), xytext=(offset_x, offset_y),
                 fontsize=8, color="black",
                 arrowprops=dict(arrowstyle="->", color="orange"))

ax1.set_title("Experiment 1 – Temperature over Time\n")
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("Temperature (°C)")
ax1.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
fig1.savefig(os.path.join(script_dir, "experiment1_plot.png"), dpi=150)


# GRAPH 2 – EXPERIMENT 2

fig2, ax2 = plt.subplots(figsize=(13, 6))

ax2.plot(exp2["time_seconds"], exp2["temperature_C"], color="red", linewidth=1.5)

change_points_exp2 = [
    (0.001,   41.00, "Start\n(Hot Water)"),
    (60.108,  67.75, "Change:\nHot + Cold Water"),         #Momentos en los cuales se visualiza el cambio de fase
    (118.211, 38.25, "Change:\nHot+Cold+Hot Water"),
]

for t, temp, label in change_points_exp2:
    ax2.axvline(x=t, color="orange", linewidth=1.2, linestyle="--")
    ax2.scatter(t, temp, color="orange", zorder=5, s=70)
    ax2.annotate(label, xy=(t, temp), xytext=(t + 2, temp + 2),
                 fontsize=8, color="black",
                 arrowprops=dict(arrowstyle="->", color="orange"))

ax2.set_title("Experiment 2 – Temperature over Time\n")
ax2.set_xlabel("Time (seconds)")
ax2.set_ylabel("Temperature (°C)")
ax2.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
fig2.savefig(os.path.join(script_dir, "experiment2_plot.png"), dpi=150)

plt.show()