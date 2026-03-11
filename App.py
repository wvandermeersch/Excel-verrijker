import streamlit as st
import pandas as pd
import time

# 1. Configuratie en Inlogscherm
st.set_page_config(page_title="Data Verrijker Pro", layout="centered")

def check_password():
    """Eenvoudige wachtwoordbeveiliging"""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.title("Inloggen")
        password = st.text_input("Voer wachtwoord in", type="password")
        if st.button("Log in"):
            if password == "MijnBedrijf2024": # Pas dit aan!
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Onjuist wachtwoord")
        return False
    return True

# 2. De Verrijkingslogica (Simulatie)
def verrijk_data(df):
    """
    Deze functie simuleert het zoeken op internet.
    In een echte scenario koppel je hier een API.
    """
    st.info("Bezig met het verrijken van gegevens via het internet...")
    progress_bar = st.progress(0)
    
    # We voegen nieuwe kolommen toe
    df['Telefoonnummer'] = "Onbekend"
    df['Email'] = "info@bedrijf.nl"
    df['Sector'] = "Technologie"
    
    for i in range(len(df)):
        # Simuleer zoektijd per rij
        time.sleep(0.5) 
        progress_bar.progress((i + 1) / len(df))
        
    return df

# 3. Hoofdprogramma
if check_password():
    st.title("🚀 Excel Target Verrijker")
    st.write("Upload je basislijst en de app zoekt de ontbrekende info.")

    uploaded_file = st.file_uploader("Kies een Excel bestand", type=["xlsx"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Voorbeeld van geüploade data:", df.head())

        if st.button("Start Verrijking"):
            verrijkte_df = verrijk_data(df)
            
            st.success("Verrijking voltooid!")
            st.write(verrijkte_df.head())

            # Download knop voor het resultaat
            output = verrijkte_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Verrijkt Bestand",
                data=output,
                file_name="target_klanten_verrijkt.csv",
                mime="text/csv"
            )
