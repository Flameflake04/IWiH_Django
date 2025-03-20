# Invisible Woman in Healthcare

## Overview
*Invisible Woman in Healthcare* is a Django-based web application designed to address and analyze gender bias in medical research. The platform evaluates research papers to determine whether they exhibit gender bias based on three criteria:
1. The frequency of male vs. female pronouns in the text.
2. The gender distribution of authors in the references.
3. The gender distribution of participants in the study.

## Features
- Upload PDF research papers for analysis.
- Visualize analysis results, including gender bias scores.
- Download sample PDFs for testing and understanding the analysis.

## Technologies Used
- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript

## Changelog:
- Version 1.0.0: Basic functionality of gender count and gender participant done. Have to hard-code author count because of Spacy & Numpy dependancy conflict.

### Prerequisites
- Python 3.x
- Django 3.x or higher
- Install the required dependencies using `pip`:

```bash
pip install -r requirement.txt
