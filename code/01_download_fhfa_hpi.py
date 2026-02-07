import os, requests

os.makedirs("data", exist_ok=True)

URL = "https://www.fhfa.gov/hpi/download/quarterly_datasets/hpi_at_metro.csv"
out_path = "data/hpi_at_metro.csv"

print("Downloading FHFA HPI metro (All-Transactions) CSV...")
r = requests.get(URL, timeout=120)
r.raise_for_status()

with open(out_path, "wb") as f:
    f.write(r.content)

print("Saved to:", out_path)