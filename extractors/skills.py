import nltk
 
nltk.download('stopwords')
 
SKILLS_DB = [
    'machine learning',
    'data science',
    'python',
    'word',
    'excel',
    'English',
    'html',
    'css',
    'java',
    'c',
    'c++',
    'javascript',
    'php',
    'sql',
    'nosql',
    'django',
    'flask',
    'nodejs',
    'reactjs',
    'angular',
    'vuejs',
    'ruby',
    'rails',
    'swift',
    'objective c',
    'android',
    'ios',
    'git',
    'laravel',
    'aws',
    'css',
    'sass',
    'wordpress',
    'drupal',
    'jquery',
    'bootstrap',
    'mysql',
    'mongodb',
]
 
 
def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)
 
    # remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]
 
    # remove the punctuation
    filtered_tokens = [w for w in word_tokens if w.isalpha()]
 
    # generate bigrams and trigrams (such as artificial intelligence)
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
 
    # we create a set to keep the results in.
    found_skills = set()
 
    # we search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token)
 
    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)
 
    return found_skills