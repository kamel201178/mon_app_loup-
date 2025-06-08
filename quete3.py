import streamlit as st
import pandas as pd

# Chargement du fichier CSV avec les lignes que j ai cree
df_users = pd.read_csv("users.csv", sep=";")

# Initialisation des variables de session
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# Interface de connexion
if not st.session_state.logged_in:
    st.title("Connexion")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        user = df_users[df_users['name'] == username]
        if not user.empty and user.iloc[0]['password'] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Connexion réussie !")
        else:
            st.error("Identifiants incorrects.")
else:
    # Menu dans la sidebar
    st.sidebar.write(f"Bienvenue {st.session_state.username} !")
    page = st.sidebar.radio("Menu", ["Accueil", "Photos"])
    if st.sidebar.button("Déconnexion"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_rerun()

    # Contenu des pages
    if page == "Accueil":
        st.title("Bienvenue dans l'univers du Loup gris des neiges ")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("wolf1.jpg", use_container_width=True)
        with col2:
            st.image("wolf2.jpg", use_container_width=True)
        with col3:
            st.image("wolf3.jpg", use_container_width=True)

    elif page == "Photos":
        st.title("Album Photo")
        st.write("Voici la page de l'album. Tu peux ajouter d'autres photos ici.")


