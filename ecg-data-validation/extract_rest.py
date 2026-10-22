#!/usr/bin/env python3
"""The resting phase of every Sport DB 2.0 recording made with the BioHarness 3.0 chest band.

Sport DB 2.0 (Romagnoli et al., Computing in Cardiology 2023, doi:10.22489/CinC.2023.067;
Mendeley Data doi:10.17632/kzkjkt7mx2.2, CC BY 4.0). The BioHarness recordings hold the raw ECG
of the whole session (Data.ECG, 250 Hz); the resting phase is given in each TrNote.txt
("Resting: from 00:00:00 to hh:mm:ss"). Recordings without a resting phase (trekking) are skipped.

    python extract_rest.py <path to SportDB2/>
        -> data/<id>.csv.gz     sample, t (s), ecg (BioHarness raw units)
           data/records.csv     id, sport, subject, session, sex, age, disease, rest_s, samples

id = <sport>_<subject>, with _<session> when the subject has more than one session.
"""
import pathlib
import re
import sys

import numpy as np
import pandas as pd
import scipy.io as sio

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "data"
FS = 250


def seconds(hms):
    h, m, s = (int(v) for v in hms.split(":"))
    return 3600 * h + 60 * m + s


def main():
    src = pathlib.Path(sys.argv[1])
    OUT.mkdir(exist_ok=True)
    crds = sorted(src.rglob("CRD*"))
    rows = []
    for d in crds:
        data = sio.loadmat(d / "Data.mat", squeeze_me=True, struct_as_record=False)["Data"]
        if "BR" not in data._fieldnames:                              # not a BioHarness recording
            continue
        note = (d / "TrNote.txt").read_text(encoding="utf-8-sig", errors="ignore")
        m = re.search(r"Rest\w*\s*:\s*from\s*(\S+)\s*to\s*(\S+)", note, re.I)
        if not m:
            continue
        sport = d.parts[-3] if d.parts[-4] != "SOC" else d.parts[-4 + 1]
        subject, session = d.parts[-2], d.parts[-1]
        many = len([c for c in crds if c.parent == d.parent]) > 1
        rid = f"{sport.lower()}_{subject}" + (f"_{session.lower()}" if many else "")
        a, b = seconds(m.group(1)), seconds(m.group(2))
        ecg = np.asarray(data.ECG)[a * FS:b * FS]                     # as stored: uint16 (most sports) or float64 (cycling)
        n = np.arange(len(ecg))
        pd.DataFrame({"sample": n, "t": n / FS, "ecg": ecg}).to_csv(OUT / f"{rid}.csv.gz", index=False)
        dem = pd.read_csv(d / "Dem.txt", sep="\t")
        rows.append(dict(id=rid, sport=sport, subject=subject, session=session,
                         sex={0: "M", 1: "F"}.get(dem.Sex.iloc[0], "?"), age=dem.Age.iloc[0],
                         disease=dem.Disease.iloc[0], rest_s=b - a, samples=len(ecg)))
        print(f"{rid:14s} rest {b - a:5d} s  {len(ecg):,} samples")
    pd.DataFrame(rows).to_csv(OUT / "records.csv", index=False)
    print(f"{len(rows)} recordings -> {OUT}")


if __name__ == "__main__":
    main()
