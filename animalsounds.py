def animal_sound(animal):
    if animal == "cat":
        return "Meow"
    elif animal == "dog":
        return "Woof"
    elif animal == "cow":
        return "Moo"
    elif animal == "duck":
        return "Quack"
    else:
        return "I don't know that animal."

animal = input("Enter an animal (cat, dog, cow, duck): ").lower()
print(animal_sound(animal))
