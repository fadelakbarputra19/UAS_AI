# YouTube Comment Sentiment Analysis Project

## Project Overview
This project implements a sentiment analysis system for YouTube comments using various deep learning models. The system analyzes comments from specific YouTube videos and classifies them into three categories: positive (1), negative (0), and neutral (2).

## Project Structure
- `youtube.py` & `scraping_youtube.py`: Scripts for scraping YouTube comments using the YouTube Data API
- Model Implementation Notebooks:
  - `UAS_GRU_SGD.ipynb`: GRU model with SGD optimizer
  - `UAS_GRU_ADAM.ipynb`: GRU model with Adam optimizer
  - `UAS_BILSTM_SGD.ipynb`: BiLSTM model with SGD optimizer
  - `UAS_BILSTM_ADAM.ipynb`: BiLSTM model with Adam optimizer
  - `UAS_TRANSFORMER.ipynb`: Transformer model implementation
- Visualization Files:
  - `sentiment_analysis.png`: Sentiment analysis visualization
  - `sentiment_count.png`: Sentiment distribution visualization
  - ROC curve plots for different models and sentiment classes
- `word2vec_training.ipynb`: Word2Vec model training for word embeddings
- `wikipedia.ipynb`: Additional data processing notebook
- `UAS_AI_Kelompok 2.pdf`: Project documentation

## API Keys and Dependencies
The project uses the following APIs and keys:
- YouTube Data API (requires API key)
  - Current implementation uses a placeholder key "developerkeyy"
  - **Note**: Replace with your own API key for production use

## Data Collection
- Comments are collected from specific YouTube videos (video IDs: "i7V5sI7gVAw", "tAqzxb6VCqs")
- Data is stored in both JSON and CSV formats
- Comments include metadata such as:
  - Author information
  - Timestamp
  - Like count
  - Comment text
  - Video ID
  - Public status
  - Sentiment label

## Model Architecture
The project implements multiple deep learning architectures:
1. GRU (Gated Recurrent Unit)
   - Implemented with both SGD and Adam optimizers
   - Includes dropout layers for regularization
2. BiLSTM (Bidirectional Long Short-Term Memory)
   - Implemented with both SGD and Adam optimizers
   - Uses bidirectional processing for better context understanding
3. Transformer
   - Modern architecture for sequence processing
   - Self-attention mechanism for better context understanding

## Model Performance
Performance metrics are visualized through:
- ROC curves for each sentiment class (positive, negative, neutral)
- Separate visualizations for different model-optimizer combinations
- Sentiment distribution analysis

## Dependencies
- Python 3.x
- Key libraries:
  - TensorFlow/Keras
  - Pandas
  - NumPy
  - Google API Client
  - scikit-learn
  - gensim
  - matplotlib

## Usage
1. Set up your YouTube API key in `youtube.py`
2. Run the scraping script to collect comments
3. Choose a model notebook based on your requirements
4. Follow the notebook cells to train and evaluate the model

## Security Note
- The current implementation uses a placeholder API key
- For production use, replace the API key with your own
- Store API keys securely using environment variables or a secure configuration management system

## Contributors
- Project by Kelompok 2
- See `UAS_AI_Kelompok 2.pdf` for detailed documentation

## License
[Add appropriate license information]