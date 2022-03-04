def text_conversion(sentence):
    input = sentence
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    sent_2 = " "
    for char in input:
        if char.isalpha() and char != " ":
            sent_2 = sent_2 + char.lower()
        elif char == " ":
            sent_2 = sent_2 + " "
        elif char == "-":
            sent_2 = sent_2 + " "
    input = sent_2.split()
    count = 0
    the_dictionary = {}
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    uninteresting_words1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for word in input:
        if word not in uninteresting_words and word not in uninteresting_words1:
            if word not in the_dictionary:
                count = 1
                the_dictionary[word]= count
            else:
                c = the_dictionary[word]
                the_dictionary[word] = c + 1 
    print(sent_2)
    print(the_dictionary)

text_conversion("""In the beginning, nearly fourteen billion years ago, all the space and all the matter and all the energy of the known universe was contained in a volume less than one-trillionth the size of the period that ends this sentence. Conditions were so hot, the basic forces of nature that were collectively describe the universe were unified. Though still unknown how it came into existence, this sub-pinpointIn the beginning, nearly fourteen billion years ago, all the space and all the matter and all the energy of the known universe was contained in a volume less than one-trillionth the size of the period that ends this sentence. Conditions were so hot, the basic forces of nature that were collectively describe the universe were unified. Though still unknown how it came into existence, this sub-pinpoint-size cosmos could only expand. Rapidly. In what today we call the big bang. Einstein's general theory of relativity, put forth in 1916, gives us our modern understanding of gravity, in which the presence of matter and energy curves the fabric of space and time surrounding it. In the 1920s, quantum mechanics would be discovered, providing our modern account of all that is small: molecules, atoms, and subatomic particles. But these two understandings of nature are formally incompatible with one another, which set physicists off on a race to blend the theory of the small with the theory of the large into a single coherent theory of quantum gravity. Although we haven't yet reached the finish line, we know exactly where the high hurdles are. One of them is during the "Plank era" of the early universe. That's the interval of time from one-ten-million-trillion-trillion-trillionths of a second after the beginning, and before the universe grew to one hundred billion trillion-trillionths of a meter across.""")
