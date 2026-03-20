import string


def word_frequency(text):
    cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = cleaned_text.split()
    word_freq = {}
    for w in words:
        word_freq[w] = word_freq.get(w, 0) + 1
    return word_freq


long_text = """
    In a Java Spring Boot application, the controller handles the request, 
    the service processes the request, 
    and the repository fetches the data for the request. 
    The request flows through the Spring Boot layers where each layer processes the request and returns a response. 
    Proper handling of the request and response in Spring Boot ensures that the application remains scalable, maintainable, and efficient.
"""
freq = word_frequency(long_text)
most_common_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)
for word, freq in most_common_words[:5]:
    print({word: freq})
