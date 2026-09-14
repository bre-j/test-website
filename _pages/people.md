---
layout: page
title: people
permalink: /people/
description: The group is currently split between the Centre de Recerca Matemàtica in Barcelona and CFIN in Aarhus.
nav: true
nav_order: 2
---

<style>
  .lab-people { margin-top: 1.5rem; }
  .lab-people h2.site-heading {
    font-size: 1.15rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    opacity: 0.6;
    margin: 2.5rem 0 0.25rem;
  }
  .lab-people .site-where { font-size: 0.9rem; opacity: 0.6; margin-bottom: 1.25rem; }
  .lab-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1.25rem;
  }
  .lab-card {
    display: flex;
    gap: 0.9rem;
    align-items: flex-start;
    padding: 0.9rem 1rem;
    border: 1px solid rgba(128, 128, 128, 0.25);
    border-radius: 10px;
  }
  .lab-card.pi { grid-column: 1 / -1; }
  .lab-avatar {
    flex: 0 0 auto;
    width: 46px;
    height: 46px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    font-size: 0.95rem;
    letter-spacing: 0.03em;
    background: rgba(128, 128, 128, 0.16);
  }
  .lab-card.pi .lab-avatar { width: 64px; height: 64px; font-size: 1.2rem; }
  .lab-name { font-weight: 600; line-height: 1.3; }
  .lab-role { font-size: 0.88rem; opacity: 0.75; }
  .lab-meta { font-size: 0.82rem; opacity: 0.65; margin-top: 0.35rem; }
  .lab-collab { columns: 2; column-gap: 2rem; font-size: 0.9rem; }
  .lab-collab li { break-inside: avoid; margin-bottom: 0.35rem; }
  @media (max-width: 576px) {
    .lab-collab { columns: 1; }
  }
</style>

{% assign m = site.data.members %}

<div class="lab-people">

{% for person in m.pi %}

  <div class="lab-grid">
    <div class="lab-card pi">
      {% assign parts = person.name | split: " " %}
      {% assign firstinitial = parts.first | slice: 0 %}
      {% assign lastinitial = parts.last | slice: 0 %}
      <div class="lab-avatar">{{ firstinitial }}{{ lastinitial }}</div>
      <div>
        <div class="lab-name">
          {% if person.url %}<a href="{{ person.url }}">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}
        </div>
        <div class="lab-role">{{ person.role }}</div>
        {% if person.title %}<div class="lab-meta">{{ person.title }}</div>{% endif %}
        {% if person.interests %}<div class="lab-meta">{{ person.interests }}</div>{% endif %}
        {% if person.email %}<div class="lab-meta">{{ person.email }}</div>{% endif %}
      </div>
    </div>
  </div>
  {% endfor %}

  <h2 class="site-heading">Barcelona</h2>
  <div class="site-where">Centre de Recerca Matemàtica, Campus UAB</div>
  <div class="lab-grid">
    {% for person in m.barcelona %}
    <div class="lab-card">
      {% assign parts = person.name | split: " " %}
      {% assign firstinitial = parts.first | slice: 0 %}
      {% assign lastinitial = parts.last | slice: 0 %}
      <div class="lab-avatar">{{ firstinitial }}{{ lastinitial }}</div>
      <div>
        <div class="lab-name">{{ person.name }}</div>
        <div class="lab-role">{{ person.role }}</div>
        {% if person.interests %}<div class="lab-meta">{{ person.interests }}</div>{% endif %}
        {% if person.email %}<div class="lab-meta">{{ person.email }}</div>{% endif %}
      </div>
    </div>
    {% endfor %}
  </div>

  <h2 class="site-heading">Aarhus</h2>
  <div class="site-where">Center of Functionally Integrative Neuroscience, Aarhus University</div>
  <div class="lab-grid">
    {% for person in m.aarhus %}
    <div class="lab-card">
      {% assign parts = person.name | split: " " %}
      {% assign firstinitial = parts.first | slice: 0 %}
      {% assign lastinitial = parts.last | slice: 0 %}
      <div class="lab-avatar">{{ firstinitial }}{{ lastinitial }}</div>
      <div>
        <div class="lab-name">{{ person.name }}</div>
        <div class="lab-role">{{ person.role }}</div>
        {% if person.interests %}<div class="lab-meta">{{ person.interests }}</div>{% endif %}
        {% if person.email %}<div class="lab-meta">{{ person.email }}</div>{% endif %}
      </div>
    </div>
    {% endfor %}
  </div>

  <h2 class="site-heading">Frequent collaborators</h2>
  <div class="site-where">People we publish with regularly, outside the group.</div>
  <ul class="lab-collab">
    {% for c in m.collaborators %}
    <li>{{ c.name }} <span style="opacity: 0.6">— {{ c.affiliation }}</span></li>
    {% endfor %}
  </ul>
</div>

---

Group membership changes; the authoritative rosters are the
[CRM Computational and Mathematical Neuroscience page](https://www.crm.cat/_neuroscience/) and the
[CFIN Analysis Group people page](https://cfin.au.dk/cfin-labs-research-groups/comand-computational-modelling-analysis-of-neuronal-dynamics/people).
To edit this page, change `_data/members.yml` — nothing else needs touching.
