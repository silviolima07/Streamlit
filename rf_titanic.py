import streamlit as st
import pickle
import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import time



def main():
    """ RandonForestClassifier - Titanic """
    
    # Titulo
    st.title("	STREAMLIT	")
    st.title("RandomForestClassifier / Titanic")
    st.markdown("## Silvio Lima")

    st.sidebar.title("About")

    st.sidebar.info(
    "Streamlit é uma biblioteca do Python que torna fácil construir apps web. Semelhante ao Shiny usado com R. Veja mais em: https://github.com/streamlit/streamlit e https://streamlit.io/")

    # Carregar dataset
    my_dataset = "dataset.csv"
    st.text(" Dataset Titanic - 891 observações / 6 atributos")
    st.text("Atributos: Status, Classe, Sexo, Idade, Passagem, Embarque")
    
    def ler_dados(dataset):
        df = pd.read_csv(os.path.join(dataset))
        return df

    if st.checkbox("Preview Dataset"):
        data = ler_dados(my_dataset)
        if st.button("Head"):
            st.write(data.head())
    
    st.text("Modelo gerado para classificar se o passageiro:")
    st.write("SOBREVIVEU ou MORREU")
    st.text("O modelo obteve uma acurácia de 83.58%")
    
    filename = "RFmodel.sav"
    
    rfmodel = pickle.load(open(filename,'rb'))

    st.markdown("## Selecione as caracteristicas do passageiro")

    classe = st.radio('Classe',('Primeira Classe ', 'Segunda Classe', 'Terceira Classe'))

    sexo = st.radio('Sexo',('Homem', 'Mulher'))

    embarque = st.radio('Cidade de Embarque',('Cherboug', 'Queenstown', 'Southampton'))

    idade = st.slider('Idade',min_value=1, max_value=80, value=20, step=5)
  
    passagem = st.slider('Valor da Passagem',min_value=0, max_value=512, value=100, step=50)

    st.markdown("## Caracteristicas selecionadas do passageiro")

    st.write(classe,'---', sexo, '---',embarque,'---',idade,"anos",'---','$$',passagem)
    

    data = [{'Classe': classe, 'Sexo': sexo, 'Embarque':embarque, 'Idade': idade, 'Passagem': passagem}]

    df = pd.DataFrame(data)
 
    if (classe == "Primeira Classe" and sexo == "Homem" and embarque == "Cherboug" and idade == 20 and passagem == 512):
        status = "Nada"
     
    status = rfmodel.predict(df)

    time.sleep(1)

    if (status == 'Sobreviveu'):
        st.markdown('# Sobreviveu')
        #st.balloons()
    else:
        st.markdown('# Morreu')
        st.write(" no acidente")
        
    
    #st.markdown("Parametros do modelo gerado")
    #st.write(rfmodel)
    


if __name__ == '__main__':
    main()

     
