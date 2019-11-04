import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
#from sklearn.ensemble import RandomForestClassifier



def main():
    """ RandonForestClassifier - Titanic """
    
    # Titulo
    st.title("	STREAMLIT	")
    st.title("RandonForestClassifier / Titanic")
    st.markdown("Streamlit é um servidor python para web apps.")

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
    st.write("## sobreviveu")
    st.markdown("ou")
    st.markdown("## morreu")
    st.text("Foram aplicados: LabeEncoder, OneHotEncoder e StandarScaler.")
    st.text("O modelo treinado foi salvo com o pacote pickle (dump e load)")
    st.markdown("Acurácia: 83.58%")
    
    filename = "RFmodel.sav"
    
    rfmodel = pickle.load(open(filename,'rb'))

    st.markdown("## Selecione as caracteristicas do passageiro")

    classe = st.radio('Classe',('Primeira Classe', 'Segunda Classe', 'Terceira Classe'))

    sexo = st.radio('Sexo',('Homem', 'Mulher'))

    embarque = st.radio('Cidade de Embarque',('Cherboug', 'Queenstown', 'Southampton'))

    idade = st.slider('Idade',min_value=1, max_value=80, value=20, step=5)
  
    passagem = st.slider('Valor da Passagem',min_value=0, max_value=512, value=100, step=50)

    st.markdown("## Caracteristicas selecionadas")

    st.write("Classe:", classe)

    st.write("Sexo:", sexo)

    st.write("Cidade de Embarque:", embarque)

    st.write("Idade:", idade)

    st.write("Preço da Passagem:", passagem)

    data = [{'Classe': classe, 'Sexo': sexo, 'Embarque':embarque, 'Idade': idade, 'Passagem': passagem}]

    df = pd.DataFrame(data)

    st.write(df)

    le = LabelEncoder()
   
    df.Classe =   le.fit_transform(df.Classe)
    df.Sexo   =   le.fit_transform(df.Sexo)
    df.Embarque = le.fit_transform(df.Embarque)

    oneh = OneHotEncoder(categorical_features=[0,1,2])
    df = oneh.fit_transform(df).toarray()

    #scaler = StandardScaler()
    #df = scaler.fit_transform(df)
   
    st.write(df)
    
    rfmodel(df)



if __name__ == '__main__':
    main()

     
