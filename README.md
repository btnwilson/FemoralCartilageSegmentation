# Femoral Cartilage MRI Segmentation with U-Net and Adaptive Preprocessing

## Project Overview

This project was developed in collaboration with a UVM research lab to automate femoral cartilage segmentation from knee MRI scans. Manual cartilage segmentation is time-intensive and creates a major bottleneck for clinical researchers and undergraduate lab members working with musculoskeletal imaging data.

The goal of this work was to create a reproducible deep learning pipeline that could both improve segmentation accuracy and be easily retrained and maintained by future undergraduate researchers without rebuilding the workflow from scratch.

The project combines a U-Net segmentation model with preprocessing optimization to improve performance on difficult MRI slices and reduce manual annotation burden.

---

## Objectives

- Automate femoral cartilage segmentation from MRI scans
- Reduce manual annotation time for clinical researchers
- Create a maintainable workflow for future lab use
- Improve segmentation performance through adaptive preprocessing
- Evaluate preprocessing parameter selection using reinforcement learning-based optimization

---

## Methods

### Segmentation Model

A U-Net architecture was trained using paired MRI images and manually annotated cartilage masks. The model was implemented in Python using PyTorch and optimized for binary segmentation performance using Dice-based loss evaluation.

### Preprocessing Optimization

To improve segmentation consistency across varying image quality and contrast conditions, multiple preprocessing filters and parameter combinations were evaluated.

A reinforcement learning-style optimization workflow was used to identify preprocessing parameter combinations that improved downstream segmentation performance beyond the baseline U-Net.

### Evaluation

Model performance was evaluated using Dice score on held-out test data.

Because of the limited number of subjects available, train/validation/test splitting was performed at the slice level rather than the subject level. This supported stable model development, though subject-level validation would be preferred in a larger follow-up dataset to reduce potential leakage between adjacent slices.

---

## Results

- Baseline U-Net achieved strong segmentation performance on held-out MRI data
- Final model achieved a mean Dice score of **0.842**
- Adaptive preprocessing improved mean Dice score by approximately **5%** over baseline
- The workflow significantly reduced manual annotation burden for the research lab

---

## Tools Used

- Python
- PyTorch
- NumPy
- OpenCV
- Matplotlib
- Google Colab

---

## Project Significance

This project focused not only on model performance, but also on building a practical system that could be used and maintained by real lab members. The final notebook was designed to support reproducible retraining and deployment for future undergraduate researchers working in the lab.

This work reflects a broader interest in building machine learning systems that are not just accurate, but reliable, interpretable, and useful in real-world research environments.

---

## Future Work

- Expand dataset size for stronger generalization
- Move to subject-level train/test validation
- Improve preprocessing optimization strategies
- Explore 3D segmentation approaches for volumetric MRI data
- Package the workflow into a more modular training and inference pipeline
