import streamlit as st

# Título del formulario

# Datos fijos con estilo
st.markdown("""
<div style="border: 2px dashed #000; padding: 15px; border-radius: 10px; background-color: #f9f9f9;">
    <h3 style="color: #333;">Datos de la Empresa</h3>
    <p><strong>Nombre de la empresa:</strong> Solares Valencia (Empresa) - Jorge Luis González Ordaz</p>
    <p><strong>NIF:</strong> Y69018187Z</p>
    <p><strong>Dirección:</strong> Ave.Cuartel 7, puerta 13. CP:46770</p>
    <p><strong>Población:</strong> Xeraco Playa</p>
    <p><strong>Provincia:</strong> Valencia</p>
    <p><strong>Teléfono:</strong> +34 611 078 238</p>
</div>
""", unsafe_allow_html=True)



# Título del formulario
st.header(" Datos Clientes")


nombre_cliente = st.text_input("Nombre del Cliente:")
domicilio = st.text_input("Domicilio:")

col3, col4 = st.columns(2)

with col3:
    # Campo para el NIF
    poblacio = st.text_input("Población:")

with col4:
    telefono_cliente = st.text_input("Teléfono del cliente:")

st.markdown("---")  # Línea horizontal


st.header(" Datos del Servicio")

col5, col6 = st.columns([2, 3])

with col5:

    
# Número entre 1 y 10
    unidad = st.number_input(
    "Ingrese la unidad (1-10):",
    min_value=1,  # Valor mínimo
    max_value=10,  # Valor máximo
    step=1  # Incremento de los valores
        )


    

with col6:
    # Opciones del selector
    opciones_toldos = [
        "Toldo punto recto normal",
        "Toldo punto recto tensión",
        "Toldo punto recto tensión cofre",
        "Toldo telón balcón",
        "Toldo telón balcón con cofre",
        "Toldo telón quitavientos con guías",
        "Toldo telón quitavientos con cofre",
        "Toldo brazo invisible Smart",
        "Toldo brazo invisible cofre mini",
        "Toldo brazo invisible premium",
        "Toldo brazo cofre maxi",
        "Toldo brazo invisible cruzado",
        "Toldo brazo invisible monoblock",
        "Toldo patio guías 80x40 entre paredes",
        "Toldo patio guías 80x40 con portería",
        "Toldo patio guías 80x40 con doble portería",
        "Toldo patio guías 120x80 con portería",
        "Toldo patio guías 120x80 con doble portería",
        "Toldo patio guías 120x120 con portería",
        "Toldo patio guías 120x120 con doble portería",
        "Cortina con riel normal",
        "Vela tensada",
        "Cambio de lona"
    ]

    # Selector desplegable
    modelo_toldo = st.selectbox("Modelo de toldos:", opciones_toldos)

    # Mostrar la selección
    #st.write(f"Modelo seleccionado: {modelo_toldo}")


col7, col8,col9 = st.columns([1, 1,1])

with col7:
    # Número decimal entre 1 y 10
    linea = st.number_input(
    "Ingrese la Linea (1.0 - 10.0):",
    min_value=1.0,  # Valor mínimo
    max_value=10.0,  # Valor máximo
    step=0.1  # Incremento con decimales
    )

    # Mostrar el número ingresado
    #st.write(f"Unidad ingresada: {unidad}")

with col8:

    # Número decimal entre 1 y 10
    salida = st.number_input(
    "Ingrese la Salida (1.0 - 10.0):",
    min_value=1.0,  # Valor mínimo
    max_value=10.0,  # Valor máximo
    step=0.1  # Incremento con decimales
    )

    # Mostrar el número ingresado
    #st.write(f"Unidad ingresada: {unidad}")
with col9:

    referencia_lona = st.text_input("Referencia de lona:")


col10, col11 ,col12 = st.columns([1, 1, 1])

with col10:
    

    # Opciones del selector
    opciones_maquina = [
        "Derecha",
        "Izquierda",
        
    ]

    # Selector desplegable
    maquina = st.selectbox("Máquina:", opciones_maquina)

with col11:

    # Opciones del selector
    opciones_motor = [
        "Ninguno",
        "Pulsador",
        "Mando a distancia",
        
    ]

    # Selector desplegable
    motor = st.selectbox("Motor:", opciones_motor)
    
with col12:

    
    opciones_medida_manivela = [
        "0.80",
        "110",
        "120",
        "150",
        "180",
        "200",
        "220",
        "240",
        
    ]

    # Selector desplegable
    medida_manivela = st.selectbox("Medida de Manivela:", opciones_medida_manivela)


col13, col14 ,col15 = st.columns([1, 1, 1])

with col13:
    lacado = st.text_input("Lacado:")
with col14:
    opciones_faldon = [
        "Recto ",
        "Ondulado",
         "No"
    ]

    # Selector desplegable
    faldon = st.selectbox("Faldon:", opciones_faldon)
with col15:
    medida_faldon = st.number_input(
    "Medida del faldón:",
    min_value=0.3,  # Valor mínimo
    max_value=10.0,  # Valor máximo
    step=0.1  # Incremento con decimales
    )

opciones_automatismo  = [
        "Central Windtec Viento – Sol",
        "Central Windtec Solo Viento",
        "Central Vibración Solo Viento",
        "No"
    ]

# Selector desplegable
automatismo = st.selectbox("Automatismo climático:", opciones_automatismo)
    
st.markdown("---")  # Línea horizontal
st.markdown("---")  # Línea horizontal


firma = st.text_area("Observaciones:", height=180)  # Ajustar la altura aquí

st.markdown("---")  # Línea horizontal


# Crear dos columnas
col16, col17 = st.columns(2)

# Columna 1: Opciones de satisfacción
with col16:
    st.markdown("¿Está satisfecho?")
    opciones_satisfaccion = ["😞", "😐", "😊"]
    seleccion = st.radio(
        "Seleccione su nivel de satisfacción:", 
        opciones_satisfaccion, 
        index=1,  # Selección predeterminada
        horizontal=True
    )
    st.write(f"Ha seleccionado: {seleccion}")

# Columna 2: Campo para la firma
with col17:
    
    firma = st.text_area("Firma del cliente:", height=120)  # Ajustar la altura aquí


