import os
import subprocess
import streamlit as st

# Clone the private repository using subprocess to avoid gitpython issues
if not os.path.exists('AIpersona'):
    subprocess.run(['git', 'clone', f'https://{os.getenv("GITHUB_TOKEN")}@github.com/vlsathvika/AIpersona.git', 'AIpersona'], check=True)

# Run the entire code_1.py script
exec(open('AIpersona/persona_s.py').read())
