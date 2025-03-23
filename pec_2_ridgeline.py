import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import joypy
from matplotlib import cm
from matplotlib.patches import Patch
import os

# Descargamos el dataset desde Kaggle
path = kagglehub.dataset_download("uciml/red-wine-quality-cortez-et-al-2009")

# Definimos la ruta del archivo CSV
csv_path = os.path.join(path, "winequality-red.csv")

# Cargamos el dataset 
df = pd.read_csv(csv_path, sep=',')

# Configuramos el estilo de la visualización
plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 18,
    'axes.edgecolor': 'gray',
    'axes.linewidth': 0.8
})

# Definimos el colormap para una buena visualización del degradado
cmap = cm.get_cmap('plasma', df['quality'].nunique())

# Creamos el Ridgeline Chart agrupando por calidad del vino (quality)
fig, axes = joypy.joyplot(
    data=df,
    by='quality',
    column='alcohol',
    figsize=(14, 9),
    colormap=cmap,
    linewidth=1,
    fade=True,
    alpha=0.9,
    grid=True
)

# Añadimos el título y la etiquetas del eje X
plt.title('Alcohol Content Distribution by Red Wine Quality Score', fontsize=18, weight='bold', pad=30)
plt.xlabel('Alcohol (%)', fontsize=14)

qualities = sorted(df['quality'].unique())

# Creamos la leyenda con cada nivel de calidad
handles = [
    Patch(color=cmap(i / len(qualities)), label=f'Quality "{q}"')
    for i, q in enumerate(sorted(df['quality'].unique()))
]
plt.legend(handles=handles, title='Quality Scores', loc='upper left', bbox_to_anchor=(1, 1))

# Ajustamos el grid y los márgenes
for ax in axes:
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)

plt.tight_layout()

# Mostramos el gráfico
plt.show()
