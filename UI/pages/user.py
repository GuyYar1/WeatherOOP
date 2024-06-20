import streamlit as st
import UI.menu
import pdb
from UI.pages.service_add_root import Serviceaddroot

# Redirect to app.py if not logged in, otherwise show the navigation menu
Serviceaddroot.support_abs_sys_path()

st.title("This page is available to all users")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
