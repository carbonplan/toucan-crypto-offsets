import datetime
from pathlib import Path

import pandas as pd
import requests

OUTPUT_DIR = Path("/tmp")


def download_data():
    r = requests.post(
        "https://registry.verra.org/uiapi/asset/asset/search?$skip=0&format=csv",
        json={"program": "VCS", "issuanceTypeCodes": ["ISSUE"]},
    )
    data = r.json()["value"]
    return pd.DataFrame(data)


if __name__ == "__main__":
    utc_date = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    out_fname = OUTPUT_DIR / f"verra_{utc_date}.csv"

    print("Downloading Verra transactions")
    df = download_data()

    print(f"Writing Verra transactions to {out_fname}")
    df.to_csv(out_fname, index=False)
