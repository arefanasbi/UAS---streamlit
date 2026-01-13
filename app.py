import streamlit as st

st.set_page_config(page_title="Deteksi COVID-19", page_icon="🦠", layout="centered")

# Fungsi diagnosa
def diagnosa_covid(demam, batuk, sesak_napas, indra_penciuman):
    if demam == "Ya":
        if sesak_napas == "Ya":
            if indra_penciuman == "Ya":
                return "Positif COVID-19 🚨"
            else:
                return "Negatif COVID-19 ✅"
        else:
            if batuk == "Ya":
                if indra_penciuman == "Ya":
                    return "Positif COVID-19 🚨"
                else:
                    return "Negatif COVID-19 ✅"
            else:
                return "Negatif COVID-19 ✅"
    else:
        return "Negatif COVID-19 ✅"

# UI Streamlit
st.title("🦠 Deteksi Gejala COVID-19")
st.markdown("Isi form berikut untuk mendapatkan diagnosa awal berdasarkan gejala yang Anda alami.")

col1, col2 = st.columns(2)

with col1:
    demam = st.selectbox("Demam?", ["Ya", "Tidak"])
    batuk = st.selectbox("Batuk?", ["Ya", "Tidak"])

with col2:
    sesak_napas = st.selectbox("Sesak Napas?", ["Ya", "Tidak"])
    indra_penciuman = st.selectbox("Kehilangan Indra Penciuman?", ["Ya", "Tidak"])

if st.button("Diagnosa Sekarang", type="primary"):
    hasil = diagnosa_covid(demam, batuk, sesak_napas, indra_penciuman)
    
    if "Positif" in hasil:
        st.error(hasil)
        st.warning("Segera hubungi dokter atau fasilitas kesehatan terdekat!")
    else:
        st.success(hasil)
        st.info("Tetap jaga kesehatan dan patuhi protokol kesehatan.")

st.markdown("---")
st.caption("Aplikasi ini hanya untuk tujuan edukasi. Konsultasi dengan tenaga medis untuk diagnosa yang akurat.")