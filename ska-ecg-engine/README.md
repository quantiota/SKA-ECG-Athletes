# SKA learning on the resting ECG of athletes — results

This folder holds the **results** of the SKA engine on the resting phase of the athletes of
[Sport DB 2.0](../ecg-data-validation/): the learner's output for every step, the figures and the
cubes. The method is that of
[SKA-ECG-Heart-Rate-Variability](https://github.com/quantiota/SKA-ECG-Heart-Rate-Variability/tree/main/ska-ecg-engine):
five waves per cardiac cycle (P, Q, R, S, T), one step per wave, input Re ċ (cosine), scale 25,
one loop of up to 3,500 steps (fewer when the resting phase is shorter), at 250 Hz. Learning
starts 3 s into the resting phase. The engine code is not published.

| file | content |
|---|---|
| `results/<id>/ska_<id>_runs.csv` | the learner's output for every step |
| `results/<id>/complex_events_<id>.csv` | the waves and their phasors |
| `results/<id>/figures/` | H and P on the step index; the steps in (z, ż, P) |
| `results/tau_H.csv` | τ_H and N_H of every record |
| `vr/` | three cubes per record (P, missing waves tagged, Δt) |
| `excluded/` | 19 records not used: the chest band lost electrode contact (11), or a disease is listed in Dem.txt (8) |

τ_H = time for the learner to reach 90 % of its saturation on its slowest transition;
N_H = τ_H / T_c, in cardiac cycles. In run_S4 the slowest transition (P→Q) does not saturate.

| sport | record | sex | age | scale | steps | τ_H (min) | N_H (cycles) | figures | cube |
|---|---|---|---|---|---|---|---|---|---|
| American football | amf_S11 | M | 18 | 25 | 3,500 | 5.0 | 444 | [H, P](results/amf_S11/figures/ska_amf_S11_cdot_cos_scale25.png) · [3D](results/amf_S11/figures/bands3d_amf_S11_cdot_cos_scale25.png) | [cube](vr/ska_ecg_amf_S11_scale25_vr.html) |
| American football | amf_S12 | M | 27 | 25 | 3,500 | 8.1 | 634 | [H, P](results/amf_S12/figures/ska_amf_S12_cdot_cos_scale25.png) · [3D](results/amf_S12/figures/bands3d_amf_S12_cdot_cos_scale25.png) | [cube](vr/ska_ecg_amf_S12_scale25_vr.html) |
| American football | amf_S14 | M | 25 | 25 | 3,500 | 8.1 | 586 | [H, P](results/amf_S14/figures/ska_amf_S14_cdot_cos_scale25.png) · [3D](results/amf_S14/figures/bands3d_amf_S14_cdot_cos_scale25.png) | [cube](vr/ska_ecg_amf_S14_scale25_vr.html) |
| American football | amf_S15 | M | 23 | 25 | 3,500 | 7.5 | 522 | [H, P](results/amf_S15/figures/ska_amf_S15_cdot_cos_scale25.png) · [3D](results/amf_S15/figures/bands3d_amf_S15_cdot_cos_scale25.png) | [cube](vr/ska_ecg_amf_S15_scale25_vr.html) |
| American football | amf_S2 | M | 23 | 25 | 3,500 | 9.1 | 698 | [H, P](results/amf_S2/figures/ska_amf_S2_cdot_cos_scale25.png) · [3D](results/amf_S2/figures/bands3d_amf_S2_cdot_cos_scale25.png) | [cube](vr/ska_ecg_amf_S2_scale25_vr.html) |
| American football | amf_S3 | M | 21 | 25 | 3,500 | 6.4 | 562 | [H, P](results/amf_S3/figures/ska_amf_S3_cdot_cos_scale25.png) · [3D](results/amf_S3/figures/bands3d_amf_S3_cdot_cos_scale25.png) | [cube](vr/ska_ecg_amf_S3_scale25_vr.html) |
| American football | amf_S4 | M | 21 | 25 | 3,500 | 9.0 | 630 | [H, P](results/amf_S4/figures/ska_amf_S4_cdot_cos_scale25.png) · [3D](results/amf_S4/figures/bands3d_amf_S4_cdot_cos_scale25.png) | [cube](vr/ska_ecg_amf_S4_scale25_vr.html) |
| American football | amf_S5 | M | 25 | 25 | 3,500 | 6.1 | 488 | [H, P](results/amf_S5/figures/ska_amf_S5_cdot_cos_scale25.png) · [3D](results/amf_S5/figures/bands3d_amf_S5_cdot_cos_scale25.png) | [cube](vr/ska_ecg_amf_S5_scale25_vr.html) |
| American football | amf_S6 | M | 24 | 25 | 3,500 | 6.2 | 423 | [H, P](results/amf_S6/figures/ska_amf_S6_cdot_cos_scale25.png) · [3D](results/amf_S6/figures/bands3d_amf_S6_cdot_cos_scale25.png) | [cube](vr/ska_ecg_amf_S6_scale25_vr.html) |
| American football | amf_S7 | M | 25 | 25 | 3,500 | 7.2 | 500 | [H, P](results/amf_S7/figures/ska_amf_S7_cdot_cos_scale25.png) · [3D](results/amf_S7/figures/bands3d_amf_S7_cdot_cos_scale25.png) | [cube](vr/ska_ecg_amf_S7_scale25_vr.html) |
| American football | amf_S9 | M | 25 | 25 | 3,500 | 7.0 | 530 | [H, P](results/amf_S9/figures/ska_amf_S9_cdot_cos_scale25.png) · [3D](results/amf_S9/figures/bands3d_amf_S9_cdot_cos_scale25.png) | [cube](vr/ska_ecg_amf_S9_scale25_vr.html) |
| cycling | cyc_S1 | M | 20 | 25 | 3,500 | 7.9 | 576 | [H, P](results/cyc_S1/figures/ska_cyc_S1_cdot_cos_scale25.png) · [3D](results/cyc_S1/figures/bands3d_cyc_S1_cdot_cos_scale25.png) | [cube](vr/ska_ecg_cyc_S1_scale25_vr.html) |
| cycling | cyc_S8 | F | 22 | 25 | 3,500 | 7.9 | 553 | [H, P](results/cyc_S8/figures/ska_cyc_S8_cdot_cos_scale25.png) · [3D](results/cyc_S8/figures/bands3d_cyc_S8_cdot_cos_scale25.png) | [cube](vr/ska_ecg_cyc_S8_scale25_vr.html) |
| running | run_S1 | M | 21 | 25 | 3,500 | 7.4 | 583 | [H, P](results/run_S1/figures/ska_run_S1_cdot_cos_scale25.png) · [3D](results/run_S1/figures/bands3d_run_S1_cdot_cos_scale25.png) | [cube](vr/ska_ecg_run_S1_scale25_vr.html) |
| running | run_S10 | M | 22 | 25 | 3,500 | 4.9 | 473 | [H, P](results/run_S10/figures/ska_run_S10_cdot_cos_scale25.png) · [3D](results/run_S10/figures/bands3d_run_S10_cdot_cos_scale25.png) | [cube](vr/ska_ecg_run_S10_scale25_vr.html) |
| running | run_S2 | F | 21 | 25 | 3,500 | 8.3 | 685 | [H, P](results/run_S2/figures/ska_run_S2_cdot_cos_scale25.png) · [3D](results/run_S2/figures/bands3d_run_S2_cdot_cos_scale25.png) | [cube](vr/ska_ecg_run_S2_scale25_vr.html) |
| running | run_S3 | M | 22 | 25 | 3,500 | 5.2 | 473 | [H, P](results/run_S3/figures/ska_run_S3_cdot_cos_scale25.png) · [3D](results/run_S3/figures/bands3d_run_S3_cdot_cos_scale25.png) | [cube](vr/ska_ecg_run_S3_scale25_vr.html) |
| running | run_S4 | M | 21 | 25 | 2,679 | – | – | [H, P](results/run_S4/figures/ska_run_S4_cdot_cos_scale25.png) · [3D](results/run_S4/figures/bands3d_run_S4_cdot_cos_scale25.png) | [cube](vr/ska_ecg_run_S4_scale25_vr.html) |
| running | run_S5 | M | 21 | 25 | 3,500 | 9.5 | 679 | [H, P](results/run_S5/figures/ska_run_S5_cdot_cos_scale25.png) · [3D](results/run_S5/figures/bands3d_run_S5_cdot_cos_scale25.png) | [cube](vr/ska_ecg_run_S5_scale25_vr.html) |
| running | run_S6 | M | 20 | 25 | 3,500 | 6.6 | 520 | [H, P](results/run_S6/figures/ska_run_S6_cdot_cos_scale25.png) · [3D](results/run_S6/figures/bands3d_run_S6_cdot_cos_scale25.png) | [cube](vr/ska_ecg_run_S6_scale25_vr.html) |
| running | run_S7 | M | 22 | 25 | 3,500 | 7.4 | 664 | [H, P](results/run_S7/figures/ska_run_S7_cdot_cos_scale25.png) · [3D](results/run_S7/figures/bands3d_run_S7_cdot_cos_scale25.png) | [cube](vr/ska_ecg_run_S7_scale25_vr.html) |
| running | run_S8 | M | 20 | 25 | 3,500 | 7.2 | 671 | [H, P](results/run_S8/figures/ska_run_S8_cdot_cos_scale25.png) · [3D](results/run_S8/figures/bands3d_run_S8_cdot_cos_scale25.png) | [cube](vr/ska_ecg_run_S8_scale25_vr.html) |
| running | run_S9 | M | 21 | 25 | 3,500 | 3.5 | 384 | [H, P](results/run_S9/figures/ska_run_S9_cdot_cos_scale25.png) · [3D](results/run_S9/figures/bands3d_run_S9_cdot_cos_scale25.png) | [cube](vr/ska_ecg_run_S9_scale25_vr.html) |
