import streamlit as st
import math

st.set_page_config(page_title="Calculadora Anno 1800", layout="centered")
st.title("🧮 Calculadora de Producción - Anno 1800 (Viejo Mundo)")
st.markdown("Calculadora basada en el número de habitantes. Solo incluye productos fabricables en el Viejo Mundo (hasta artesanos).")

# ======================
# INPUTS
# ======================
campesinos = st.number_input("👨‍🌾 Número de campesinos:", min_value=0, step=50, value=200)
obreros = st.number_input("🔧 Número de obreros:", min_value=0, step=50, value=200)
artesanos = st.number_input("🎩 Número de artesanos:", min_value=0, step=50, value=200)

st.markdown("---")

# ======================
# FUNCIONES DE CÁLCULO
# ======================
def calcular_necesarios(consumo_por_hab, total_habitantes, produccion_por_min):
    consumo_total = total_habitantes * consumo_por_hab
    necesarios = math.ceil(consumo_total / produccion_por_min)
    return necesarios

# ======================
# CÁLCULOS POR PRODUCTO
# ======================

resultados = {}

# === Campesinos ===
resultados["Ropa de trabajo"] = calcular_necesarios(0.017, campesinos, 2)  # Sastrería
resultados["Pescado"] = calcular_necesarios(0.017, campesinos, 1)          # Pescador
resultados["Pan (campesinos)"] = calcular_necesarios(0.017, campesinos, 1) # Panadería
resultados["Cerveza (campesinos)"] = calcular_necesarios(0.0085, campesinos, 1)  # Cervecería

# === Obreros ===
resultados["Salchichas"] = calcular_necesarios(0.017, obreros, 1)
resultados["Jabón"] = calcular_necesarios(0.0085, obreros, 1)
resultados["Pan (obreros)"] = calcular_necesarios(0.017, obreros, 1)
resultados["Cerveza (obreros)"] = calcular_necesarios(0.0085, obreros, 1)
resultados["Zapatos de trabajo"] = calcular_necesarios(0.0085, obreros, 1)

# === Artesanos ===
resultados["Conservas"] = calcular_necesarios(0.0085, artesanos, 1)
resultados["Galletas"] = calcular_necesarios(0.0085, artesanos, 1)
resultados["Ropa de lujo"] = calcular_necesarios(0.0085, artesanos, 1)
resultados["Maletas"] = calcular_necesarios(0.0085, artesanos, 1)
resultados["Bombillas"] = calcular_necesarios(0.0085, artesanos, 1)

# ======================
# RESULTADOS
# ======================
st.header("📦 Resultados de Producción (por edificio)")

for producto, cantidad in resultados.items():
    st.write(f"🔹 **{producto}**: {cantidad} edificio(s) necesario(s)")

st.markdown("---")
st.caption("Cálculos basados en ratios estándar del juego base sin mejoras de productividad.")
