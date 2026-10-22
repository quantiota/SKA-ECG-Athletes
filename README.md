# SKA ECG Athletes

 [![arXiv](https://img.shields.io/badge/arXiv-2503.13942-b31b1b)](https://arxiv.org/abs/2503.13942)   [![arXiv](https://img.shields.io/badge/arXiv-2504.03214-b31b1b)](https://arxiv.org/abs/2504.03214)   [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-SKA-orange)](https://huggingface.co/quant-iota) [![Sponsor](https://img.shields.io/badge/Sponsor-quantiota-ea4aaa?logo=github-sponsors)](https://github.com/sponsors/quantiota)


**Structured Knowledge Accumulation (SKA) on the heart of athletes at rest**

This project applies the SKA real-time learner to the resting ECG of athletes, from
[Sport DB 2.0](https://data.mendeley.com/datasets/kzkjkt7mx2/2) (Romagnoli et al., Computing in
Cardiology 2023, [doi:10.22489/CinC.2023.067](https://doi.org/10.22489/CinC.2023.067); CC BY 4.0).

The method is the one of
[SKA-ECG-Heart-Rate-Variability](https://github.com/quantiota/SKA-ECG-Heart-Rate-Variability):
the five waves of each cardiac cycle, the same input, the same learner, the same 3D cube.

## Data

The BioHarness 3.0 chest band records the raw ECG of the whole session at 250 Hz; each session
begins with a resting phase, given in the training notes of the dataset. The resting phase of
the 42 recordings (38 athletes: American football, cycling, running, soccer) is in
[`ecg-data-validation/`](ecg-data-validation/). 23 are learned; 19 are excluded: the chest band lost electrode contact (11) or a disease
is listed for the athlete (8) (see [`ska-ecg-engine/excluded/`](ska-ecg-engine/excluded/)).

## Folders

| folder | content |
|---|---|
| [`ecg-data-validation/`](ecg-data-validation/) | the resting phases, extracted from Sport DB 2.0 |
| [`ska-ecg-engine/`](ska-ecg-engine/) | the results and the cube builder |
| [`vr-library/`](vr-library/) | the cubes |

The SKA real-time engine is proprietary and is not included in this repository.
