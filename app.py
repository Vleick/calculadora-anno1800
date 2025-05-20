import streamlit as st
import math

st.set_page_config(page_title="Calculadora Anno 1800", layout="wide")
st.title("🧮 Calculadora de Producción - Anno 1800 (Todas las regiones)")

st.markdown("""
Esta calculadora cubre las necesidades de producción para **todas las regiones** del juego base y DLCs:
- 🏙️ Viejo Mundo
- 🌴 Nuevo Mundo
- 🌞 Enbesa
- ❄️ Ártico
Incluye **interdependencias regionales**.
""")

# Función genérica de cálculo
def calcular(consumo_por_hab, n_habs, prod_por_min):
    total = n_habs * consumo_por_hab
    return math.ceil(total / prod_por_min)

# Tabs por región
tab_vm, tab_nm, tab_enbesa, tab_artico = st.tabs(["🏙️ Viejo Mundo", "🌴 Nuevo Mundo", "🌞 Enbesa", "❄️ Ártico"])

# ================= VIEJO MUNDO ====================
with tab_vm:
    st.header("🏙️ Viejo Mundo")
    campesinos = st.number_input("Campesinos", 0, step=100, value=200)
    obreros = st.number_input("Obreros", 0, step=100, value=200)
    artesanos = st.number_input("Artesanos", 0, step=100, value=200)
    ingenieros = st.number_input("Ingenieros", 0, step=100, value=200)

    st.subheader("Productos locales")
    panaderias = calcular(0.017, obreros, 1)
    st.write(f"🍞 Panaderías necesarias: {panaderias}")

    st.subheader("Productos importados")
    cafe = calcular(0.0085, ingenieros, 1)
    st.write(f"☕ Café necesario (producido en el 🌴 Nuevo Mundo): {cafe} unidades/minuto")

# ================= NUEVO MUNDO ====================
with tab_nm:
    st.header("🌴 Nuevo Mundo")
    jornaleros = st.number_input("Jornaleros", 0, step=100, value=200)
    obreros_nuevo = st.number_input("Obreros (N. Mundo)", 0, step=100, value=200)

    st.subheader("Productos locales")
    cafe_nm = calcular(0.0085, jornaleros, 1)
    st.write(f"☕ Plantaciones de café: {cafe_nm}")

    st.subheader("Exportación")
    st.write(f"🚢 Puedes exportar hasta {cafe_nm} unidades/minuto de café al 🏙️ Viejo Mundo")

# ================= ENBESA ====================
with tab_enbesa:
    st.header("🌞 Enbesa")
    ancianos = st.number_input("Ancianos", 0, step=100, value=200)
    sabios = st.number_input("Sabios", 0, step=100, value=200)

    st.subheader("Productos locales")
    injera = calcular(0.017, ancianos, 1)
    st.write(f"🍽️ Producción de Injera: {injera}")

    st.subheader("Productos importados")
    herramientas = calcular(0.0085, sabios, 1)
    st.write(f"🛠️ Herramientas necesarias desde 🏙️ Viejo Mundo: {herramientas} unidades/minuto")

# ================= ÁRTICO ====================
with tab_artico:
    st.header("❄️ Ártico")
    exploradores = st.number_input("Exploradores", 0, step=100, value=200)
    tecnicos = st.number_input("Técnicos", 0, step=100, value=200)

    st.subheader("Productos locales")
    aceite = calcular(0.017, exploradores, 1)
    st.write(f"🛢️ Estufas de aceite: {aceite}")

    st.subheader("Productos importados")
    abrigos = calcular(0.0085, tecnicos, 1)
    st.write(f"🧥 Abrigos importados desde 🌞 Enbesa o 🏙️ Viejo Mundo: {abrigos} unidades/minuto")

st.markdown("---")
st.caption("Versión inicial multi-región con lógica interdependiente básica. Se puede expandir con nuevas cadenas, ratios personalizados y optimización por electricidad.")
