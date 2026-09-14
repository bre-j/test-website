---
layout: page
title: statistics and prediction
description: Testing hypotheses about brain dynamics, and predicting individual traits from them.
img: assets/img/research_statistics.png
importance: 2
category: methods
related_publications: true
---

Fitting a model is the easy half. The harder half is saying, with a defensible error rate, what it means —
and doing so when the estimates are unstable, the observations within a subject are not exchangeable, and the
family of hypotheses is large.

**Inference.** Within-subject functional connectivity estimates are noisy, yet between-subject conclusions are
often drawn directly from them. We have worked on when that is and is not valid, and on permutation schemes
that respect the structure of the data — multi-level block permutation for family-structured cohorts such as
the Human Connectome Project, and, more recently, a general permutation-based framework for testing
hypotheses about brain dynamics that covers across-subject, across-trial and across-time designs.

**Prediction.** A model fitted to one person's data is a rich object, but it lives in a curved parameter
space, so feeding its parameters into a linear predictor is the wrong move. The **Fisher kernel** takes the
geometry seriously: it compares two subjects by how the model would have to change to account for each of
them. In practice this predicts individual traits more accurately — and, importantly, more _reliably_ — than
the alternatives, which matters if predictions are ever to be used at the level of a single person.

**Normative modelling.** Where pathology is diffuse rather than focal, comparing a patient against a
normative range one region at a time discards the thing that is actually abnormal. We argue for and develop
whole-brain normative approaches to brain function.

Methods from this line are implemented in [glhmm]({{ '/software/' | relative_url }}) and in the accompanying
statistical testing module.
