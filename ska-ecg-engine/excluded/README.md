# Excluded records

These 19 records were learned like the others (scale 25), but they are not used, for one of two
reasons.

## Poor ECG (11)

amf_S13, cyc_S2, cyc_S3, cyc_S4, cyc_S5, cyc_S6, cyc_S7, cyc_S9, cyc_S10, cyc_S11, cyc_S12

In long stretches of their resting phase the chest band lost electrode contact. The ECG is then
flat (clipped), drifting or swinging, with gaps of up to 10 s in which no cardiac cycle can be
found. The band's own heart rate (`Data.HR`) reads 0 for 20–88 % of the cyclists' rest. In these
records only 22–78 % of the rest time has R–R intervals between 0.4 and 1.5 s. In the kept records
it is above 94 %.

## Disease listed (8)

amf_S1 (Diabetes), amf_S8 (Asthma), amf_S10 (Tachycardia); soc3_S1_crd1 … crd5, one athlete in
five sessions (Atrial stenosis, Tachycardia)

The `Disease` field of the athlete's `Dem.txt` in Sport DB 2.0 names a disease; the Sport DB
paper lists these athletes as not healthy. The repository keeps only healthy athletes.

## Files

| folder | content |
|---|---|
| `results/<id>/` | learning results, as in `../results/` |
| `vr/` | their cubes |
| `tau_H_excluded.csv` | their τ_H and N_H |
| `signal_check/rate_check.csv` | all 42 records: the band's median heart rate and its share of zeros, and the detected cycles/min |
| `signal_check/cyc_<subject>_peaks.png` | each cyclist's ECG over three 10 s windows, with the detected P, R and T peaks (cyc_S1 and cyc_S8 are kept, for comparison) |
