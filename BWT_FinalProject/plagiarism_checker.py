import string
import nltk
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')  # For WordNet lemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Streamlit application title and image
st.image('https://infobeat.com/wp-content/uploads/2018/08/featured-image.png')
st.title("Plagiarism Checker")

# Function to preprocess text
def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = word_tokenize(text.lower())  # Tokenize and lower the case
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    preprocessed_text = ' '.join(filtered_tokens)
    return preprocessed_text

# Function to load and preprocess documents from a file
@st.cache_data
def load_documents(file):
    documents = []
    # Read the uploaded file as text
    content = file.read().decode('utf-8')
    for line in content.splitlines():
        documents.append(preprocess_text(line.strip()))  # Preprocess each line
    return documents

# File upload in Streamlit
uploaded_file = st.file_uploader("Upload a document to compare:", type=None)  # Allow all file types
user_text = st.text_area("Enter text for plagiarism check:")

# Button to trigger the plagiarism check
if st.button("Check for Plagiarism"):
    if uploaded_file and user_text:
        try:
            documents = load_documents(uploaded_file)  # Load and preprocess documents
            st.success("Documents loaded and preprocessed successfully!")
            
            preprocessed_user_text = preprocess_text(user_text)

            # TfidfVectorizer for similarity check
            vectorizer = TfidfVectorizer()
            tfidf_vectors = vectorizer.fit_transform(documents)
            user_tfidf_vector = vectorizer.transform([preprocessed_user_text])

            # Calculate similarity scores
            similarities = cosine_similarity(user_tfidf_vector, tfidf_vectors)

            # Display results
            st.subheader("Similarity Results")
            max_similarity = max(similarities[0])
            most_similar_idx = similarities[0].argmax()

            if max_similarity > 0.7:  # Threshold for potential plagiarism
                st.write(f"The entered text is {max_similarity*100:.2f}% similar to the document, indicating potential plagiarism.")
                st.write(f"Most similar document snippet: {documents[most_similar_idx]}")
            else:
                uniqueness_percentage = (1 - max_similarity) * 100
                st.write(f"The entered text is {uniqueness_percentage:.2f}% unique.")
        except Exception as e:
            st.error(f"Error processing the file: {e}")
    else:
        st.warning("Please upload a document and enter text for plagiarism check.")
