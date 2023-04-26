import streamlit as st
import pandas as pd
import pydeck as pdk
from streamlit_extras.switch_page_button import switch_page

# ######################################
#     CARREGANDO DADOS
# ######################################

# Variaveis predefinidas
dict_color_categoria_escola = {
    "Municipal": [153, 237, 204],
    "Estadual": [183, 195, 243],
    "Particular": [241, 81, 82]
}
dict_raio_abrangencia = {
    'Péssimo': 1000,
    'Regular': 525,
    'Excelente': 250
}

def carrega_dados():
    # Carrega dados escolas municipais - df_mun
    # Carrega dados escolas estaduais - df_est
    # Carrega dados escolas particulares - df_part

    # Carrega dados
    url_mun = "./data/tabela_escolas municipais.xlsx"
    url_est = "./data/tabela_escolas estaduais.xlsx"
    url_part = "./data/tabela_escolas particulares.xlsx"
    df_mun = pd.read_excel(url_mun)
    df_est = pd.read_excel(url_est)
    df_part = pd.read_excel(url_part)

    # Preprocess 1 - Add coluna tipo de escolas (municipal, estadual, particular)
    df_mun['Categoria'] = 'Municipal'
    df_est['Categoria'] = 'Estadual'
    df_part['Categoria'] = 'Particular'
    # Preprocess 2 - Concat all data in one dataframe
    df_escolas = pd.concat([df_mun, df_est, df_part], ignore_index=True)
    # Preprocess 3 - Add color column
    df_escolas['cor_categoria'] = df_escolas['Categoria'].map(dict_color_categoria_escola)
    
    return df_mun, df_est, df_part, df_escolas

# Dataframes
df_mun, df_est, df_part, df_escolas = carrega_dados()
# Etapas para filtro
list_etapas = df_escolas.etapa.unique()


# ######################################
# Título e introdução

btn_volta_inicio = st.button(
    label="Voltar ao início",
    type="secondary"
)
if btn_volta_inicio:
    switch_page("Início")


st.title(":world_map: Localização das Escolas")
st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
# ######################################



# ######################################
# Filtros de escolas e raios

st.caption("Filtros")

col1, col2, col3 = st.columns(3)

# Filtro de ensino fundamental, medio
with col1:
    st.markdown("**Filtro de categoria de ensino**")
    filtro_ei = st.checkbox("Ensino Infantil", value=True)
    filtro_ef = st.checkbox("Ensino Fundamental", value=True)
    filtro_em = st.checkbox("Ensino Médio", value=True)
    filtro_eja = st.checkbox("Ensino de Jovens e Adultos", value=True)
    st.caption("(Ainda não funciona)")

# Filtro de categoria escola
with col3:
    st.markdown("**Filtro Categoria de escola**")
    filtro_mun = st.checkbox("Escolas Municipais", value=True)
    filtro_est = st.checkbox("Escolas Estaduais", value=True)
    filtro_part = st.checkbox("Escolas Particulares", value=True)

# Filtro de raio
with col2:
    st.markdown("**Filtro raio**")
    raio_abrangencia = st.radio(
        label="Raio",
        options=('Péssimo', 'Regular', 'Excelente')
    )

# Filtro de etapa



# ######################################
#        MAPA
# ######################################
# Obtem o dataframe filtrado
df_escolas_mapa = df_escolas if filtro_mun else df_escolas[df_escolas['Categoria'] != 'Municipal']
df_escolas_mapa = df_escolas_mapa if filtro_est else df_escolas_mapa[df_escolas_mapa['Categoria'] != 'Estadual']
df_escolas_mapa = df_escolas_mapa if filtro_part else df_escolas_mapa[df_escolas_mapa['Categoria'] != 'Particular']
# Define a layer to display on a map
layer_escolas = pdk.Layer(
    "ScatterplotLayer",
    df_escolas_mapa,
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    radius_scale=50,
    radius_min_pixels=1,
    radius_max_pixels=50,
    line_width_min_pixels=1,
    get_position="[long, lat]",
    get_fill_color="cor_categoria",
    get_line_color=[0, 0, 0],
)
layer_raio_abrangencia = pdk.Layer(
    "ScatterplotLayer",
    df_escolas_mapa,
    pickable=False,
    opacity=0.005,
    stroked=False,
    filled=True,
    radius_scale=dict_raio_abrangencia[raio_abrangencia],
    line_width_min_pixels=1,
    get_position="[long, lat]",
    get_fill_color="cor_categoria",
    get_line_color="cor_categoria"
)
# Set the viewport location
view_state = pdk.ViewState(latitude=-22.385131, longitude=-46.948222, zoom=13, bearing=0, pitch=0)
# Define tooltip
tooltip = {
    "html": "<b>Nome:</b> {escola} <br> <i>{Categoria}</i> <br> {porte} <br> {etapa}",
    "style": {
    "background": "#f4f4f4",
    "color": "#311f89",
    "border-radius": "10px"
    },
}
# Render
map_pydeck = pdk.Deck(
    map_style=None,
    layers=[layer_escolas, layer_raio_abrangencia],
    initial_view_state=view_state,
    tooltip=tooltip
    )
st.pydeck_chart(map_pydeck)
# ######################################

st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")

# ######################################
# Relação Alunos Matriculados
st.markdown("# Relação Alunos matriculados com densidade populacional")
st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")

st.info("Em desenvolvimento", icon="🤖")

df_escolas
