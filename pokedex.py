import streamlit as st
import numpy as np
import requests
from buscar_nome_pokemon import buscar_nome_pokemon
from buscar_numero_pokemon import buscar_numero_pokemon

url = "https://pokeapi.co/api/v2/pokemon/"
requisicao = requests.get(url)
dados = requisicao.json()

st.title("PROTOTIPO POKEDEX")

numero_pokemon = st.number_input("Escolha o número do pokémon", value=None, placeholder= "Digite o número da pokedex do pokémon", min_value=0, max_value=1025, step=1)

nome_pokemon = st.text_input("Insira o nome do pokémon que deseja ver: ").lower()
if nome_pokemon:
    buscar_nome_pokemon(nome_pokemon)

elif numero_pokemon:
    buscar_numero_pokemon(numero_pokemon)
    
else:
    st.error("Este pokémon não existe!")


    
