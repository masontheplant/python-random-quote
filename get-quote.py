import random
last = 16
rnd= random.randint(0, last)
rnd2= random.randint(0, last)
def primary():
 print("Keep it logically awesome.")

 f = open("quotes.txt")
 quotes = f.readlines()
 f.close()

 print(quotes[rnd], end = '')
 print(quotes[rnd2])

if __name__== "__main__":
  primary()
