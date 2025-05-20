import streamlit as st
import math

st.set_page_config(page_title="Calculadora Anno 1800", layout="centered")

st.title("🧮 Calculadora de Producción - Anno 1800")
st.markdown("Versión inicial en castellano. Introduce el número de habitantes por nivel para estimar los edificios necesarios.")

# Entradas de población
campesinos = st.number_input("👨‍🌾 Número de campesinos:", min_value=0, step=50, value=200)
obreros = st.number_input("🔧 Número de obreros:", min_value=0, step=50, value=200)

st.markdown("---")

# === Ropa de trabajo ===
ropa_consumo_total = campesinos * 0.5  # unidades/minuto
sastrerias_necesarias = math.ceil(ropa_consumo_total / 2)  # produce 2/min
granjas_ovejas_necesarias = sastrerias_necesarias  # 1:1

# === Salchichas ===
salchichas_consumo_total = obreros * 0.25
fabricas_salchichas = math.ceil(salchichas_consumo_total / 1)  # produce 1/min
mataderos = fabricas_salchichas
granjas_cerdos = fabricas_salchichas

# === Pan ===
pan_consumo_total = obreros * 0.25
panaderias = math.ceil(pan_consumo_total / 1)
molinos = panaderias  # cada molino produce 2/min
granjas_trigo = molinos

# === Resultados ===
st.header("📦 Resultados de Producción")

st.subheader("👕 Ropa de trabajo")
st.write(f"- Sastrerías necesarias: **{sastrerias_necesarias}**")
st.write(f"- Granjas de ovejas: **{granjas_ovejas_necesarias}**")

st.subheader("🐷 Salchichas")
st.write(f"- Fábricas de salchichas: **{fabricas_salchichas}**")
st.write(f"- Mataderos: **{mataderos}**")
st.write(f"- Granjas de cerdos: **{granjas_cerdos}**")

st.subheader("🍞 Pan")
st.write(f"- Panaderías: **{panaderias}**")
st.write(f"- Molinos: **{molinos}**")
st.write(f"- Granjas de trigo: **{granjas_trigo}**")

st.markdown("---")
st.caption("Creado con ❤️ por ChatGPT y tú 😄")
