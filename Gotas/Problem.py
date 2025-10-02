from collections import Counter



def flames_game(name1, name2):





 s1 = "".join(ch for ch in name1.lower() if ch.isalpha())

 s2 = "".join(ch for ch in name2.lower() if ch.isalpha())



 c1 = Counter(s1)



 c2 = Counter(s2)



 for ch in list(c1.keys()):



  if ch in c2:



   common = min(c1[ch], c2[ch])



   c1[ch] -= common



   c2[ch] -= common



   if c1[ch] == 0:



    del c1[ch]



   if c2.get(ch, 0) == 0 and ch in c2:



    del c2[ch]



 total = sum(c1.values()) + sum(c2.values())







 if total == 0:



  return "Not compatible! Single forever </3"



 flames = ["Friendship", "Enemy", "Affection", "Love", "Marriage", "Sibling"]





 idx = 0



 while len(flames) > 1:



  idx = (idx + total - 2) % len(flames)



  flames.pop(idx)



  if idx == len(flames):



   idx = 0





 return flames[0]







if __name__ == "__main__":



 n1 = input("your name: ")



 n2 = input("Crush name 2: ")







 print("Result:", flames_game(n1, n2))



