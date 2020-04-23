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
careers = ['garbage human', 'chronically unemployed alcoholic', 'invalid', 'human loofa']
print(careers)
print(careers.index('invalid'))
print('invalid' in careers)
careers.append('labotomist')
print(careers)
careers.insert(0,'boy genius')
print(careers)
for career in careers:
    print("When I grow up I wanna be a " + career)
demon_lovers = []
print(demon_lovers)
demon_lovers.append('Jafar')
demon_lovers.append('Dracula')
demon_lovers.append('The Beast')
demon_lovers.append('David Bowie from The Labrynth')
demon1 = demon_lovers[0]
print(demon1)
demon_last = demon_lovers[-1]
print(demon_last)
print(demon_lovers)
for alpha_demon in sorted(demon_lovers):
    print(alpha_demon)
for beta_demon in reversed(sorted(demon_lovers)):
    print(beta_demon)
for non_demon in demon_lovers:
    print (non_demon)
for reverse_demon in reversed(demon_lovers):
    print(reverse_demon)
demon_lovers.reverse()
print(demon_lovers)

breads = ['ciabatta', 'foccacia', 'challah']

def bread_cost(y):
    if y is 'ciabatta':
        return  4
    if y is 'foccacia':
        return  2
    if y is 'challah':
        return  7


def total(z):
    total = 0
    
    for y in z:
        total = (total + bread_cost(y))
        
    return total
    
print(total(breads))