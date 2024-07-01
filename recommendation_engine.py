import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def setup_recommendation_engine(job_descriptions):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(job_descriptions)
    return tfidf_vectorizer, tfidf_matrix

def recommend_jobs(user_preferences, tfidf_vectorizer, tfidf_matrix, jobs_df, top_n=5):
    user_tfidf = tfidf_vectorizer.transform([user_preferences])
    cosine_sim = cosine_similarity(user_tfidf, tfidf_matrix)
    top_job_indices = cosine_sim[0].argsort()[-top_n:][::-1]
    return jobs_df.iloc[top_job_indices]
