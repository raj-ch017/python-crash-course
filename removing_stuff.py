def removing_stuff(sentence):
    take1 = sentence.lower()
    take2 = take1.replace("i'm","i am")
    take2 = take1.replace("haven't","have not")
    print(take2)

removing_stuff("How are you? Sorry I haven't called!")