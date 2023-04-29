import streamlit as st
import webbrowser


# Configuracoes
st.set_page_config(
    page_title="Educação - Mogi Open Data",
    layout = "wide",
    initial_sidebar_state="expanded"
)

st.title("Educação em Mogi Guaçu")

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

