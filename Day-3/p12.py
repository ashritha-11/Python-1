#vowels and consonents
def vowel(n):
    count_vowels = 0
    count_consonants = 0

    for i in n.lower():  
        if i in ['a','e','i','o','u']:
            count_vowels += 1
        elif 'a' <= i <= 'z':  
            count_consonants += 1

    print("Vowels:", count_vowels)
    print("Consonants:", count_consonants)

vowel("ashritha")
