#def right_justify(s):
 #   n1 = len(s)
  #  n2 = 70 - n1
   # print(' '*n2 + s)

#right_justify('van der beek')

def grid_pattern():
    grid1()
    grid2()
    grid1()
    grid2()
    grid1()

def grid1():
    pat1 = "+" + "-" + "-" + "-" + "-" + "+" + "-" + "-" + "-" + "-" + "+"
    print(pat1)

def grid2():
    pat2 = "|" + " " + " " + " " + " " + "|" + " " + " " + " " + " " + "|"
    print(pat2)
    print(pat2)
    print(pat2)
    print(pat2)

grid_pattern()