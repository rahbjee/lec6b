a = ["Without a doubt","Most likely"," Better not tell you now", "Don't count on it"]

q = input("What is the question you'd like to present the 8-ball?")
if q[-1] != "?":
    print("Try again, please finish your question with a ? symbol")
    q = input("What is the question you'd like to present the 8-ball?")

ind = randrange(len(a))
print(a(ind))

