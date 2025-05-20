import streamlit as st
import math

st.set_page_config(page_title="Calculadora Anno 1800", layout="centered")
st.title("🧮 Calculadora de Producción - Anno 1800 (Viejo Mundo)")

st.markdown("""
Calculadora de producción para *Anno 1800* basada únicamente en bienes disponibles en el **Viejo Mundo** hasta el nivel de **artesanos**.  
No se incluyen productos del Nuevo Mundo ni DLC.  
""")

# Entradas
campesinos = st.number_input("👨‍🌾 Campesinos", 0, step=100, value=200)
obreros = st.number_input("🔧 Obreros", 0, step=100, value=200)
artesanos = st.number_input("🎩 Artesanos", 0, step=100, value=200)

st.markdown("---")

# Función genérica
def calcular(consumo_por_hab, n_habs, prod_por_min):
    total = n_habs * consumo_por_hab
    return math.ceil(total / prod_por_min)

# Resultados por categoría
st.header("📦 Resultados de producción")

# ====================
# CAMPESINOS
# ====================
st.subheader("👨‍🌾 Campesinos")

ropa = calcular(0.017, campesinos, 2)
st.write(f"🧥 **Ropa de trabajo**")
st.write(f"- 🐑 Granjas de ovejas: {ropa}")
st.write(f"- 🧵 Sastrerías: {ropa}")

pescado = calcular(0.017, campesinos, 1)
st.write(f"🐟 **Pescado**")
st.write(f"- 🎣 Pesquerías: {pescado}")

schnapps = calcular(0.017, campesinos, 1)
st.write(f"🥔 **Schnapps**")
st.write(f"- 🌱 Granjas de patatas: {schnapps}")
st.write(f"- 🥃 Destilerías: {schnapps}")

madera = calcular(0.017, campesinos, 4)  # Serrería produce 4/minuto
st.write(f"🪵 **Madera**")
st.write(f"- 🌲 Leñadores: {madera}")
st.write(f"- 🪚 Serrerías: {madera}")

# ====================
# OBREROS
# ====================
st.subheader("🔧 Obreros")

salchichas = calcular(0.017, obreros, 1)
st.write(f"🌭 **Salchichas**")
st.write(f"- 🐖 Granjas de cerdos: {salchichas}")
st.write(f"- 🪓 Mataderos: {salchichas}")
st.write(f"- 🏭 Fábricas de salchichas: {salchichas}")

pan = calcular(0.017, obreros, 1)
st.write(f"🍞 **Pan**")
st.write(f"- 🌾 Granjas de trigo: {pan}")
st.write(f"- 🌀 Molinos: {pan}")
st.write(f"- 🍞 Panaderías: {pan}")

jabon = calcular(0.0085, obreros, 1)
st.write(f"🧼 **Jabón**")
st.write(f"- 🐖 Granjas de cerdos (grasa): {jabon}")
st.write(f"- 🧪 Fábricas de sosa cáustica: {jabon}")
st.write(f"- 🧼 Fábricas de jabón: {jabon}")

cerveza = calcular(0.0085, obreros, 1)
st.write(f"🍺 **Cerveza**")
st.write(f"- 🌿 Granjas de lúpulo: {cerveza}")
st.write(f"- 🌾 Granjas de cebada: {cerveza}")
st.write(f"- 🏭 Malterías: {cerveza}")
st.write(f"- 🍺 Cervecerías: {cerveza}")

velas = calcular(0.0085, obreros, 1)
st.write(f"🕯️ **Velas**")
st.write(f"- 🧵 Granjas de lino: {velas}")
st.write(f"- 🪵 Madera: {velas}")
st.write(f"- 🕯️ Fábricas de velas: {velas}")

acero = calcular(0.0085, obreros, 1)
st.write(f"🔩 **Vigas de acero**")
st.write(f"- ⛏️ Minas de hierro: {acero}")
st.write(f"- 🔥 Fundiciones: {acero}")
st.write(f"- 🏗️ Fábricas de vigas: {acero}")

# ====================
# ARTESANOS
# ====================
st.subheader("🎩 Artesanos")

conservas = calcular(0.0085, artesanos, 1)
st.write(f"🥫 **Conservas**")
st.write(f"- 🐄 Granjas de ganado: {conservas}")
st.write(f"- 🌶️ Granjas de pimientos: {conservas}")
st.write(f"- 🍳 Cocinas artesanales: {conservas}")
st.write(f"- 🏭 Fábricas de conservas: {conservas}")

ventanas = calcular(0.0085, artesanos, 1)
st.write(f"🪟 **Ventanas**")
st.write(f"- 🏖️ Minas de arena: {ventanas}")
st.write(f"- 🔬 Fábricas de vidrio: {ventanas}")
st.write(f"- 🪟 Fábricas de ventanas: {ventanas}")

maquinas = calcular(0.0085, artesanos, 1)
st.write(f"🧵 **Máquinas de coser**")
st.write(f"- 🪵 Madera: {maquinas}")
st.write(f"- 🔩 Acero: {maquinas}")
st.write(f"- 🧵 Fábricas de máquinas: {maquinas}")

abrigos = calcular(0.0085, artesanos, 1)
st.write(f"🧥 **Abrigos de piel**")
st.write(f"- 🦌 Cabañas de cazadores: {abrigos}")
st.write(f"- 🧵 Sastrerías de lujo: {abrigos}")

st.markdown("---")
st.caption("Hecho con ❤️ para fans de Anno 1800")
