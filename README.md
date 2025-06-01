
# RSRT-DETR: Hierarchical Polar Attention and Multi-Scale Hypergraph Networks for Dense Remote-Sensing Small-Object Detection

![RSRT-DETR Architecture](rsrtdetr.pdf)

## Introduction

**RSRT-DETR** is a lightweight and effective Transformer-based framework for dense small-object detection in UAV-borne remote sensing images. It integrates Polar Dynamic Spatial Fine-tuning (PDSF) Attention, Multi-Scale Hypergraph Feature Network (MS-HFNet), and HyperSemantic Fusion Network (HSFN), achieving state-of-the-art performance on challenging benchmarks (DOTAv1.0, VisDrone2019, NWPU VHR-10) while maintaining efficiency and low computational cost.

If you find this project helpful, please consider citing our paper and starring this repo!

---

## Features

* **Hierarchical Polar Attention**: Enhances fine-grained geometry and suppresses background noise.
* **Multi-Scale Hypergraph Reasoning**: Models high-order spatial relations to disambiguate cluttered targets.
* **Progressive Semantic Fusion**: Preserves cross-scale context and enhances robustness in complex scenes.
* **State-of-the-art Results**: Achieves top performance on DOTAv1.0, VisDrone2019, and NWPU VHR-10 datasets.
* **Lightweight and Fast**: Lower FLOPs and parameter count than most DETR variants.

---

## Benchmark Results

| Dataset      | AP<sub>50</sub> | AP<sub>S</sub> | Params (M) | FLOPs (G) |
| ------------ | :-------------: | :------------: | :--------: | :-------: |
| DOTAv1.0     |       69.7      |    **36.8**    |    64.9    |   200.8   |
| VisDrone2019 |       57.1      |    **17.2**    |    69.5    |   206.4   |
| NWPU VHR-10  |       95.4      |    **84.6**    |    65.4    |   201.1   |

---


## Contact

For questions and feedback, please contact:

* Yao Zhang (Corresponding Author): [2022210888@nefu.edu.cn](mailto:2022210888@nefu.edu.cn)

---
> **Note:** The full code and pre-trained models will be made publicly available upon the official acceptance of our paper by journal. Thank you for your interest!

