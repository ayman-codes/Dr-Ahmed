import requests

# LOAD CSS
css = 'https://raw.githubusercontent.com/ayman-codes/Dr-Ahmed/main/styles/main.css?token=GHSAT0AAAAAAB5ORJB4BMPALOMCLU22Y3Q2Y6P2AYA'
# --- LOAD CSS from github ---
response_css = requests.get(css)
print(response_css.text)