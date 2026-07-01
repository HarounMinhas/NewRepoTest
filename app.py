"""Streamlit-app om Excel-bestanden te importeren en waarden te tonen."""

from __future__ import annotations

import pandas as pd
import streamlit as st


st.set_page_config(page_title="Excel importeren", page_icon="📊", layout="wide")

st.title("📊 Excel importeren en waarden tonen")
st.write(
    "Upload een Excel-bestand (`.xlsx` of `.xls`) om de tabbladen te bekijken "
    "en de waarden in een tabel te tonen."
)

uploaded_file = st.file_uploader("Kies een Excel-bestand", type=["xlsx", "xls"])

if uploaded_file is None:
    st.info("Upload een Excel-bestand om te beginnen.")
    st.stop()

try:
    excel_file = pd.ExcelFile(uploaded_file)
except Exception as exc:  # noqa: BLE001 - toon leesbare foutmelding in de UI
    st.error(f"Het bestand kon niet worden gelezen als Excel-bestand: {exc}")
    st.stop()

sheet_name = st.selectbox("Kies een tabblad", excel_file.sheet_names)

try:
    data = pd.read_excel(excel_file, sheet_name=sheet_name)
except Exception as exc:  # noqa: BLE001 - toon leesbare foutmelding in de UI
    st.error(f"Het tabblad kon niet worden ingelezen: {exc}")
    st.stop()

st.subheader(f"Waarden uit tabblad: {sheet_name}")

if data.empty:
    st.warning("Dit tabblad bevat geen waarden.")
else:
    st.dataframe(data, use_container_width=True)

    st.caption(f"Aantal rijen: {len(data)} | Aantal kolommen: {len(data.columns)}")

    with st.expander("Kolommen"):
        st.write(list(data.columns))
