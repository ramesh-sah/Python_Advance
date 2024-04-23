def division(x:int, y:int)-> int:
    return (x//y)

a =division(10,2)


print(a)


from typing import List, Dict,Tuple
cities :List[str]=['mumbai','delhi','chennai']
# This is Tuple with three elements respectively 
# of str, int and float type)
employee: Tuple[str, int, float] = ('Ravi', 25, 35000)
# Similarly in the following Dict, the object key should be str
# and value should be of int type, failing which 
# static type checker throws error
marklist: Dict[str, int] = {'Ravi': 61, 'Anil': 72}
