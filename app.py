import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title=" 사과 재배지 및 경제 지표 대시보드", layout="wide")

st.title(" 사과 재배지 및 경제 지표 대시보드")
st.markdown("""
한국 주요 **사과 재배 지역**의 생산량과 **경제 지표(GDP, 실업률)**을  
지리 정보(GIS)와 함께 시각화한 대시보드입니다.  
데이터는 예시용으로 구성되어 있습니다.
""")

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("apple_data.csv")
geo = gpd.read_file("apple_region.geojson")

# -----------------------------
# Folium 지도 생성
# -----------------------------
m = folium.Map(location=[36.5, 128.5], zoom_start=8)

for _, row in geo.iterrows():
    region_data = df[df["region"] == row["region"]].iloc[0]
    popup_text = f"""
    <b>{row['region']}</b><br>
    생산량: {region_data['production_tons']}톤<br>
    1인당 GDP: ${region_data['gdp_per_capita']:,}<br>
    실업률: {region_data['unemployment_rate']}%
    """
    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=region_data['production_tons'] / 600,
        color="crimson",
        fill=True,
        fill_opacity=0.7,
        popup=folium.Popup(popup_text, max_width=250)
    ).add_to(m)

st_folium(m, width=900, height=600)

# -----------------------------
# 데이터 표 + 요약 통계
# -----------------------------
st.subheader(" 지역별 사과 및 경제 데이터")
st.dataframe(df)

avg_gdp = df["gdp_per_capita"].mean()
avg_unemp = df["unemployment_rate"].mean()
st.markdown(f"""
**평균 1인당 GDP:** ${avg_gdp:,.0f}  
**평균 실업률:** {avg_unemp:.1f}%
""")

# -----------------------------
# 그래프 비교
# -----------------------------
st.subheader("경제 지표 비교")

col1, col2 = st.columns(2)
with col1:
    st.bar_chart(df.set_index("region")["gdp_per_capita"], width="stretch")
with col2:
    st.bar_chart(df.set_index("region")["unemployment_rate"], width="stretch")

st.caption(" 예시 데이터 기반의 데모 대시보드입니다.")
