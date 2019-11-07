import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import time
import plotly.express as px



def main():
    """ RandonForestClassifier - Titanic """
    
    # Titulo
    st.title("	STREAMLIT APPS	")
    #st.markdown("## Silvio Lima")
    st.title("RandomForestClassifier / Titanic")
    

    st.sidebar.title('EDA & Classificação')

    st.sidebar.text('Titanic - 891 obs. / 6 atributos')

    st.sidebar.markdown('Selecione uma opção:')

    def ler_dados(dataset):
        df = pd.read_csv(os.path.join(dataset))
        return df
    
    # Carregar dataset
    my_dataset = "dataset.csv"
    data = ler_dados(my_dataset)
    
    

    if st.sidebar.checkbox("Preview Dataset"):      
        st.write("Preview - 100")
        st.write(data.head(100))
    
    if st.sidebar.checkbox("Distribuiçao dos dados"):      
        x = st.sidebar.selectbox('Atributo: ', ['Status','Classe', 'Sexo', 'Idade', 'Embarque', 'Passagem'])      
        st.write("Histograma:  ",x)
        fig1 = px.histogram(data, x=x, hover_data=data.columns, color=x)
        st.plotly_chart(fig1)
        
    if st.sidebar.checkbox('Previsão / Classificação'):
        filename = "RFmodel.sav"
        rfmodel = pickle.load(open(filename,'rb'))
        st.sidebar.markdown("Selecione as caracteristicas do passageiro")
        classe = st.sidebar.radio('Classe',('Primeira Classe ', 'Segunda Classe', 'Terceira Classe'))
        sexo = st.sidebar.radio('Sexo',('Homem', 'Mulher'))
        embarque = st.sidebar.radio('Cidade de Embarque',('Cherboug', 'Queenstown', 'Southampton'))
        idade = st.sidebar.slider('Idade',min_value=1, max_value=80, value=20, step=5)
        passagem = st.sidebar.slider('Valor da Passagem',min_value=0, max_value=512, value=100, step=10)
        st.markdown("## Caracteristicas selecionadas do passageiro")
        st.write(classe,'---', sexo, '---',embarque,'---',idade,"anos",'---','$$',passagem)
        st.markdown("Confira as caracteristicas do passageiro no Preview")
        data = [{'Classe': classe, 'Sexo': sexo, 'Embarque':embarque, 'Idade': idade, 'Passagem': passagem}]
        df = pd.DataFrame(data)
        status = rfmodel.predict(df)
        bar = st.progress(0)

        if st.button('Submit'):
            for i in range(11):
                bar.progress(i * 10)
                # wait
                time.sleep(0.1)
            st.markdown('#### De acordo com o modelo:')
            if (status == 'Sobreviveu'):
                st.markdown('# Sobreviveu')
                st.write("vamos comemorar!")
                st.balloons()
            else:
                st.markdown('# Morreu')
                st.write(" infelizmente no acidente")
        
    

if __name__ == '__main__':
    main()

     
