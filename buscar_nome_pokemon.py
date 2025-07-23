import streamlit as st
import requests
import pandas as pd

def buscar_nome_pokemon(nome_pokemon):
    url_completa = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    requisicao = requests.get(url_completa)
    dados = requisicao.json()

    st.write(f"Número Pokedex: {dados["id"]}")
    st.write(f"Nome: {dados["name"]}")

    st.write("Tipos:")
    for tipo in dados["types"]:
        st.write("-", tipo["type"]["name"])

    st.write(f"Altura: {dados["height"]}  Peso: {dados["weight"]}Kg")

    st.subheader("Imagem: ")
    st.image(dados["sprites"]["other"]["official-artwork"]["front_default"])
    st.subheader("Forma Shiny: ")
    st.image(dados["sprites"]["other"]["official-artwork"]["front_shiny"])

    st.subheader("Som: ")
    st.audio(dados["cries"]["latest"])

    st.subheader("Status base: ")
    lista_status = []
    for stat in dados["stats"]:
        nome_status = (stat["stat"]["name"])
        base_status = (stat["base_stat"])
        lista_status.append({"Atributo": nome_status, "Status": base_status})

    data_frame = pd.DataFrame(lista_status)
    st.table(data_frame)