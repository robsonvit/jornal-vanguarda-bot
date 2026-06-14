import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

FB_USER_TOKEN = os.environ.get("FB_USER_TOKEN") or os.environ.get("FB_TOKEN")

if not FB_USER_TOKEN:
    print("ERRO: FB_USER_TOKEN não encontrado.")
    exit(1)

url = f"https://graph.facebook.com/v22.0/me/accounts?access_token={FB_USER_TOKEN}"
try:
    res = requests.get(url).json()
    if "data" in res:
        for page in res["data"]:
            print(f"PAGE_NAME: {page.get('name')} | PAGE_ID: {page.get('id')}")
            # print(f"PAGE_TOKEN: {page.get('access_token')[:20]}...")
    else:
        print("Erro ao buscar páginas:", res)
except Exception as e:
    print("Erro de conexão:", e)
