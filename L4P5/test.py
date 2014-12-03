vowels = ('A', 'E', 'I', 'O', 'U')
def countVowels(text):
    count = 0
    for c in text:
        if c in vowels:
            count += 1
    return count

print countVowels('AABBCCEE')