
players = {
    'sachin': (280, 345, 250, 410, 320),
    'rahul': (310, 225, 180, 265, 385),
    'sourav': (230, 260, 350, 150, 198),
    'sehwag':(175, 375, 450, 340, 405),
    'yuvraj':(180, 250, 235, 290, 198),
    'vvs':(145, 230, 185, 150, 280, 210)
}
print(f"players:{players}")

print("-" * 40)
print(f"Sachin :{players['sachin']}")
print(f"Sachin :{sum(players['sachin'])}")

print("-" * 40)
score  = {score for score in players}
print(f"score :{score}")

print("-" * 40)
score = {score for score in players.keys()}
print(f"score :{score}")

print("-" * 40)
score = {score for score in players.values()}
print(f"score :{score}")

print("-" * 40)
score = {k: v for (k, v) in players.items()}
print(f"scores :{score}")

print("-" * 40)
score = {k: sum(v) for (k, v) in players.items()}
print(f"score :{score}")

print("-" * 40)
score = {k : (lambda score: sum(score) / len(score))(v)
         for k, v in players.items()}
print(f"score :{score}")

print("-" * 40)
sentence  = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 40)
words = {word: len(word) for word in sentence.split()}
print(f"words :{words}")

print("-" * 40)
res = [{x : (lambda par : "Mr. " + par)("sachin {}".format(x))}
       for x in range(1, 6)]
print(f"res :{res}")

print("-" * 40)
score = [scr for scores in players.values() for scr in scores]
print(f"score :{score}")

print("-" * 40)
scores  = [scr for scores  in players.values() for scr in scores if scr > 200]
print(f"score:  {scores}")

print("-" * 40)
scores = {name: [scr for scr in scores if scr > 200]    
        for name, scores in players.items()}
print(f"scores :{scores}")
