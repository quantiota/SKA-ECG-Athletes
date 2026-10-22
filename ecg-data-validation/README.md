# The resting phases

Source: [Sport DB 2.0](https://data.mendeley.com/datasets/kzkjkt7mx2/2), Mendeley Data,
doi:10.17632/kzkjkt7mx2.2, CC BY 4.0 — Romagnoli S., Sbrollini A., Nocera A., Morettini M.,
Gambi E., Bondi D., Pietrangelo T., Verratti V., Burattini L., "Sport DB 2.0: a New Database of
Data Acquired by Wearable and Portable Devices while Practicing Sport", Computing in Cardiology
50 (2023), doi:10.22489/CinC.2023.067.

Only the recordings of the BioHarness 3.0 chest band (raw ECG, 250 Hz, the whole session) are
used; the resting phase of each is read from its training note (`TrNote.txt`). The trekking
recordings have no resting phase and are not used.

```
python extract_rest.py <path to SportDB2/>     # the folder of SportDB2.zip, unzipped
```

| file | content |
|---|---|
| `data/<id>.csv.gz` | sample, t (s), ecg as stored in Data.ECG (integers around 2,000 for American football, running and soccer; decimals around 2.0 for cycling; the dataset gives no unit) |
| `data/records.csv` | id, sport, subject, session, sex, age, disease, rest_s, samples (from `Dem.txt` and `TrNote.txt`) |

`id` = sport_subject, with the session when the subject has more than one (soc3_S1_crd1 … crd5).
