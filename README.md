# Phishing Email Detection System

## Overview
This project is a Machine Learning-based Phishing Email Detection System built using Python and Scikit-learn. It classifies emails as **Phishing** or **Safe** based on text content and URL patterns.

---

## Features
- TF-IDF text feature extraction
- Naive Bayes classification model
- Detects phishing and safe emails
- Displays accuracy score
- Shows confusion matrix
- URL detection feature
- Suspicious keyword detection

---

## Dataset
The dataset contains sample emails labeled as:
- phishing
- safe

It is used to train the machine learning model.

---

## Technologies Used
- Python
- Pandas
- Scikit-learn

---

## How to Install

```bash
pip install pandas scikit-learn

## How to Run
python phishing_detector.py

## Example Input
http://fake-bank-login.com verify your account now

## Example Output
⚠ Warning: URL detected in email

Keyword Analysis:
- Suspicious keyword found: click
- Suspicious keyword found: verify
- Suspicious keyword found: bank

Final Result:
🚨 PHISHING EMAIL