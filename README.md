# GEO Competitor Bot

Automated competitive analysis generator for DataStealth. Parses deep research
markdown and outputs structured, client-facing comparison tables for each competitor.

## Problem

Sales and GTM teams spend hours manually researching competitors and formatting
battlecards. This bot takes a structured research file and generates per-competitor
markdown reports in seconds.

## How it works

1. Feed in `deep_research.md` — a tab-separated file mapping data security problems
   to competitor approaches and DataStealth's advantage
2. The parser extracts problem-by-problem breakdowns for each competitor
3. Individual markdown comparison files are generated in `/reports`

Supports 10 competitors out of the box: BigID, DataSunrise, Fortanix, Netwrix,
Privacera, Protegrity, Securiti, Sentra, Cyera, Varonis.

## Usage
```bash
python dsp_generator.py
```

Output files are saved to `./reports/datastealth_vs_<competitor>.md`.

## Input format

`deep_research.md` should contain numbered problems with tab-separated rows:
```
1. Problem Title
CompetitorName	How they solve it	Why DataStealth wins
```

## Stack

Python · Regex parsing · Pathlib · Markdown generation

## Context

Built during a Product Engineering internship at DataStealth to eliminate manual
competitive research workflows.
