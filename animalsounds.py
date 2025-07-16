from playsound import playsound


animal_sounds = {
    "cat": "cat.mp3",
    "dog": "dog.mp3",
    "cow": "cow.mp3",
    "duck": "duck.mp3"
}


animal = input("Enter an animal (cat, dog, cow, duck): ").lower()


if animal in animal_sounds:
    print(f"Playing {animal} sound...")
    playsound(animal_sounds[animal])
else:
    print("Sorry, I don't have that animal's sound.")
