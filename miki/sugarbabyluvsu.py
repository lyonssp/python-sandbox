y = "I Love You!"
print(y)
x = "Dems Da Rulez!"
print(x)
eats = ['peanut','butter','cups']
for eat in eats: 
    print("The ingredients to my favorite food are " + eat + "!")
eating = eats[0]
eater = eats[1]
eatest = eats[2]
print(eating + eater + eatest)
print(eats[0] + eats[1] + eats[2]) 
codes = ['python', 'c', 'java']
print(codes[0])
print(codes[1])
print(codes[2])
print(codes)
codes = [5, 4, 3]
print(codes)
for language in codes:
    print(language*2)
hogs = ['javelina', 'feral', 'teacup']
littlehog = hogs[2]
print(littlehog)
for hog in hogs:
    print("I wish I was a " + hog + " hog")
    print("I wish I had a " + hog + " hog")
hogs[2] = 'babe'
print(hogs)
hogs.append('teacup')
print(hogs)
for hog in hogs:
    print("Take me down to paradise city where the hogs are " + hog + " and there's 40-50")
hogs.insert(2, 'farm')
print(hogs)
hognames = []
print(hognames)
hognames.insert(0,'cronk')
hognames.insert(1, 'spud')
hognames.append('groot')
print(hognames)
hognames.sort()
print(hognames)