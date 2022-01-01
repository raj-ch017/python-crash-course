def book_store(copies):
    cover_price = 24.95 
    discount = 0.40 * cover_price   #calculates the discount based on the marked price
    sell_price = cover_price - discount #calculates the selling price, depending on the discount
    additional_copies = copies - 1  #the number of extra copies bought
    deli_charges = 3 + (additional_copies*0.75) #delivery charge calculation
    total = sell_price + deli_charges   #calculates the total
    print(total)

book_store(100)