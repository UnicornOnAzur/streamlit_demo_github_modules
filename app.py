# Standard library
import os
import subprocess
import sys
import time
# Third party
import streamlit as st

st.set_page_config(layout="wide")  # <>
st.title("Demonstration of accessing Github repository")  # <TODO>
left, right = st.columns(2)  # Split the main page in two columns

# LEFT SIDE with the public repository
left.header("Use a public repository")
try:
    from public_repository import code as public_code
    public_code.create_empty_dataframe(left)
    public_code.display_treemap(left)
except ImportError as ie:
    left.write(f"could not import public_repository : {ie}")

# RIGHT SIDE with the private repository
right.header("Use a private repository")
try:
    from private_repository import code as private_code
except ModuleNotFoundError:
    sleep_time = 90
    dependency_warning = right.warning(
        f"Installing dependencies, this takes {sleep_time} seconds."
    )
    token = os.environ.get("token")  # get the token from the environment
    parent_directory: str = os.path.dirname(os.getcwd())  # <TODO>
# with open(f"{parent_directory}/pyproject.toml", "w") as file:
#     file.write("[project]\n")
#     file.write('name = "closed_repository"\n')
#     file.write('version = "0.0.1"\n')
    with open(f"{parent_directory}/setup.py", "w") as file:
        file.write("import setuptools\n")
        file.write(("setuptools.setup(name='test',"
                    " install_requires=['closed_repository'])\n"))
    result = subprocess.Popen(
        [(f'{sys.executable}'
            f" -m pip install -- target {parent_directory} "
            f'git+https://{token}@github.com/UnicornOnAzur/closed_repository.git')
         ],
        shell=True)
    time.sleep(sleep_time)
    dependency_warning.empty()
try:
    from private_repository import code as private_code
    private_code.create_empty_dataframe(right)
    private_code.display_treemap(right)
except ImportError as ie:
    right.write(f"could not import private_repositoy : {ie}")
