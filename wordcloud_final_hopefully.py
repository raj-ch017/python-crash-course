def calculate_frequencies(sentence):
    final_text = []
    the_dictionary = {}
    argument1 = sentence.split()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    for word in argument1:
        text = ""
        x = word.lower()
        for letter in x:
            if letter not in punctuations and letter.isalpha():
                text = text + letter
            else:
                text = text + " "
        final_text.append(text)
    for word in final_text:
        if word not in uninteresting_words:
            if word not in the_dictionary:
                count = 1
                the_dictionary[word] = count
            else:
                c = the_dictionary[word]
                the_dictionary[word] = c +1
    print(the_dictionary)     
    print(final_text)

sentence = "That's the interval of time from one ten million trillion trillion trillionths of a second after the beginning, and before the universe grew to one hundred billion trillion trillionths of a meter"
calculate_frequencies(sentence)