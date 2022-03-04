def text_coverter(sentence):
    input = sentence
    sent_2 = " "
    for char in sentence:
        if char.isalpha() and char != " ":
            sent_2 = sent_2 + char
        elif char == " ":
            sent_2 = sent_2 + char
    print(sent_2)

text_coverter("Today is Monday! Do you understand?")



def making_dictionary(part1):
    input_3 = part1
    input = input_3.split()
    count = 0
    the_dictionary = {}
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    for word in input:
        if word not in uninteresting_words:
            if word not in the_dictionary:
                count = 1
                the_dictionary[word]= count
            else:
                c = the_dictionary[word]
                the_dictionary[word] = c + 1 
    return the_dictionary

print(making_dictionary("The black cat met a white dog and brown dog"))