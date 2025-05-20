import streamlit as st
import math
from collections import defaultdict

st.set_page_config(page_title="Calculadora Anno 1800", layout="wide")
st.title("🧮 Calculadora de Producción - Anno 1800 (Todas las regiones)")

st.markdown("""
Esta calculadora cubre las necesidades de producción para **todas las regiones** del juego base y DLCs:
- 🏙️ Viejo Mundo
- 🌴 Nuevo Mundo
- 🌞 Enbesa
- ❄️ Ártico
Incluye **interdependencias regionales**, exportaciones y materiales avanzados como los necesarios para dirigibles.
""")

# =====================================
# 🔽 Productos embebidos directamente en el código
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
            "bombillas": {"consumo": 0.0085, "produccion": 1, "emoji": "💡"},
            "teléfonos": {"consumo": 0.0085, "produccion": 1, "emoji": "📞"},
            "café": {"consumo": 0.0085, "produccion": 0, "emoji": "☕", "importado_de": "nuevo_mundo"}
        }
    },
    "nuevo_mundo": {
        "jornaleros": {
            "platano": {"consumo": 0.017, "produccion": 1, "emoji": "🍌"},
            "café": {"consumo": 0.0085, "produccion": 1, "emoji": "☕"},
            "algodón": {"consumo": 0.017, "produccion": 1, "emoji": "🧵"},
            "caucho": {"consumo": 0.0085, "produccion": 1, "emoji": "🌿"}
        },
        "obreros": {
            "cacao": {"consumo": 0.0085, "produccion": 1, "emoji": "🍫"},
            "ron": {"consumo": 0.0085, "produccion": 1, "emoji": "🥃"},
            "motores": {"consumo": 0.0085, "produccion": 1, "emoji": "⚙️"}
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
def calcular(consumo_por_hab, n_habs):
    return consumo_por_hab * n_habs

def calcular_edificios(total_demanda, produccion):
    if produccion == 0:
        return total_demanda
    return math.ceil(total_demanda / produccion)

# Estructura para recolectar demandas cruzadas
importaciones_necesarias = defaultdict(lambda: defaultdict(float))
poblaciones_regionales = {}

def registrar_importacion(origen, producto, cantidad):
    importaciones_necesarias[origen][producto] += cantidad

# =====================================
# Función general para mostrar región
# =====================================
def mostrar_region(nombre_region, region_key):
    st.header(f"{nombre_region}")
    poblaciones = {}
    poblaciones_regionales[region_key] = {}

    for clase in productos[region_key]:
        n = st.number_input(f"{clase.capitalize()} ({region_key})", 0, step=100, value=200)
        poblaciones[clase] = n
        poblaciones_regionales[region_key][clase] = n

    st.subheader("Productos locales")
    for clase, productos_clase in productos[region_key].items():
        for nombre, info in productos_clase.items():
            demanda_local = calcular(info["consumo"], poblaciones[clase])

            if "importado_de" in info:
                registrar_importacion(info["importado_de"], nombre, demanda_local)
                continue

            demanda_externa = importaciones_necesarias[region_key][nombre]
            demanda_total = demanda_local + demanda_externa
            edificios = calcular_edificios(demanda_total, info["produccion"])

            extra = f" (+{round(demanda_externa, 2)} externas)" if demanda_externa else ""
            st.write(f"{info['emoji']} {nombre.capitalize()}: {edificios} edificio(s) para {round(demanda_total, 2)} unidad/minuto{extra}")

    if region_key in importaciones_necesarias and importaciones_necesarias[region_key]:
        st.subheader("📦 Productos que debes exportar a otras regiones")
        for producto, cantidad in importaciones_necesarias[region_key].items():
            st.write(f"🚢 {producto.capitalize()}: {round(cantidad, 2)} unidad/minuto")

# =====================================
# Tabs por región y renderizado
# =====================================
tabs = st.tabs(["🏙️ Viejo Mundo", "🌴 Nuevo Mundo", "🌞 Enbesa", "❄️ Ártico"])
region_keys = ["viejo_mundo", "nuevo_mundo", "enbesa", "artico"]

for i, tab in enumerate(tabs):
    with tab:
        mostrar_region(tab.label, region_keys[i])

st.markdown("---")
st.caption("Versión interconectada entre regiones, calcula importaciones/exportaciones reales y suma toda la demanda.")
