from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume = "python java data structures machine learning data visualization react"
job = "looking for python developer with machine learning and data analysis skills"

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([resume, job])
score = cosine_similarity(vectors[0], vectors[1])[0][0]

print(f"Match score: {round(score * 100, 2)}%")