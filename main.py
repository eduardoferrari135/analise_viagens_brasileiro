import pandas as pd
import plotly.express as px


def main():
    # Dicionário mestre de coordenadas (Lat, Lon)
    # Mapeia nomes canônicos para a localização real

    df = pd.read_csv("data2.csv")

    df["arena_lower"] = df["arena"].apply(
        lambda x: x.replace("*(PF)", "")
        .replace("(*PF)", "")
        .replace("(PF)", "")
        .replace("\xa0", "")
        .lower()
        .strip()
    )
    df_coords = pd.read_csv("arena_coords.csv")

    df_plot = df.merge(
        df_coords, left_on="arena_lower", right_on="estadio_original", how="left"
    )

    breakpoint()

    fig = px.scatter_mapbox(
        df_plot,
        lat="latitude",
        lon="longitude",
        # O que aparece ao passar o mouse:
        hover_name="arena",
        hover_data={"latitude": False, "longitude": False},
        zoom=3,  # Zoom inicial para focar no Brasil
        center={
            "lat": -15.793889,
            "lon": -47.882778,
        },  # Centro aproximado do Brasil (Brasília)
        color_discrete_sequence=["blue"],  # Cor dos pontos
        size_max=15,
        title="Mapa de Estádios de Futebol no Brasil",
    )

    # Define o estilo do mapa (existem outros como "open-street-map", "carto-darkmatter")
    fig.update_layout(
        mapbox_style="carto-positron",
        margin={
            "r": 0,
            "t": 40,
            "l": 0,
            "b": 0,
        },  # Margens para aproveitar melhor a tela
    )
    fig.show()


if __name__ == "__main__":
    main()
