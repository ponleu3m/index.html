# List of questions and answers
questions = [
    {"sentence": "The sun rises in the ___", "answer": "east"},
    {"sentence": "Fish swim in the ___", "answer": "water"},
    {"sentence": "Birds fly in the ___", "answer": "sky"},
    {"sentence": "You write with a ___", "answer": "pen"},
    {"sentence": "The moon appears at ___", "answer": "night"}
]

score = 0

print("🔤 Welcome to the Missing Word Game!\n")

# Loop through each question
for q in questions:
    print(q["sentence"].replace(q["answer"], "___"))
    guess = input("What is the missing word? ").strip().lower()

    if guess == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Oops! The correct word was '{q['answer']}'.\n")

print(f"🎉 Game over! You got {score}/{len(questions)} correct.")
