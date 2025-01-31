import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime
import subprocess

load_dotenv()

# Configuration
CRYPTO_IDS = ["bitcoin", "ethereum", "solana"]
OUTPUT_FILE = "crypto_prices.json"
GITHUB_REPO_PATH = os.getenv("GITHUB_REPO_PATH")  

# Récupérer les prix depuis CoinGecko
url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(CRYPTO_IDS)}&vs_currencies=usd"
response = requests.get(url)
data = response.json()

# Ajouter un timestamp
data["timestamp"] = datetime.now().isoformat()

# Charger les anciennes données (si existent)
if os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, "r") as f:
        old_data = json.load(f)
else:
    old_data = []

# Ajouter les nouvelles données
old_data.append(data)

# Sauvegarder dans le fichier
with open(OUTPUT_FILE, "w") as f:
    json.dump(old_data, f, indent=4)

# Automatiser le commit et le push
def git_commit_and_push():
    try:
        os.chdir(GITHUB_REPO_PATH)
        subprocess.run(["git", "add", OUTPUT_FILE], check=True)
        subprocess.run(["git", "commit", "-m", f"Update prices {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"], check=True)
        
         # Push avec tracking de la branche principale
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

        print("Push effectué avec succès ! 🚀")

    except subprocess.CalledProcessError as e:
        print("❌ Erreur lors du push Git :", e)

git_commit_and_push()
