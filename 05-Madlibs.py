# string concatenation(aka how to put stings together)
# suppose we want to create a sting that says "susctibe to ----------"
# youtuber = "Kylie Jing" #some string variable

# a few ways to do this
# print ("suscribe to" + youtuber)
# print ("suscribe to {}".format(youtuber))
# print (f"suscribe to {youtuber}")

Nouns1 = input("Nouns: ")
Nouns2 = input("Nouns: ")
Nouns3 = input("Nouns: ")
famous_person = input("Famous person: ")

madlibs = f"What came first, the chicken or the {Nouns1}? \
Be careful not to vacuum the {Nouns2} when you clean under your bed \
Love is what makes the {Nouns3} go Round."

print(madlibs)
