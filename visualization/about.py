import streamlit as st
from utils import get_image_as_base64


def render_about():

    st.title('🔍 Ola seja bem vindo ao projeto de detecção de fraudes!')

    

    img_about = get_image_as_base64("assets/FC_IMAGE.png")

    st.markdown(f"""
    <div style="margin-top: 100px;"></div>
    <img src="data:image/png;base64,{img_about}">
    """, unsafe_allow_html=True
    )

    st.markdown("""
        <div style="margin-top: 100px;"></div>

        ### O que você verá neste projeto 🚀:
        
        <br>

        📊 **Dashboard:** Relatório desenvolvido a partir da análise exploratória dos dados. (Menu lateral &gt;)
        
        📓 **Notebook:** Contexto completo da análise de dados, contendo o modelo de ML utilizado para treinamento e medição da acurácia. (Menu lateral &gt;)
        
        ⚙️ **Simulador de compras:** "Em desenvolvimento"
        
        **(Navegue até o menu lateral esquerdo para ver os componentes do projeto 🚀)**
               

""", unsafe_allow_html=True),
                


    st.markdown("""
    <div style="margin-top: 100px;"></div>
                   
    #### Origem dos dados:
                
    <br>
    Este dataset simulado contém transações de cartão de crédito, tanto legítimas quanto fraudulentas, registradas entre 1º de janeiro de 2019 e 31 de dezembro de 2020. Ele abrange transações realizadas por 1.000 clientes em uma rede de 800 estabelecimentos comerciais.
    Os dados foram gerados utilizando a ferramenta Sparkov Data Generation, disponível no GitHub, criada por Brandon Harris. A simulação foi executada para o período de 1º de janeiro de 2019 a 31 de dezembro de 2020, e os arquivos resultantes foram combinados e convertidos para um formato padrão.
    
    <br>
    <br>
                
    #### Como a Simulação Funciona:
                
    
    O simulador utiliza uma lista predefinida de comerciantes, clientes e categorias de transação. Com o auxílio da biblioteca Faker, os dados são gerados com base em perfis específicos, como "adultos do sexo feminino, entre 25 e 50 anos, residentes em áreas rurais". Cada perfil possui parâmetros definidos, como número mínimo e máximo de transações diárias, distribuição ao longo da semana e propriedades estatísticas para os valores das transações. A partir dessas distribuições, os dados são simulados de forma realista.
    Neste dataset, foram geradas transações para todos os perfis disponíveis, criando um conjunto de dados mais representativo e diversificado.
    
    <br>
    <br>       
                   
    #### Créditos:
            
    <br>       
    Agradecimento especial a Brandon Harris pelo excelente trabalho na criação do Sparkov Data Generation, que facilitou a construção deste dataset de transações fraudulentas.
                
   link: [Brandon Harris_repositirio](https://github.com/namebrandon/Sparkov_Data_Generation/tree/master)
    
""", unsafe_allow_html=True)