def count_word(sentence):
    word_count = {}
    final_text = []
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    for word in sentence.split():
        text = ""
        for letter in word.lower():
            if letter not in punctuations and letter.isalpha():
                text += letter
            
        if word not in uninteresting_words:
            final_text.append(text)
            
    for word in final_text:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    return word_count

print(count_word("""Sorrow came—a gentle sorrow—but not at all in the shape of any
disagreeable consciousness.—Miss Taylor married. It was Miss Taylor’s
loss which first brought grief. It was on the wedding-day of this
beloved friend that Emma first sat in mournful thought of any
continuance. The wedding over, and the bride-people gone, her father
and herself were left to dine together, with no prospect of a third to
cheer a long evening. Her father composed himself to sleep after
dinner, as usual, and she had then only to sit and think of what she
had lost."""))