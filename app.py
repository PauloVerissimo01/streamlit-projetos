import pandas as pd # pacote para manipulação de dados
import seaborn as sns # para contrução de Gráficos
import matplotlib.pyplot as plt
import streamlit as st # nos permite criar uma aplocação web, para nosso projeto de Dados


# importando os dados

dados = pd.read_csv('estoque.csv')

st.title (' Análise de estoque\n')

st.write('Nesse projeto vamos analisar a quantidade de produtos em estoque, por categoria. de uma base de dados de produtos de supermercado')


# filtros para a tabela
checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')
# pacote stream modulo: barra lateral func: checbox, stream: aplc web



if checkbox_mostrar_tabela:

    st.sidebar.markdown('Filtro para tabela')

    categorias = list[dados['Categoria'].unique()]
    categorias.append('Todas')

 