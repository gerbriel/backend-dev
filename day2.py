def first_vowel(x):
    for index, char in enumerate(x):
        if char in 'aeiou':
            return index    
def convert(x):
    index=first_vowel(x)
    return x[index:]+x[:index]+'ay'
    print(convert('dog'))
# englishWords = ['dog','zebra','tiger']
# vowels = 'aeiou'
# wordAmount = 3






# bitwiseClasses = ['intro to backend','react','mobile friendly']
# classAmount = 3
# classAvailibility = True
# classBackendGrade = 97.4
# classReactGrade = 90.4
# classMobileGrade = 96.4
# spam = 'spam'
# print (englishWords)

# classAverage = (classBackendGrade + classReactGrade +
# classMobileGrade) / classAmount
# print(classAverage)


# loops, conditionals if/else
# loop through a string and stop as soon as you get to a vowel
# slice and put at the end of the word
# add 'ay' to end
# slice
# print (bitwiseClasses[:1])

# for loops
# for spamChar in spam:
#     print(spamChar)
# while loops
# classTracker=0
# while(classTracker < 3):
#     print(bitwiseClasses[classTracker])
#     classTracker+=1

# if classAmount >=5:
#     print("awesome")
# else:
#     print("not awesome")