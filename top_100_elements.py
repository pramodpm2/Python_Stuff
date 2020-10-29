%%time
from random import randint
_from = -1000
_to = 100000
top = []
for _ in range(1000):
  
    input_stream_data = randint(_from,_to)
    top.append(input_stream_data)
    if(len(top)==101):
      m=min(top)
      top.remove(m)
    
top.sort(reverse=True)
print(top)
print(len(top))

