# Day 1 – Streamlit 기반 GIS 대시보드 만들기

## 수업 목표
파이썬으로 데이터를 불러와 시각화하고, 지도 + 그래프 + 표를 결합한 간단한 웹앱을 완성한다.

- Day 1: 개념 설명 + 코드 실습  
- Day 2: 조합 및 응용 프로젝트 완성  

---

## 1. 환경 설정

### Python 설치  
https://www.python.org/downloads/

### 필수 라이브러리 설치
```bash
pip install streamlit pandas geopandas folium streamlit-folium plotly
```

### 실행 방법
```bash
cd "폴더경로"
python -m streamlit run app.py
```

2. 폴더 구조
## 2. 폴더 구조
```plaintext
apple-dashboard-day1/
├── app.py
├── apple_data.csv
├── apple_region.geojson
└── README.md
```

4. 결과 예시
<img width="1269" src="https://github.com/user-attachments/assets/e3521174-7c7a-4772-abb9-39aeedc114ea" />	Streamlit 실행 초기화면
<img width="1776" src="https://github.com/user-attachments/assets/49e858b7-31a3-429a-a79d-dea25cfc457a" />	데이터 및 그래프 표시 예시

