class County:
  def __init__(self,init_name,init_population,init_turnout):
    self.name = init_name
    self.population = init_population
    self.turnout = init_turnout
    
def highest_turnout(data):
    d = data.copy()
    highper = []
    for county in data:
      x = county.turnout
      y = county.population
      z = x/y
      highper.append(z)
    out = (max(highper))
    i = highper.index(out)
    n = d[i]
    a = n.name
    b = n.population
    c = round(out,1)
    tup = (a,b,c)
    return tup

# your program will be evaluated using these objects 
# it is okay to change/remove these lines but your program
# will be evaluated using these as inputs
allegheny = County("allegheny", 1000490, 645469)
philadelphia = County("philadelphia", 1134081, 539069)
montgomery = County("montgomery", 568952, 399591)
lancaster = County("lancaster", 345367, 230278)
delaware = County("delaware", 414031, 284538)
chester = County("chester", 319919, 230823)
bucks = County("bucks", 444149, 319816)
data = [allegheny, philadelphia, montgomery, lancaster, delaware, chester, bucks]  

result = highest_turnout(data) # do not change this line!
print(result) # prints the output of the function
# do not remove this line!

