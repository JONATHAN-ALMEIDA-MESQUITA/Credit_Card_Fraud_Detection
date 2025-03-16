import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px



@st.cache_data
def render_relatorio():

    st.title('📊 Relatorio: Analise exploratoria detecção de fraudes!')

    # Carregando os dados
    df = pd.read_csv("assets/fraudTest.csv", index_col="Unnamed: 0")
    
    # Agrupando os dados por categoria
    df_cat = df.groupby('category').agg(
        qtd_trans=('trans_num', 'count'),
        qtd_fraud=('is_fraud', 'sum'),
        mean_fraud=('is_fraud', lambda x: (x.mean() * 100).round(2)),
        ttl_gasto=('amt', 'sum')
    ).reset_index().sort_values(by=['mean_fraud', 'qtd_fraud'], ascending=False)
    
    # Criando o gráfico
    fig = go.Figure()

    # Adicionando barras para a quantidade de transações
    fig.add_trace(go.Bar(
        x=df_cat['category'],
        y=df_cat['qtd_trans'],
        name='Quantidade de Transações', 
        marker_color='lemonchiffon',
        text=df_cat['qtd_trans'].apply(lambda x: f'{x/1000:.0f}k'),
        textposition='auto'
    ))

    # Adicionando linha para a média de fraudes (%)
    fig.add_trace(go.Scatter(
        x=df_cat['category'],
        y=df_cat['mean_fraud'],
        name='Média de Fraudes (%)',
        mode='lines+markers',
        yaxis='y2',  # Define para o eixo secundário
        marker=dict(color='deepskyblue', size=8),
        line=dict(color='deepskyblue', width=2)
    ))

    # Ajustando o layout
    fig.update_layout(
        title='Incidência de Fraudes por Categoria',
        xaxis_title='Categoria',
        yaxis=dict(title='Quantidade de Transações', side='left', showgrid=False),
        yaxis2=dict(
            title='Média de Fraudes (%)',
            overlaying='y',  # Sobrepõe ao eixo y principal
            side='right',
            showgrid=False
        ),
        template='plotly_dark',
        legend=dict(
            x=0.6, 
            y=1.1,
            orientation='h'  # Posiciona a legenda horizontalmente
        )
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("##### 📌 Conclusão Fraude por Categoria de Compras:", expanded=False):

        st.markdown("""
        

        - Ao analisar as **categorias**, observa-se que **compras online** (`shopping_net` e `misc_net`) possuem as **maiores taxas de fraude**:  
        - 🛒 **Shopping_net:** **1,21%** **(Linha azul do grafico)** 
        - 💳 **Misc_net:** **0,98%**  **(Linha azul do grafico)** 
        - Isso sugere que **transações online podem estar mais suscetíveis a fraudes**, possivelmente devido à **falta de verificação presencial** ou ao uso de **métodos de pagamento menos seguros**.  

        - Além disso, **compras em mercados físicos** (`grocery_pos`) também apresentam uma **alta incidência de fraudes**:  
        - 🏪 **Grocery_pos:** **53k devendas** e uma taxa de **0,92%** de fraudes.  
        - Isso pode estar relacionado ao **alto volume de transações** nessa categoria ou a **vulnerabilidades específicas no processo de pagamento**.  

        - Por outro lado, categorias como **`home`**, **`kids_pets`** e **`personal_care`** têm as **menores taxas de fraude**, indicando que **esses setores podem ser mais seguros ou menos visados por fraudadores**.  

        💡 **Essa análise destaca a importância de reforçar medidas de segurança, especialmente em transações online e em mercados físicos, para reduzir a incidência de fraudes.**  

        """)


    #Analise por pessoas

    df_gender = df.groupby('gender').agg(
        qtd_trans = ('trans_num', 'count'),
        qtd_fraud = ('is_fraud', 'sum'),
        mean_fraud = ('is_fraud', lambda x: (x.mean()*100).round(2))
        ).assign(
        prop_trans= lambda x : (x['qtd_trans'] / x['qtd_trans'].sum()*100).round(2),
        prop_fraud= lambda x : (x['mean_fraud'] / x['mean_fraud'].sum()*100).round(2)
        ).reset_index()

        #Grafico de proporção de fraud entre genero

    fig = make_subplots(rows=1, cols=3, subplot_titles=('Quantidade de transações por genero', 'Quantidade de fraudes por genero', 'Quantidade de transações'))



    fig.add_trace(go.Bar(
        x=df_gender['gender'],
        y=df_gender['qtd_trans'],
        name='Média de fraudes(%)', 
        marker_color='lemonchiffon', 
        text=df_gender['qtd_trans'].apply(lambda x : f'{x/1000: .0f}k'),
        textposition='auto'), row=1, col=1)


    fig.add_trace(go.Bar(
        x=df_gender['gender'],
        y=df_gender['qtd_fraud'], 
        name='Quatidade de fraudes',
        marker_color='lightblue',
        text=df_gender['qtd_fraud'].apply(lambda x : f'{x:,}'.replace(',',".")),
        textposition='auto'), row=1, col=2)



    fig.add_trace(go.Bar(
        x=df_gender['gender'],
        y=df_gender['mean_fraud'],
        name='Média de fraudes(%)', 
        marker_color='lightcoral', 
        text=df_gender['mean_fraud'].apply(lambda x : f'{x: .2f}%'),
        textposition='auto'), row=1, col=3)


    # Ajustando o layout
    fig.update_layout(
        template='plotly_dark',
        showlegend=True, 
        legend=dict(
            x=0.3,
            y=-0.3,
            orientation='h'       
        ))

    #Atualizar titulo dos eixos
    fig.update_xaxes(title_text = 'Genero', row=1 ,col=1)
    fig.update_yaxes(title_text = 'Média', row=1 ,col=1)
    fig.update_xaxes(title_text = 'Genero', row=1 ,col=2)
    fig.update_yaxes(title_text = 'Quantidade', row=1 ,col=2)
    fig.update_xaxes(title_text = 'Genero', row=1 ,col=3)
    fig.update_yaxes(title_text = 'Quantidade', row=1 ,col=3)


    st.plotly_chart(fig, use_container_width=True)

    with st.expander("##### 📌 Conclusão Comparação por Gênero :", expanded=False):

        st.markdown("""

        - O número total de transações de pessoas do gênero **F** (**305k**) é **maior** que o de pessoas do gênero **M** (**251k**).  
        - A quantidade **absoluta** de fraudes para **F** (**1.164**) também é maior do que para **M** (**981**).  

        - No entanto, a **média de fraudes** (ou taxa de fraude) é praticamente a mesma para ambos os grupos:  
        - **0,38% para F**  
        - **0,39% para M**  

        **🔍 Como interpretar isso?**  

        > A taxa de fraude sendo parecida indica que a **probabilidade de uma transação ser fraudulenta** não varia muito entre os gêneros.  
        > O fato de **F** ter mais fraudes absolutas ocorre simplesmente porque **há mais transações desse grupo**. 
    
        """)


    #Converter a coluna de data e hore em datetime
    df['trans_date_trans_time'] = pd.to_datetime(df['trans_date_trans_time'])
    #Extrair hora formatada em H:M:S usanto strftime
    df['hour'] = df['trans_date_trans_time'].dt.strftime('%H:%M:%S')
    df['only_hour'] = df['trans_date_trans_time'].dt.strftime('%H')

    df_hour = df.groupby('only_hour').agg(
    qtd_fraud = ('is_fraud', 'sum'),
    mean_fraud = ('is_fraud', lambda x: (x.mean()*100).round(2))
    ).reset_index().sort_values(by='mean_fraud', ascending=False)


    # Criando o gráfico
    fig = go.Figure()

    # Adicionando as barras
    fig.add_trace(go.Bar(
        x=df_hour['only_hour'], 
        y=df_hour['qtd_fraud'], 
        name='Quantidade de Fraudess',
        marker_color='lemonchiffon',
        text=df_hour['qtd_fraud'],
        textposition='auto'
    ))

    # Ajustando o layout
    fig.update_layout(
        title='Distribuição de Fraudess por Hora',
        title_x = 0.5,
        xaxis_title='Hora',
        yaxis_title='Quantidade de Fraudess',
        template='plotly_dark'
    )

    # Exibindo o gráfico
    st.plotly_chart(fig, use_container_width=True)


    with st.expander("##### 📌 Conclusão Pico de fraudes (hora)", expanded=False):

        st.markdown("""

        **🔴 Pico de fraudes entre 22h e 23h:**  

        - O maior índice de transações fraudulentas ocorre entre **22h e 23h**, com **550 e 538 fraudes**, respectivamente.  
        - Isso indica um **período crítico** onde as fraudes são mais frequentes.  

        **📉 Redução nas primeiras horas da madrugada:**  

        - Entre **00h e 03h**, há uma redução significativa (**cerca de 65%**) no número de fraudes em comparação com o pico das **22h-23h**.  
        - Isso sugere que, embora ainda haja uma incidência alta de fraudes nesse período, ela é **menor** do que no pico inicial.  

        **🟢 Períodos de menor incidência:**  

        - Das **04h às 21h**, a quantidade de fraudes é significativamente **menor**, com valores abaixo de **40 fraudes por hora**.  
        - Isso indica que esses horários são **menos críticos**.  

        **🔐 Ações de segurança:**  

        - Aumentar os **critérios de segurança** durante os horários de pico (**22h-23h**) e nas primeiras horas da madrugada (**00h-03h**).  
        - Isso pode incluir **verificação adicional de transações, autenticação de dois fatores ou monitoramento mais rigoroso**.  

        **📊 Uso da variável para treinamento do modelo:**  

        - A variável **`only_hour`** parece ter uma **alta correlação** com a ocorrência de fraudes, o que a torna uma **feature relevante** para o modelo de classificação.  
        - Incluir essa variável pode **melhorar a precisão** do modelo ao prever transações fraudulentas.    
        dulentas.


        """)

    
    df['day'] = df['trans_date_trans_time'].dt.day_name()
    df_heatmap = df.groupby(['only_hour', 'day']).agg(
        qtd_fraud=('is_fraud', 'sum') 
    ).reset_index().sort_values(by= 'qtd_fraud', ascending=False)

    fig = px.density_heatmap(
        df_heatmap,
        x='only_hour', 
        y='day',  
        z='qtd_fraud',  
        title='Mapa de Calor de Fraudes por Hora e Dia da Semana',
        labels={'only_hour': 'Hora', 'day': 'Dia da Semana', 'qtd_fraud': 'Quantidade de Fraudes'},
        color_continuous_scale='agsunset', 
        text_auto=True 
    )

    # Ajustando o layout
    fig.update_layout(
        xaxis_title='Hora',
        yaxis_title='Dia da Semana',
        template='plotly_dark'
    )

    st.plotly_chart(fig, use_container_width=True)


    with st.expander('##### 📌Conclusão dia com maior numero de fraudes', expanded=False):

        st.markdown("""


        O domingo apresenta o maior pico de fraudes, com **105 fraudes às 22h** e **101 fraudes às 23h**.  

        Outros dias da semana também mostram picos significativos, especialmente:  

        - **Quinta-feira (Thursday):** 78 fraudes às 22h e 82 fraudes às 23h.  
        - **Terça-feira (Tuesday):** 89 fraudes às 22h e 73 fraudes às   

        ---

        **📊 Impacto do Dia da Semana**  

        Embora o **domingo** tenha o maior número absoluto de fraudes, os outros dias da semana também apresentam picos consistentes, especialmente entre **22h e 23h**.  

        📍 Isso sugere que **o horário tem um impacto mais significativo do que o dia emana**.  

        ---

        **⏰ Horários de Pico**  

        - Os horários entre **22h e 23h** são consistentemente os mais críticos em todos os dias da semana, com uma média de **70 a 100 fraudes** nesse período.  
        - Fora desse horário, a quantidade de fraudes **cai drasticamente**, com a maioria dos dias registrando menos de **10 des por hora**.  

        ---

        **✅ Recomendações**  

        ✔️ **Reforçar a segurança** durante os horários de pico (**22h-23h**) em todos os dias da semana.  
        ✔️ **Monitorar especialmente o domingo**, que apresenta os maiores picos de fraudes.  
        ✔️ **Considerar a implementação de verificações adicionais** ou **autenticação de dois fatores** durante esses horários críticos.  
       
     """)
        


 

    mes= { 1 : '01-jan', 2: '02-feb', 3: 'mar', 4: '04-apr', 5: '05-mai', 6: '06-jun', 
        7 : '07-jul', 8:'08-ago', 9: '09-sep', 10: '10-oct', 11: '11-nov', 12: '12-dec'}

    df['month'] = df['trans_date_trans_time'].dt.month.map(mes)

    df_month = df.groupby('month').agg(
        qtd_trans = ('trans_num', 'count'),
        qtd_fraud = ('is_fraud', 'sum'),
        mean_fraud = ('is_fraud', lambda x  :(x.mean()*100).round(2)),
        total_preju = ('amt', lambda x: x[df['is_fraud']== 1].sum())
    ).assign(
        fraud_ratio = lambda x : (x['qtd_trans'] / x['qtd_fraud']).astype(int)
    ).reset_index().sort_values(by= 'month', ascending=True)

    fig = make_subplots(rows=2, cols=1, subplot_titles=('Quantidade de transações fraudulentas','Prejuizo financeiro de transações fraudadas'), 
                        vertical_spacing=0.20)


    fig.add_trace(go.Bar(
        x=df_month['month'],
        y=df_month['qtd_fraud'],
        marker_color= 'lightblue',
        text=df_month['qtd_fraud']), row=1, col=1)



    fig.add_trace(go.Bar(
        x=df_month['month'],
        y=df_month['total_preju'],
        marker_color= 'lemonchiffon',
        text=df_month['total_preju'].apply(lambda x : f'{x/1000: .0f}k')), row=2, col=1)



    # Ajustando o layout
    fig.update_layout(
        height=600,
        title='Analise financeira',
        template='plotly_dark',
        showlegend=False,
        )

    #Atualizar titulo dos eixos
    fig.update_yaxes(title_text = 'Qtd. fraudes', row=1 ,col=1)
    fig.update_yaxes(title_text = 'Valor transações', row=2 ,col=1)


    st.plotly_chart(fig, use_container_width=True)


    with st.expander('##### 📌 Conclusão quantidade de fraudes por mês:', expanded=False):

        st.markdown("""


        1. **Junho:**
        - Em junho, foram realizadas **30 mil transações**, com uma **média de fraudes de 0,44%**. Isso significa que, a cada **226 transações legítimas**, **1 fraude** foi detectada, gerando um **prejuízo financeiro de 73 mil**.
        - Esse mês apresenta um **índice de fraudes moderado**, mas ainda assim relevante, considerando o volume total de transações.

        2. **Outubro:**
        - Outubro registrou **69 mil transações**, com um **índice de fraudes de 0,55%**, o **maior entre os meses analisados**. Isso indica que, a cada **180 transações**, **1 era fraudulenta**.
        - Esse mês se destaca como o **período com maior risco de fraudes**, tanto em termos percentuais quanto absolutos.
        - O **prejuízo financeiro** foi de **196 mil**.

        3. **Dezembro:**
        - Dezembro teve o **maior volume de transações (140 mil)**, mas o **menor índice de fraudes (0,18%)**. Isso significa que, a cada **540 transações**, apenas **1 era fraudulenta**.
        - Esse mês pode ser considerado o **mais seguro** em termos de fraudes, apesar do alto volume de transações.

        ---

        #### 📌 Resumo:

        - **Outubro** foi o mês com o **maior índice de fraudes**, com **1 fraude a cada 180 transações**. Esse período merece atenção especial, pois, além do alto percentual de fraudes, também teve um **volume significativo de transações**.
        - **Dezembro**, apesar de ter o **maior volume de transações (140 mil)**, apresentou o **menor índice de fraudes (0,18%)**, sendo o mês mais seguro.
        - **Junho** teve um **índice de fraudes moderado (0,44%)**, com **1 fraude a cada 226 transações**.

        **Observação importante:** Como não temos dados completos para os meses de **janeiro a maio**, não é possível afirmar se outubro é realmente o mês com o maior índice de fraudes ao longo de todo o ano. No entanto, com base nos dados disponíveis, outubro se destaca como o período de maior risco.

            """)