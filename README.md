# Data Share Administrator

This project simulates a data preparation pipeline for AI-based assessment systems. It demonstrates key data management tasks such as retrieval, merging, cleaning, and anonymisation.

## Features

- Merges student metadata with exam scores
- Cleans missing or invalid data
- Anonymises personally identifiable information
- Exports a clean, ready-for-AI dataset

## Tech Stack

- Python
- pandas
- Faker (used to generate mock data)

## Project Structure

```
AI-Assessment-Data-Prep/
├── data/
│   ├── student_metadata.csv
│   ├── exam_scores.csv
├── src/
│   └── data_pipeline.py
├── output/
│   └── cleaned_dataset.csv (created after running the script)
├── README.md
├── requirements.txt
```

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the data pipeline:

```bash
python src/data_pipeline.py
```

## Disclaimer

All datasets are **fictional** and generated for demonstration purposes only. No real student data is used.

## Relevance

This project demonstrates:

- Retrieval of raw data files (CSV-based exam scores and student metadata)
- Merging and reshaping of datasets to suit AI training requirements
- Data cleaning and quality assurance (handling nulls, validating score ranges)
- Anonymisation of sensitive student data to comply with GDPR
- Output of clean, structured datasets ready for use in AI systems
  
This end-to-end example showcases my readiness to support organisations with real-life data operations and a strong focus on privacy, quality, and structure.
