import random

print("🎮 Welcome to Rock, Paper, Scissors with AI!")
print("Type rock, paper, or scissors to play.")
print("Type quit to end the game.\n")

choices = ["rock", "paper", "scissors"]

user_score = 0
ai_score = 0

def determine_winner(user, ai):
    global user_score, ai_score

    if user == ai:
        return "It's a tie!"
    elif (
        (user == "rock" and ai == "scissors") or
        (user == "paper" and ai == "rock") or
        (user == "scissors" and ai == "paper")
    ):
        user_score += 1
        return "You win!"
    else:
        ai_score += 1
        return "AI wins!"

while True:
    user_choice = input("Your move (rock/paper/scissors): ").lower()

    if user_choice == "quit":
        print("\nGame Over!")
        print(f"Final Score → You: {user_score} | AI: {ai_score}")
        break

    if user_choice not in choices:
        print("❌ Invalid choice. Try again.\n")
        continue

    # Simple AI logic (random choice)
    ai_choice = random.choice(choices)

    print(f"🤖 AI chose: {ai_choice}")
    result = determine_winner(user_choice, ai_choice)
    print(result)
    print(f"Score → You: {user_score} | AI: {ai_score}\n")
