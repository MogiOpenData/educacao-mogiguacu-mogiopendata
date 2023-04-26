import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page
import webbrowser


# Configuracoes
st.set_page_config(
    page_title="Educação - Mogi Open Data",
    layout = "wide",
    initial_sidebar_state="expanded"
)

st.title("Educação em Mogi Guaçu")

add_vertical_space(5)
st.markdown("### Páginas:")
col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    btn_pag_mogiod = st.button(
        label='Mogi Open Data',
        help="Abre a página inicial da Mogi Open Data",
        type="secondary"
    )

    if btn_pag_mogiod:
        webbrowser.open_new_tab("https://mogiopendata.com.br")

with col2:
    btn_pag_localizacao = st.button(
        label="Localização Escolas",
        help="Abre a página 'Localização Escolas'",
        type="secondary"
    )

    if btn_pag_localizacao:
        switch_page("localização escolas")

