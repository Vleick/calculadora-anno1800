import streamlit as st
import math
import json

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

# =====================================
# 🔽 Datos simulados (futura carga JSON)
# =====================================
productos = {
    "viejo_mundo": {
        "campesinos": {
            "ropa de trabajo": {"consumo": 0.017, "produccion": 2, "emoji": "🧥"},
            "pescado": {"consumo": 0.017, "produccion": 1, "emoji": "🐟"},
            "schnapps": {"consumo": 0.017, "produccion": 1, "emoji": "🥔"},
            "madera": {"consumo": 0.017, "produccion": 4, "emoji": "🪵"}
        },
        "obreros": {
            "pan": {"consumo": 0.017, "produccion": 1, "emoji": "🍞"},
            "salchichas": {"consumo": 0.017, "produccion": 1, "emoji": "🌭"},
            "jabon": {"consumo": 0.0085, "produccion": 1, "emoji": "🧼"},
            "cerveza": {"consumo": 0.0085, "produccion": 1, "emoji": "🍺"},
            "vigas de acero": {"consumo": 0.0085, "produccion": 1, "emoji": "🔩"}
        },
        "artesanos": {
            "conservas": {"consumo": 0.0085, "produccion": 1, "emoji": "🥫"},
            "ventanas": {"consumo": 0.0085, "produccion": 1, "emoji": "🪟"},
            "máquinas de coser": {"consumo": 0.0085, "produccion": 1, "emoji": "🧵"},
            "abrigos de piel": {"consumo": 0.0085, "produccion": 1, "emoji": "🧥"}
        },
        "ingenieros": {
            "café": {"consumo": 0.0085, "produccion": 0, "emoji": "☕", "importado_de": "nuevo_mundo"}
        }
    },
    "nuevo_mundo": {
        "jornaleros": {
            "platano": {"consumo": 0.017, "produccion": 1, "emoji": "🍌"},
            "café": {"consumo": 0.0085, "produccion": 1, "emoji": "☕"},
            "algodón": {"consumo": 0.017, "produccion": 1, "emoji": "🧵"}
        },
        "obreros": {
            "cacao": {"consumo": 0.0085, "produccion": 1, "emoji": "🍫"},
            "ron": {"consumo": 0.0085, "produccion": 1, "emoji": "🥃"}
        }
    },
    "enbesa": {
        "ancianos": {
            "injera": {"consumo": 0.017, "produccion": 1, "emoji": "🍽️"},
            "hibisco": {"consumo": 0.0085, "produccion": 1, "emoji": "🌺"},
            "teff": {"consumo": 0.017, "produccion": 1, "emoji": "🌾"}
        },
        "sabios": {
            "linaza": {"consumo": 0.0085, "produccion": 1, "emoji": "🧵"},
            "herramientas": {"consumo": 0.0085, "produccion": 0, "emoji": "🛠️", "importado_de": "viejo_mundo"}
        }
    },
    "artico": {
        "exploradores": {
            "carne de foca": {"consumo": 0.017, "produccion": 1, "emoji": "🦭"},
            "aceite": {"consumo": 0.017, "produccion": 1, "emoji": "🛢️"}
        },
        "tecnicos": {
            "estufas": {"consumo": 0.0085, "produccion": 1, "emoji": "🔥"},
            "abrigos": {"consumo": 0.0085, "produccion": 0, "emoji": "🧥", "importado_de": "viejo_mundo"}
        }
    }
}

# =====================================
# 🔧 Función de cálculo genérico
# =====================================
def calcular(consumo_por_hab, n_habs, produccion):
    if produccion == 0:
        return n_habs * consumo_por_hab  # solo consumo si es importado
    total = n_habs * consumo_por_hab
    return math.ceil(total / produccion)

# =====================================
# Tabs de regiones
# =====================================
tabs = st.tabs(["🏙️ Viejo Mundo", "🌴 Nuevo Mundo", "🌞 Enbesa", "❄️ Ártico"])

# Función general para cada región
def mostrar_region(nombre_region, clases):
    st.header(f"{nombre_region}")
    poblaciones = {}
    region_key = nombre_region.split(" ")[1].lower()
    for clase in productos[region_key]:
        poblaciones[clase] = st.number_input(f"{clase.capitalize()}", 0, step=100, value=200)

    st.subheader("Productos locales")
    for clase, productos_clase in productos[region_key].items():
        for nombre, info in productos_clase.items():
            if "importado_de" in info:
                continue
            cantidad = calcular(info["consumo"], poblaciones[clase], info["produccion"])
            st.write(f"{info['emoji']} {nombre.capitalize()}: {cantidad}")

    st.subheader("Productos importados")
    for clase, productos_clase in productos[region_key].items():
        for nombre, info in productos_clase.items():
            if "importado_de" in info:
                cantidad = calcular(info["consumo"], poblaciones[clase], 0)
                origen = info.get("importado_de", "otra región")
                st.write(f"{info['emoji']} {nombre.capitalize()} (de {origen.replace('_', ' ')}): {cantidad} unidades/minuto")

# Mostrar cada región
titulos = ["🏙️ Viejo Mundo", "🌴 Nuevo Mundo", "🌞 Enbesa", "❄️ Ártico"]
for i, tab in enumerate(tabs):
    with tab:
        mostrar_region(titulos[i], productos[list(productos.keys())[i]])

st.markdown("---")
st.caption("Versión con todas las regiones y productos representativos integrados dinámicamente.")
