import streamlit as st

from supabase import create_client, Client

supabase_url = st.secrets["SUPERBASE_UPL"]
supabase_key = st.secrets["SUPERBASE_KEY"]

supabase = create_client(
    supabase_url,
    supabase_key
)