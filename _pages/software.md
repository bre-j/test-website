---
layout: page
permalink: /software/
title: software
description: Open-source toolboxes from the group and from close collaborators.
nav: true
nav_order: 5
---

Methods are only useful if other people can run them. Everything below is open source.

## glhmm

**Gaussian-Linear Hidden Markov Models — Python.**
The group's main toolbox. It fits a family of HMMs based on Gaussian distributions to time series data
(fMRI, MEG, EEG, ECoG) and relates the resulting dynamics to non-brain variables such as behaviour or
physiology. It covers the standard state-mean and state-covariance models, the Gaussian-linear
(regression) variant, and the permutation-based statistical testing framework. GPU acceleration is available
through CuPy, and a companion GUI allows the main analyses to be run without writing code.

```bash
pip install glhmm
```

- Code: [github.com/vidaurre/glhmm](https://github.com/vidaurre/glhmm)
- Documentation and tutorial notebooks: [glhmm.readthedocs.io](https://glhmm.readthedocs.io/)
- Paper: _The Gaussian-linear hidden Markov model: a Python package_, **Imaging Neuroscience** (2025) —
  [MIT Press](https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00460/127499/The-Gaussian-linear-hidden-Markov-model-A) ·
  [arXiv:2312.07151](https://arxiv.org/abs/2312.07151)
- Licence: GPL-3.0

If you use glhmm in published work, please cite the Imaging Neuroscience paper.

## Statistical testing for brain dynamics

The permutation framework described in _A comprehensive framework for statistical testing of brain dynamics_
(**Nature Protocols**, 2026) ships as part of glhmm. It handles across-subject, across-trial and across-time
designs, and the family-structured permutation schemes needed for cohorts such as the Human Connectome
Project.

- Protocol: [Nature Protocols](https://www.nature.com/articles/s41596-025-01300-2)
- Preprint: [arXiv:2505.02541](https://arxiv.org/abs/2505.02541)

## HMM-MAR

**MATLAB.** The original toolbox for segmentation and characterisation of transient connectivity, including
the time-delay embedded and multivariate autoregressive observation models behind much of our earlier work on
M/EEG. It is the reference implementation for several of the spectral analyses, but it is no longer actively
supported — **new projects should start with glhmm**.

- Code: [github.com/OHBA-analysis/HMM-MAR](https://github.com/OHBA-analysis/HMM-MAR)

## Related work from collaborators

- **osl-dynamics** — a Python toolbox for modelling fast dynamic brain activity, from the OHBA group in
  Oxford (Gohil et al., _eLife_, 2024): [github.com/OHBA-analysis/osl-dynamics](https://github.com/OHBA-analysis/osl-dynamics)
- **NetsPredict** — prediction of behavioural variables from network/connectivity matrices:
  [github.com/vidaurre/NetsPredict](https://github.com/vidaurre/NetsPredict)

Other code accompanying individual papers is on [Diego's GitHub profile](https://github.com/vidaurre).
