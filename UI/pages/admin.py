import streamlit as st
import UI.menu
from UI.pages.service_add_root import Serviceaddroot

# Redirect to app.py if not logged in, otherwise show the navigation menu
Serviceaddroot.support_abs_sys_path()

# Verify the user's role
if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("This page is available to all admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
