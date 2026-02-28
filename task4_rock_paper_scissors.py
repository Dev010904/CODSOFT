# ============================================================
# TASK 4 - ROCK-PAPER-SCISSORS GAME
# CodSoft Python Programming Internship
# ============================================================

import random

CHOICES = ["rock", "paper", "scissors"]
EMOJI   = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

# What beats what
BEATS = {
    "rock":     "scissors",
    "scissors": "paper",
    "paper":    "rock",
}

def get_winner(user, computer):
    """Return 'user', 'computer', or 'tie'."""
    if user == computer:
        return "tie"
    elif BEATS[user] == computer:
        return "user"
    else:
        return "computer"

def display_scores(user_score, comp_score, ties):
    print(f"\n  📊 Score — You: {user_score}  |  Computer: {comp_score}  |  Ties: {ties}")

def main():
    print("\n" + "=" * 50)
    print("    🎮  ROCK - PAPER - SCISSORS GAME")
    print("=" * 50)
    print("  Rules: Rock beats Scissors | Scissors beats Paper | Paper beats Rock")

    user_score = 0
    comp_score = 0
    ties       = 0
    round_num  = 0

    while True:
        print("\n" + "-" * 50)
        print("  Your choices:  1. Rock 🪨   2. Paper 📄   3. Scissors ✂️   4. Quit")
        choice_input = input("  Enter your choice (1/2/3/4): ").strip()

        if choice_input == "4":
            break

        if choice_input not in ("1", "2", "3"):
            print("  ⚠️  Invalid choice! Please enter 1, 2, 3, or 4.")
            continue

        user_choice = CHOICES[int(choice_input) - 1]
        comp_choice = random.choice(CHOICES)
        round_num  += 1

        print(f"\n  Round {round_num}")
        print(f"  You chose    : {EMOJI[user_choice]}  {user_choice.capitalize()}")
        print(f"  Computer chose: {EMOJI[comp_choice]}  {comp_choice.capitalize()}")

        winner = get_winner(user_choice, comp_choice)

        if winner == "tie":
            print("  🤝 It's a TIE!")
            ties += 1
        elif winner == "user":
            print(f"  🎉 You WIN! {user_choice.capitalize()} beats {comp_choice.capitalize()}!")
            user_score += 1
        else:
            print(f"  💻 Computer WINS! {comp_choice.capitalize()} beats {user_choice.capitalize()}!")
            comp_score += 1

        display_scores(user_score, comp_score, ties)

    # Final summary
    print("\n" + "=" * 50)
    print("  🏁  GAME OVER — Final Results")
    print("=" * 50)
    print(f"  Rounds Played : {round_num}")
    display_scores(user_score, comp_score, ties)

    if user_score > comp_score:
        print("\n  🏆 Overall Winner: YOU! Congratulations!\n")
    elif comp_score > user_score:
        print("\n  🤖 Overall Winner: Computer! Better luck next time!\n")
    else:
        print("\n  🤝 Overall Result: It's a TIE! Well played!\n")

if __name__ == "__main__":
    main()
