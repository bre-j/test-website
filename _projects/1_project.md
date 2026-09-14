---
layout: page
title: modelling brain dynamics
description: Time-varying models of neural activity — hidden Markov models and their generalisations.
img: assets/img/research_dynamics.png
importance: 1
category: methods
related_publications: true
---

Standard functional connectivity collapses a whole recording into one matrix. That is a strong assumption:
it says the relationships between brain areas hold still for the duration of the scan. They do not.

Our core methodological programme is a family of **time-varying models** that describe a recording as a
sequence of recurring states, each with its own distribution over the data. Fitting such a model gives two
things at once: a small set of network patterns that the brain revisits, and a moment-by-moment estimate of
which pattern is active. The approach works on fMRI, where states last seconds, and on M/EEG and invasive
electrophysiology, where they last tens to hundreds of milliseconds.

Lines of work here include:

- **The Gaussian-Linear HMM.** A generalisation that unifies several model variants — state-wise means,
  covariances, and regression relationships between two sets of variables — under one estimation framework,
  released as the [glhmm Python package]({{ '/software/' | relative_url }}).
- **Spectral and hierarchical structure.** States defined by frequency-specific phase coupling, and the
  observation that transitions between states are themselves organised — hierarchically in time, and, more
  recently, into structured cycles.
- **Dimensionality reduction inside the model.** Estimating a low-dimensional representation and the
  time-varying connectivity jointly, rather than as two separate steps.
- **Decoding that respects temporal variability.** Standard decoders assume a response is time-locked across
  trials. ADA relaxes that, allowing the timing of the response to vary.

The practical question running through all of it is **how much dynamics the data can actually support**.
Time-varying estimates are noisy, and a model that is too flexible will happily describe noise; much of our
methods work is about where that line sits.
