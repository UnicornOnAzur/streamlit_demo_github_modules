# Standard library
import os
import subprocess
import sys
import time
# Third party
import streamlit as st


st.set_page_config(layout="wide")
st.title("Demonstration of accessing Github repository")

left, right = st.columns(2)
left.header("Use a public repository")
try:
    from public_repository import code as public_code
    public_code.make_dataframe(left)
    public_code.make_graph(left)
except ImportError as ie:
    left.write(f"could not import public_repository : {ie}")
#
right.header("Use a private repository")
try:
    from private_repository import code as private_code
    private_code.make_dataframe(right)
    private_code.make_graph(right)
except ImportError as ie:
    right.write(f"could not import private_repositoy : {ie}")
