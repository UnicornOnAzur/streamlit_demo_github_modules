# Standard library
import glob
import os
import subprocess
import sys
import time
# Third party
import streamlit as st

st.set_page_config(layout="wide")  # <>
st.title("Demonstration of accessing Github repository")  # <>
left, right = st.columns(2)  # Split the main page in two columns

# LEFT SIDE with the public repository
left.header("Use a public repository")
try:
    from public_repository import code as public_code
    public_code.make_dataframe(left)
    public_code.make_graph(left)
except ImportError as ie:
    left.write(f"could not import public_repository : {ie}")

# RIGHT SIDE with the private repository
right.header("Use a private repository")
token = os.environ.get("token")  # get the token from the environment\
right.write(sys.executable)
right.write(os.getcwd())
result = subprocess.Popen(
    [(f'{sys.executable}'
        f" -m pip install -- target {os.getcwd()} "
        f'git+https://{token}@github.com/UnicornOnAzur/closed_repository.git')
     ],
    shell=True)
# # wait for subprocess to install package before running your actual code below
# time.sleep(30)
# right.write(os.listdir())
# time.sleep(30)
# right.write(os.listdir())
try:
    from private_repository import code as private_code
    private_code.make_dataframe(right)
    private_code.make_graph(right)
except ImportError as ie:
    right.write(f"could not import private_repositoy : {ie}")
