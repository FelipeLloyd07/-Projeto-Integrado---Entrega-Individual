import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Entrega Individual — Trabalho', layout='wide')

df = pd.read_csv('data/emprego_sexo.csv')

st.title('Trabalho e População Empregada')
st.subheader('Taxa de desocupação por UF — 3º trimestre de 2012 x 3º trimestre de 2022')
st.write('Gráfico individual baseado em dados oficiais da PNAD Contínua/IBGE.')

with st.sidebar:
    sexo = st.selectbox('Sexo', ['Total', 'Homens', 'Mulheres'])
    ufs = st.multiselect('UF', sorted(df['uf'].unique()), default=sorted(df['uf'].unique()))

f = df[(df['sexo'] == sexo) & (df['uf'].isin(ufs))].copy()
if f.empty:
    st.warning('Selecione pelo menos uma UF.')
    st.stop()

long = f.melt(
    id_vars=['uf'],
    value_vars=['taxa_desocupacao_2012', 'taxa_desocupacao_2022'],
    var_name='ano',
    value_name='taxa'
)
long['ano'] = long['ano'].str.extract('(2012|2022)')[0]

fig = px.bar(
    long,
    x='uf',
    y='taxa',
    color='ano',
    barmode='group',
    text_auto='.1f',
    labels={'uf': 'Unidade da Federação', 'taxa': 'Taxa de desocupação (%)', 'ano': 'Ano'},
    color_discrete_map={'2012': '#6c9fb8', '2022': '#d95f59'},
    title=f'Taxa de desocupação — {sexo}'
)
fig.update_layout(yaxis_title='Taxa de desocupação (%)', xaxis_title='UF', legend_title='Ano')
st.plotly_chart(fig, use_container_width=True)

st.markdown(
    '**Como interpretar:** cada UF possui duas barras. A barra azul mostra a taxa no '
    '3º trimestre de 2012 e a vermelha mostra a taxa no 3º trimestre de 2022. '
    'A diferença entre elas é medida em pontos percentuais.'
)
st.caption('Fonte: IBGE, PNAD Contínua, SIDRA, tabela 4093. Dados reais.')
