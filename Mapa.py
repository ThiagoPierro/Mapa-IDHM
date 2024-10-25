import pandas as pd
import plotly.express as px
import json

data = {
    'Região': ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste'],
    'IDHM 2010': [0.667, 0.663, 0.766, 0.754, 0.757],
    'Incremento (1991-2010)': [0.251, 0.276, 0.220, 0.242, 0.268]
}

df = pd.DataFrame(data)

estado_regiao = {
    'AC': 'Norte',
    'AL': 'Nordeste',
    'AM': 'Norte',
    'AP': 'Norte',
    'BA': 'Nordeste',
    'CE': 'Nordeste',
    'DF': 'Centro-Oeste',
    'ES': 'Sudeste',
    'GO': 'Centro-Oeste',  
    'MA': 'Nordeste',
    'MG': 'Sudeste',
    'MS': 'Centro-Oeste',
    'MT': 'Centro-Oeste',
    'PA': 'Norte',
    'PB': 'Nordeste',
    'PE': 'Nordeste',
    'PI': 'Nordeste',
    'RJ': 'Sudeste',
    'RN': 'Nordeste',
    'RO': 'Norte',
    'RR': 'Norte',
    'RS': 'Sul',
    'SC': 'Sul',
    'SE': 'Nordeste',
    'SP': 'Sudeste',
    'TO': 'Norte',
    'PR': 'Sul'

}

estados = pd.DataFrame({
    'Sigla': list(estado_regiao.keys()),
    'Região': list(estado_regiao.values())
})


merged_df = pd.merge(estados, df, on='Região', how='left')

mean_idhm = merged_df.groupby('Sigla')['IDHM 2010'].mean().reset_index()

geojson_file = r'D:\PythonProjects\venv\brazil_geo.json'
with open(geojson_file, encoding='utf-8') as f:
    geojson_data = json.load(f)

print("DataFrame:")
print(mean_idhm)
print("\nGeoJSON keys:")
print([feature['id'] for feature in geojson_data['features']])


fig = px.choropleth(
    mean_idhm,
    geojson=geojson_data,
    locations='Sigla',
    featureidkey="id",
    color='IDHM 2010',
    hover_name='Sigla',
    color_continuous_scale="Viridis",
    title="Mapa Coroplético do IDHM das Regiões do Brasil (2010)"
)

fig.update_geos(fitbounds="geojson", visible=False)
fig.update_layout(margin={"r": 0, "t": 30, "l": 0, "b": 0})

fig.show()
