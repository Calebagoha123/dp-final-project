# Process Book

## Entries

### Date of entry: 12 May 2025
- **What I’ve worked on:** Set up the project structure and gathered initial datasets (`audio_features.csv`, `kaggle_dataset.csv`, `top_songs_by_year.csv`).
- **What problems I encountered:** Difficulty finding a credible source for hits from 2000–2024, as Spotify lacks official playlists for this range.
- **What I learned:** How to use the Spotify and Genius APIs and what data they provide.
- **Which resources did I use:** Kaggle datasets, Spotify API documentation.

### Date of entry: 13 May 2025
- **What I’ve worked on:** Ran scrapers to collect audio features and lyrics for songs from Spotify and Genius.
- **What problems I encountered:** Preventing the computer from sleeping during long scraping sessions.
- **What I learned:** How to set up a `.env` file for API keys, use exponential backoff for API rate limits, and use the `caffeinate` command on macOS to prevent sleep mode.
- **Which resources did I use:** Spotify and Genius API documentation, macOS terminal commands, Python requests library.

### Date of entry: 15 May 2025
- **What I’ve worked on:** Started cleaning and exploring the audio features dataset.
- **What problems I encountered:** Handling missing values and inconsistent column formats.
- **What I learned:** Basic imputation techniques and how to summarize distributions using Pandas.
- **Which resources did I use:** Pandas documentation, online data cleaning tutorials.

### Date of entry: 18 May 2025
- **What I’ve worked on:** Began text preprocessing for lyrics and conducted basic word frequency analysis.
- **What problems I encountered:** Special characters and punctuation caused issues in tokenization.
- **What I learned:** How to clean text using techniques such as stopword removal and lemmatization.
- **Which resources did I use:** NLTK documentation.

### Date of entry: 19 May 2025
- **What I’ve worked on:** Explored common word patterns and trends in lyrics across years.
- **What problems I encountered:** Grouping songs by year required handling duplicates and missing release dates.
- **What I learned:** How to group and merge datasets effectively in Pandas.
- **Which resources did I use:** Pandas documentation.

### Date of entry: 21 May 2025
- **What I’ve worked on:** Applied LDA topic modeling to the lyrics data.
- **What problems I encountered:** Low coherence scores and poor topic separation.
- **What I learned:** Importance of preprocessing quality and initial parameter tuning in topic models.
- **Which resources did I use:** Gensim documentation, Introdcution to Topic Modelling on YouTube (SICSS).

### Date of entry: 22 May 2025
- **What I’ve worked on:** Continued tuning vectorizer and LDA model parameters to improve results.
- **What problems I encountered:** Coherence improved, but interpretability remained an issue.
- **What I learned:** How to evaluate LDA models using coherence scores and visualize topics.
- **Which resources did I use:** Gensim tutorials, Python plotting libraries.

### Date of entry: 23 May 2025
- **What I've worked on:** Cleaned up notebooks for submission.
- **What problems I encountered:** N/A
- **What I learned:** N/A
- **Which resources did I use:** N/A