from unittest import result
import streamlit as st

import search as s
query = st.text_input('Search', '')

if query:
    s.search(query)
    st.write('Search results for:', query)
    st.write(s.search(query))