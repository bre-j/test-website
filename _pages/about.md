---
layout: about
title: about
permalink: /
subtitle: Computational and statistical models of <strong>brain dynamics</strong>. <a href="https://www.crm.cat/_neuroscience/">Centre de Recerca Matemàtica</a>, Barcelona &middot; <a href="https://cfin.au.dk/cfin-labs-research-groups/comand-computational-modelling-analysis-of-neuronal-dynamics">CFIN</a>, Aarhus University.

profile:
  align: right
  image: lab_hero.png
  image_circular: false # crops the image to make it circular
  more_info: >
    <p><strong>Centre de Recerca Matemàtica</strong></p>
    <p>Campus UAB, Edifici C</p>
    <p>08193 Bellaterra (Barcelona), Spain</p>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

We build **statistical and machine-learning models of how brain activity unfolds in time**, and we use them
to connect brain function to behaviour, cognition and disease.

Most analyses of neuroimaging data average over time: they describe the brain as a single, static pattern of
connectivity. But the brain is not static. Activity reorganises continuously, on timescales from tens of
milliseconds to minutes, and much of that reorganisation is spontaneous — it is not driven by anything in the
experiment. Our work asks what these ongoing dynamics are, how to estimate them reliably from noisy and
short recordings, and what they tell us about the individual person being scanned.

The group works across modalities — MEG, EEG, fMRI, ECoG and invasive electrophysiology — and along three
connected lines:

- **Methods.** Time-varying models of brain data: hidden Markov models and their Gaussian-linear
  generalisations, decoding methods for temporally variable responses, and the statistical machinery needed to
  test hypotheses about them. See our [software]({{ '/software/' | relative_url }}).
- **Basic science.** Spontaneous brain activity, its temporal structure, and how it shapes perception and
  cognition.
- **Clinical application.** Whole-brain, individual-level models of brain function in disease — from
  multiple sclerosis and Parkinson's to early markers of dementia.

A recurring theme is the move from group averages to **individual-level models**: fitting a model to one
person's data and using it to predict that person's traits, symptoms or outcome. Methods we have developed for
this, such as the [Fisher kernel]({{ '/publications/' | relative_url }}) and the
[glhmm toolbox](https://github.com/vidaurre/glhmm), are used well beyond our own group.

### Where we are

Diego Vidaurre joined the **Centre de Recerca Matemàtica (CRM)** in Barcelona in November 2025 through the
Spanish **ATRAE** talent programme, where he is a Principal Investigator in the
[Computational and Mathematical Neuroscience unit](https://www.crm.cat/_neuroscience/) and leads the project
*"A new integrative statistical framework to connect symptoms to mechanisms in brain disease."* He remains
Adjunct Professor at the **Center of Functionally Integrative Neuroscience (CFIN)**, Aarhus University, where
part of the group continues as the
[COMAND / Analysis Group](https://cfin.au.dk/cfin-labs-research-groups/comand-computational-modelling-analysis-of-neuronal-dynamics).
The group is currently split across the two sites; see [people]({{ '/people/' | relative_url }}).

### Joining us

We look for people with a strong quantitative background — mathematics, statistics, machine learning,
physics, engineering or computational neuroscience — who want to work on real neuroimaging data. If that
sounds like you, get in touch with Diego with a CV and a short note about what you would like to work on.
