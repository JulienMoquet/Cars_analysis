import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

st.subheader("Corrélations des caractéristiques d'une voiture")

heatmap_corr, ax = plt.subplots()
sns.heatmap(df.corr(), cmap = "coolwarm", ax = ax)
st.pyplot(heatmap_corr)


st.header("Statistiques par Pays et caractéristiques")

pays = []
st.write("Pays")

if st.checkbox("US", value = True):
	pays.append(' US.')
if st.checkbox("Europe", value = True):
	pays.append(' Europe.')
if st.checkbox("Japon", value = True):
	pays.append(" Japan.")

cara = st.radio("Caractéristque:", ['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60', 'year'])

graph , ax1 = plt.subplots()
sns.barplot(data = df.loc[df.continent.isin(pays)], x = "continent", y = df[cara], ax = ax1)
ax1.set_title(f"Moyenne de {cara} par pays")
st.pyplot(graph)