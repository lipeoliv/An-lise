import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title= "Atividade Final") #layout="wide"

with st.container():

    st.subheader( "Análise de Dados")
    st.title("Datafreme com valores do Combustível Automotivo no 2° Semestre do ano de 2022")
    st.write(" Na primeira etapa será feito a preparação do dados! ")

with st.container():
    st.write("---")
    st.write("Abrindo o DataFrame:")
    df = pd.read_csv("ca-2022-02.csv", sep=";" , decimal=",")
    df 

with st.container():
    st.write("---")
    st.subheader("Usado para contar o número de valores nulos em cada coluna do DataFrame.")
    st.write("Contagem de valores nulos por coluna:")
    st.write(df.isnull().sum())
   



with st.container():
    st.write("---")
    st.subheader("Isso atribuirá o valor 'Sem Numero' à coluna 'Numero Rua' nas linhas onde a coluna 'Numero Rua' é nula.")
    df.loc[df['Numero Rua'].isnull(), 'Numero Rua'] = 'Sem Numero'
    df
    

with st.container():

    st.write("---")
    st.subheader("Isso atribuirá o valor 'Nao Informado' à coluna ' Bairro' nas linhas onde a coluna Bairro' é nula.")
    df.loc[df['Bairro'].isnull(), 'Bairro'] = 'Nao Informado'
    df
   

with st.container():
    st.write("---")
    st.subheader("Isso atribuirá o valor 'Nao Informado'à coluna' Complemento' nas linhas onde a coluna 'Complemento' é nula.")
    df.loc[df['Complemento'].isnull(), 'Complemento'] = 'Nao Informado'
    df
    
with st.container():

    st.write("---")
    st.subheader("A Coluna 'Valor de Compra' foi excluída pois só existe números nulos nela.")
    del df['Valor de Compra']
    df
    st.write("---")







# a seguir será feito as análise 
    

with st.container():
    st.write("---") 
    produto_selecionado = st.selectbox("Selecione o Produto:", df['Produto'].unique())

    # Filtra os dados com base no produto selecionado
    dados_produto_selecionado = df[df['Produto'] == produto_selecionado]

    # Encontra o maior preço de venda do produto para cada estado
    maiores_precos_por_estado = dados_produto_selecionado.groupby('Estado - Sigla')['Valor de Venda'].max().reset_index()

    # Exibe no Streamlit
    st.subheader(f" 1° Maior Preço de Venda de {produto_selecionado} por Estado")

    # Verifica se há resultados na consulta
    if not maiores_precos_por_estado.empty:
        # Cria um gráfico de barra
        st.bar_chart(maiores_precos_por_estado.set_index('Estado - Sigla'))
        
        # Exibe uma tabela com os resultados
        st.write(maiores_precos_por_estado)
  
with st.container():
    st.write("---") 
    produto_selecionado = st.selectbox("Selecione o Produto:", df['Produto'].unique(),key="selectbox_produto")

    # Filtra os dados com base no produto selecionado
    dados_produto_selecionado = df[df['Produto'] == produto_selecionado]

    # Encontra o maior preço de venda do produto para cada estado
    maiores_precos_por_estado = dados_produto_selecionado.groupby('Estado - Sigla')['Valor de Venda'].min().reset_index()

    # Exibe no Streamlit
    st.subheader(f" 2° Menor Preço de Venda de {produto_selecionado} por Estado")

    # Verifica se há resultados na consulta
    if not maiores_precos_por_estado.empty:
        # Cria um gráfico de barra
        st.bar_chart(maiores_precos_por_estado.set_index('Estado - Sigla'))
        
        # Exibe uma tabela com os resultados
        st.write(maiores_precos_por_estado)


with st.container():

    st.write("---")
    dados_rn = df[df['Estado - Sigla'] == 'RN']

    # Escolha um produto específico para análise (você pode ajustar conforme necessário)
    produto_selecionado = 'GASOLINA'

    # Filtra os dados com base no produto selecionado
    dados_produto_selecionado = dados_rn[dados_rn['Produto'] == produto_selecionado]

    # Encontra o maior preço de venda do produto para cada município
    maiores_precos_por_municipio = dados_produto_selecionado.groupby('Municipio')['Valor de Venda'].max().reset_index()

    # Exibe no Streamlit
    st.subheader(f" 3° Maior Preço de Venda de {produto_selecionado} por Município no RN")

    # Verifica se há resultados na consulta
    if not maiores_precos_por_municipio.empty:
        # Cria um gráfico de barra
        st.bar_chart(maiores_precos_por_municipio.set_index('Municipio'))
        
        # Exibe uma tabela com os resultados
        st.write(maiores_precos_por_municipio)
    else:
        st.write(f"Sem dados disponíveis para {produto_selecionado} no RN.")

with st.container():
    st.write("---")
    dados_rn = df[df['Estado - Sigla'] == 'RN']

    # Escolha um produto específico para análise (você pode ajustar conforme necessário)
    produto_selecionado = 'GASOLINA'

    # Filtra os dados com base no produto selecionado
    dados_produto_selecionado = dados_rn[dados_rn['Produto'] == produto_selecionado]

    # Encontra o maior preço de venda do produto para cada município
    maiores_precos_por_municipio = dados_produto_selecionado.groupby('Municipio')['Valor de Venda'].min().reset_index()

    # Exibe no Streamlit
    st.subheader(f" 4° Menor Preço de Venda de {produto_selecionado} por Município no RN")

    # Verifica se há resultados na consulta
    if not maiores_precos_por_municipio.empty:
        # Cria um gráfico de barra
        st.bar_chart(maiores_precos_por_municipio.set_index('Municipio'))
        
        # Exibe uma tabela com os resultados
        st.write(maiores_precos_por_municipio)
    else:
        st.write(f"Sem dados disponíveis para {produto_selecionado} no RN.")


with st.container():
    st.write("---")
    dados_rn = df[df['Estado - Sigla'] == 'PB']

    # Escolha um produto específico para análise (você pode ajustar conforme necessário)
    produto_selecionado = 'GASOLINA'

    # Filtra os dados com base no produto selecionado
    dados_produto_selecionado = dados_rn[dados_rn['Produto'] == produto_selecionado]

    # Encontra o maior preço de venda do produto para cada município
    maiores_precos_por_municipio = dados_produto_selecionado.groupby('Municipio')['Valor de Venda'].max().reset_index()

    # Exibe no Streamlit
    st.subheader(f" 6° Maior Preço de Venda de {produto_selecionado} por Município na PB")

    # Verifica se há resultados na consulta
    if not maiores_precos_por_municipio.empty:
        # Cria um gráfico de barra
        st.bar_chart(maiores_precos_por_municipio.set_index('Municipio'))
        
        # Exibe uma tabela com os resultados
        st.write(maiores_precos_por_municipio)
  


with st.container():
    st.write("---")
    dados_rn = df[df['Estado - Sigla'] == 'PB']

    # Escolha um produto específico para análise (você pode ajustar conforme necessário)
    produto_selecionado = 'GASOLINA'

    # Filtra os dados com base no produto selecionado
    dados_produto_selecionado = dados_rn[dados_rn['Produto'] == produto_selecionado]

    # Encontra o maior preço de venda do produto para cada município
    maiores_precos_por_municipio = dados_produto_selecionado.groupby('Municipio')['Valor de Venda'].min().reset_index()

    # Exibe no Streamlit
    st.subheader(f" 7° Menor Preço de Venda de {produto_selecionado} por Município na PB")

    # Verifica se há resultados na consulta
    if not maiores_precos_por_municipio.empty:
        # Cria um gráfico de barra
        st.bar_chart(maiores_precos_por_municipio.set_index('Municipio'))
        
        # Exibe uma tabela com os resultados
        st.write(maiores_precos_por_municipio)


  


with st.container():
    st.write("---") 
    estado_selecionado = st.selectbox("Selecione o Estado:", df['Estado - Sigla'].unique())

    # Filtra os dados com base no estado selecionado
    dados_estado_selecionado = df[df['Estado - Sigla'] == estado_selecionado]

    # Escolha um produto específico para análise (você pode ajustar conforme necessário)
    produto_selecionado = 'GASOLINA'

    # Filtra os dados com base no produto selecionado
    dados_produto_selecionado = dados_estado_selecionado[dados_estado_selecionado['Produto'] == produto_selecionado]

    # Encontra o maior preço de venda do produto para cada município
    maiores_precos_por_municipio = dados_produto_selecionado.groupby('Municipio')['Valor de Venda'].max().reset_index()

    # Exibe no Streamlit
    st.subheader(f"8° Preço da {produto_selecionado} por Município {estado_selecionado}")

    # Verifica se há resultados na consulta
    if not maiores_precos_por_municipio.empty:
        # Cria um gráfico de barra
        st.bar_chart(maiores_precos_por_municipio.set_index('Municipio'))
        
        # Exibe uma tabela com os resultados
        st.write(maiores_precos_por_municipio)

