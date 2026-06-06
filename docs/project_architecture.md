# Project Architecture

## High Level Architecture

Customer Data
|
v
Raw Dataset
(data/raw)
|
v
preprocess.py
|
v
Processed Dataset
(data/processed)
|
v
train.py
|
v
model.pkl
(models/)
|
v
predict.py
|
v
Predictions

## Repository Structure

customer-churn-ml

data/
raw/
processed/

docs/
dataset_registry.md
project_architecture.md

models/

notebooks/

tests/

src/
train.py
predict.py
preprocess.py

requirements.txt
Dockerfile
README.md

## Future Architecture

GitHub
|
v
GitHub Actions
|
v
AWS
|
v
S3
|
v
Training Pipeline
|
v
Model Deployment

## Design Principles

1. Raw data is never modified.
2. Processed data is generated from raw data.
3. Models are generated from processed data.
4. Source code is version controlled in Git.
5. Large datasets should not be stored in Git.
