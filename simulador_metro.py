import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# 1. Configuración de la página y estilo visual retro
st.set_page_config(page_title="Mundo 2: Simulador CDMX", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    .retro-title {
        font-family: 'Press Start 2P', monospace;
        color: #E52521;
        text-shadow: 2px 2px 0px #000000;
        font-size: 22px;
        margin-bottom: 20px;
    }
    .retro-text {
        font-family: 'Press Start 2P', monospace;
        font-size: 11px;
        color: #43B047;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="retro-title"> Mundo 2: Redes de Optimización CDMX</div>', unsafe_allow_html=True)
st.markdown('<div class="retro-text">Desarrollado por: Christian Gabriel Villafuerte Aguilar y Esteban Gonzalez Reyes </div><br>', unsafe_allow_html=True)

# 2. Definición de la Red Base
def crear_red_metro():
    G = nx.Graph()
    pos = {
        'Politécnico': (8, 12), 'Indios Verdes': (12, 11), 'Inst. del Petróleo': (6, 11),
        '18 de Marzo': (10, 10), 'Rosario': (2, 11), '4 Caminos': (-1, 10),
        'Martín Carrera': (12, 8.5), 'La Raza': (7, 9), 'Tacuba': (2, 9),
        'Buenavista': (3.5, 8.5), 'Guerrero': (5, 8), 'Consulado': (9, 7.5),
        'Hidalgo': (3.5, 7), 'Garibaldi': (6.5, 6.5), 'Oceanía': (11, 6),
        'Ciudad Azteca': (14, 5.5), 'Bellas Artes': (5, 5.5), 'Morelos': (8, 5),
        'Tacubaya': (0, 6.5), 'Observatorio': (-2, 6.5), 'Balderas': (2, 5.5),
        'Salto del Agua': (3.5, 4.5), 'San Lázaro': (10, 4.5), 'Pino Suárez': (5, 3.5),
        'Candelaria': (7.5, 3.5), 'Pantitlán': (12, 3), 'La Paz': (14, 1),
        'Centro Médico': (1.5, 3), 'Chabacano': (4.5, 2), 'Jamaica': (7, 2),
        'Mixcoac': (-1, 2.5), 'Barranca del Muerto': (-3, 1.5), 'Zapata': (1, 1),
        'Universidad': (-1, -0.5), 'Ermita': (3, -0.5), 'Santa Anita': (6.5, 0.5),
        'Tasqueña': (1, -2), 'Atlalilco': (5, -1.5), 'Const. de 1917': (7, -3),
        'Tláhuac': (3, -3)
    }
    
    edges = [
        ('Politécnico', 'Inst. del Petróleo', 2), ('Rosario', 'Inst. del Petróleo', 8),
        ('Inst. del Petróleo', '18 de Marzo', 4), ('Inst. del Petróleo', 'La Raza', 4),
        ('18 de Marzo', 'Indios Verdes', 2), ('18 de Marzo', 'La Raza', 4),
        ('18 de Marzo', 'Martín Carrera', 4), ('Rosario', 'Tacuba', 12),
        ('4 Caminos', 'Tacuba', 4), ('Tacuba', 'Hidalgo', 8), ('Tacuba', 'Tacubaya', 6),
        ('La Raza', 'Guerrero', 4), ('La Raza', 'Consulado', 4), ('Buenavista', 'Guerrero', 2),
        ('Martín Carrera', 'Consulado', 6), ('Consulado', 'Oceanía', 6),
        ('Consulado', 'Morelos', 4), ('Guerrero', 'Hidalgo', 2), ('Guerrero', 'Garibaldi', 2),
        ('Hidalgo', 'Bellas Artes', 2), ('Hidalgo', 'Balderas', 4), ('Garibaldi', 'Bellas Artes', 2),
        ('Garibaldi', 'Morelos', 6), ('Oceanía', 'Ciudad Azteca', 24), ('Oceanía', 'San Lázaro', 6),
        ('Oceanía', 'Pantitlán', 6), ('Bellas Artes', 'Salto del Agua', 4),
        ('Bellas Artes', 'Pino Suárez', 4), ('Morelos', 'San Lázaro', 2),
        ('Morelos', 'Candelaria', 2), ('San Lázaro', 'Candelaria', 2),
        ('San Lázaro', 'Pantitlán', 8), ('Pantitlán', 'La Paz', 18),
        ('Observatorio', 'Tacubaya', 3), ('Tacubaya', 'Balderas', 8),
        ('Tacubaya', 'Centro Médico', 4), ('Tacubaya', 'Mixcoac', 4),
        ('Balderas', 'Salto del Agua', 2), ('Balderas', 'Centro Médico', 4),
        ('Salto del Agua', 'Pino Suárez', 2), ('Pino Suárez', 'Candelaria', 2),
        ('Pino Suárez', 'Chabacano', 4), ('Candelaria', 'Jamaica', 4),
        ('Mixcoac', 'Barranca del Muerto', 2), ('Mixcoac', 'Zapata', 4),
        ('Centro Médico', 'Zapata', 4), ('Centro Médico', 'Chabacano', 4),
        ('Zapata', 'Universidad', 6), ('Zapata', 'Ermita', 5),
        ('Chabacano', 'Ermita', 8), ('Chabacano', 'Jamaica', 2),
        ('Jamaica', 'Pantitlán', 8), ('Jamaica', 'Santa Anita', 2),
        ('Ermita', 'Tasqueña', 4), ('Ermita', 'Atlalilco', 5),
        ('Santa Anita', 'Atlalilco', 8), ('Atlalilco', 'Const. de 1917', 6),
        ('Atlalilco', 'Tláhuac', 18)
    ]
    G.add_weighted_edges_from(edges)
    return G, pos

G_base, pos = crear_red_metro()

# 3. Interfaz de Usuario
opciones = [
    "1. Ruta más corta (Dijkstra)", 
    "2. Árbol de peso mínimo (Kruskal)",
    "3. What-If 1: Cierre de Balderas (Dijkstra)",
    "4. What-If 2: Modernización (Kruskal)"
]
algoritmo = st.sidebar.selectbox("Selecciona el escenario:", opciones)

col1, col2 = st.columns([1, 2.5])

with col1:
    st.markdown("### Parámetros y Resultados")
    
    # ========================================================
    # ESCENARIO 1: DIJKSTRA NORMAL
    # ========================================================
    if algoritmo == "1. Ruta más corta (Dijkstra)":
        st.write("Calcula el trayecto estándar más rápido.")
        origen = st.selectbox("Origen:", list(G_base.nodes()), index=5)
        destino = st.selectbox("Destino:", list(G_base.nodes()), index=33)
        
        if st.button("Calcular Ruta"):
            try:
                ruta = nx.dijkstra_path(G_base, origen, destino, weight='weight')
                costo = nx.dijkstra_path_length(G_base, origen, destino, weight='weight')
                st.success(f"**Costo Total:** {costo} minutos")
                st.info(f"**Ruta:** {' ➔ '.join(ruta)}")
                
                G_draw = G_base
                ruta_edges = list(zip(ruta, ruta[1:]))
                edge_colors = ['red' if (u, v) in ruta_edges or (v, u) in ruta_edges else 'lightgray' for u, v in G_draw.edges()]
                edge_widths = [3.0 if (u, v) in ruta_edges or (v, u) in ruta_edges else 1.0 for u, v in G_draw.edges()]
            except nx.NetworkXNoPath:
                st.error("No hay ruta disponible.")
    
    # ========================================================
    # ESCENARIO 2: KRUSKAL NORMAL
    # ========================================================
    elif algoritmo == "2. Árbol de peso mínimo (Kruskal)":
        st.write("Conexión estructural de toda la red.")
        if st.button("Calcular Árbol"):
            mst = nx.minimum_spanning_tree(G_base, weight='weight', algorithm='kruskal')
            costo = sum(d['weight'] for u, v, d in mst.edges(data=True))
            st.success(f"**Costo Total del Árbol:** {costo} unidades")
            st.info(f"**Total de conexiones:** {mst.number_of_edges()} aristas")
            
            G_draw = G_base
            mst_edges = list(mst.edges())
            edge_colors = ['#43B047' if (u, v) in mst_edges or (v, u) in mst_edges else 'lightgray' for u, v in G_draw.edges()]
            edge_widths = [3.0 if (u, v) in mst_edges or (v, u) in mst_edges else 1.0 for u, v in G_draw.edges()]

    # ========================================================
    # ESCENARIO 3: WHAT-IF 1 (CIERRE BALDERAS)
    # ========================================================
    elif algoritmo == "3. What-If 1: Cierre de Balderas (Dijkstra)":
        st.warning(" SIMULACIÓN: Estación Balderas inhabilitada. Se aplica penalización M=9999 a sus arcos.")
        origen = st.selectbox("Origen:", list(G_base.nodes()), index=5)
        destino = st.selectbox("Destino:", list(G_base.nodes()), index=33)
        
        if st.button("Recalcular Ruta Alterna"):
            G_whatif = G_base.copy()
            # Aplicar penalización Big M
            for neighbor in list(G_whatif.neighbors('Balderas')):
                G_whatif['Balderas'][neighbor]['weight'] = 9999
                
            try:
                ruta = nx.dijkstra_path(G_whatif, origen, destino, weight='weight')
                costo = nx.dijkstra_path_length(G_whatif, origen, destino, weight='weight')
                st.success(f"**Nuevo Costo Total:** {costo} minutos")
                st.info(f"**Ruta Alterna:** {' ➔ '.join(ruta)}")
                
                G_draw = G_whatif
                ruta_edges = list(zip(ruta, ruta[1:]))
                
                edge_colors = []
                edge_widths = []
                edge_styles = []
                for u, v in G_draw.edges():
                    if (u, v) in ruta_edges or (v, u) in ruta_edges:
                        edge_colors.append('darkorange')
                        edge_widths.append(3.5)
                        edge_styles.append('solid')
                    elif u == 'Balderas' or v == 'Balderas':
                        edge_colors.append('red')
                        edge_widths.append(2.0)
                        edge_styles.append('dashed')
                    else:
                        edge_colors.append('lightgray')
                        edge_widths.append(1.0)
                        edge_styles.append('solid')
                        
            except nx.NetworkXNoPath:
                st.error("No hay ruta disponible.")

    # ========================================================
    # ESCENARIO 4: WHAT-IF 2 (MODERNIZACIÓN)
    # ========================================================
    elif algoritmo == "4. What-If 2: Modernización (Kruskal)":
        st.info(" SIMULACIÓN: Modernización de vías. Tramos Oceanía-C.Azteca y Pantitlán-La Paz optimizados.")
        if st.button("Recalcular Árbol"):
            G_whatif2 = G_base.copy()
            G_whatif2['Oceanía']['Ciudad Azteca']['weight'] = 5
            G_whatif2['Pantitlán']['La Paz']['weight'] = 6
            
            mst = nx.minimum_spanning_tree(G_whatif2, weight='weight', algorithm='kruskal')
            costo = sum(d['weight'] for u, v, d in mst.edges(data=True))
            st.success(f"**Nuevo Costo Total:** {costo} unidades")
            st.info("La topología se mantiene, pero el costo global disminuye gracias a la optimización de las ramificaciones terminales.")
            
            G_draw = G_whatif2
            mst_edges = list(mst.edges())
            
            edge_colors = []
            edge_widths = []
            for u, v in G_draw.edges():
                if ((u == 'Oceanía' and v == 'Ciudad Azteca') or (v == 'Oceanía' and u == 'Ciudad Azteca') or 
                    (u == 'Pantitlán' and v == 'La Paz') or (v == 'Pantitlán' and u == 'La Paz')):
                    edge_colors.append('cyan')
                    edge_widths.append(4.0)
                elif (u, v) in mst_edges or (v, u) in mst_edges:
                    edge_colors.append('#43B047')
                    edge_widths.append(3.0)
                else:
                    edge_colors.append('lightgray')
                    edge_widths.append(1.0)

# ========================================================
# RENDERIZADO DEL GRAFO
# ========================================================
with col2:
    if 'G_draw' in locals():
        fig, ax = plt.subplots(figsize=(14, 12))
        
        # Colorear nodo bloqueado en caso 3
        node_colors = ['#ffcccc' if n == 'Balderas' and algoritmo == "3. What-If 1: Cierre de Balderas (Dijkstra)" else 'white' for n in G_draw.nodes()]
        
        nx.draw_networkx_nodes(G_draw, pos, ax=ax, node_size=700, node_color=node_colors, edgecolors='black', linewidths=1.5)
        nx.draw_networkx_labels(G_draw, pos, ax=ax, font_size=8, font_weight='bold')
        
        # Dibujar aristas según el estilo de cada algoritmo
        if algoritmo == "3. What-If 1: Cierre de Balderas (Dijkstra)":
            for i, (u, v) in enumerate(G_draw.edges()):
                nx.draw_networkx_edges(G_draw, pos, edgelist=[(u, v)], ax=ax, 
                                       edge_color=edge_colors[i], width=edge_widths[i], style=edge_styles[i])
        else:
            nx.draw_networkx_edges(G_draw, pos, ax=ax, edge_color=edge_colors, width=edge_widths)
        
        # Etiquetas de peso especiales
        edge_labels = nx.get_edge_attributes(G_draw, 'weight')
        if algoritmo == "3. What-If 1: Cierre de Balderas (Dijkstra)":
            for k in edge_labels:
                if edge_labels[k] == 9999:
                    edge_labels[k] = 'M'
                    
        nx.draw_networkx_edge_labels(G_draw, pos, edge_labels=edge_labels, font_size=8, font_color='blue')
        
        plt.axis('off')
        st.pyplot(fig)
    else:
        st.info(" Selecciona una opción y presiona el botón para calcular y visualizar la red.")