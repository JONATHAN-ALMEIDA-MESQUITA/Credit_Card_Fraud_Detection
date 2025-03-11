import streamlit as st
import streamlit.components.v1 as components

def render_notebook():
    # Caminho para o arquivo HTML gerado
    html_file = "C:/Users/User/OneDrive/projetos_dados/ciencia__de_dados/5 - credit_card_fraud_detection/visualization/assets/Credit_Card_Fraud_Detection.html"

    try:
        # Ler o conteúdo do arquivo HTML
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Renderizar o HTML no Streamlit
        components.html(html_content, height=800, scrolling=True)
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {html_file}")
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
