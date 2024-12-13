# Predicting Amazon Product Quality with Customer Reviews

## Overview
This project focuses on developing a deep learning model to predict Amazon product quality based on customer reviews. The model utilizes Convolutional Neural Network (CNN) and Long Short-Term Memory (LSTM) models for text classification.

## Data Collection
- Scraper API is used to retrieve live streaming Amazon data.
- Steps for data collection:
  1. Set up Scraper API account.
  2. Configure the scraper.
  3. Make API requests.
  4. Process the data.
  5. Handle rate limits and errors.
  6. Ensure compliance with Amazon's terms of service.

## Algorithm Used
- CNN Model for text classification:
  - Input Layer, Embedding Layer, Convolutional Layers, Pooling Layers, Fully Connected Layers, Output Layer.
- LSTM Model for text classification:
  - Input Layer, Embedding Layer, LSTM Layers, Fully Connected Layers, Output Layer.
- Combination of CNN and LSTM models for improved accuracy in text classification tasks.

## Model Creation
- Deep Learning Approach using CNN & LSTM:
  - Tokenization, Padding Sequences, Model Building, Training, Predictions.

## Deployment
- Deployment through app.py using Flask for a web application.
- Global Deployment using Render: [Webpage Link](https://amazon-review.onrender.com)
- GitHub Repository: [GitHub Repo](https://github.com/abdullahfirdowsi/amazon-review)
