from random import choice

def get_jokes (num_jokes):
    jokes = []
    while num_jokes !=0:
        joke = [choice(nouns),choice(adverbs),choice(adjectives)]
        mass = ' '.join(joke)
        jokes.append(mass)
        num_jokes -=1
    return jokes

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(3))