import random
import time

# =====================================
# 🎮 ROCK PAPER SCISSORS LIZARD SPOCK
# =====================================

print("🎯 Welcome to Rock-Paper-Scissors-Lizard-Spock Game!")
print("Rules:")
print("""
🪨 Rock crushes Scissors & Lizard
📄 Paper covers Rock & disproves Spock
✂️ Scissors cuts Paper & decapitates Lizard
🦎 Lizard eats Paper & poisons Spock
🖖 Spock smashes Scissors & vaporizes Rock
""")

choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
user_score = 0
comp_score = 0
rounds = 5

def decide_winner(user, comp):
    if user == comp:
        return "draw"
    elif (user == "rock" and comp in ["scissors", "lizard"]) or \
         (user == "paper" and comp in ["rock", "spock"]) or \
         (user == "scissors" and comp in ["paper", "lizard"]) or \
         (user == "lizard" and comp in ["spock", "paper"]) or \
         (user == "spock" and comp in ["scissors", "rock"]):
        return "user"
    else:
        return "computer"

for round_num in range(1, rounds + 1):
    print(f"\n----- ROUND {round_num} -----")
    print("Your choices:", ", ".join(choices))
    user = input("Enter your choice: ").lower()

    if user not in choices:
        print("⚠️ Invalid choice! Try again.")
        continue

    comp = random.choice(choices)
    print(f"🤖 Computer chose: {comp}")
    time.sleep(0.5)

    winner = decide_winner(user, comp)

    if winner == "draw":
        print("🤝 It's a Draw!")
    elif winner == "user":
        print("✅ You Win this round!")
        user_score += 1
    else:
        print("💻 Computer Wins this round!")
        comp_score += 1

    print(f"🏆 Score -> You: {user_score} | Computer: {comp_score}")

# -----------------------
# Final Results
# -----------------------
print("\n===========================")
print("        FINAL RESULTS       ")
print("===========================")
if user_score > comp_score:
    print("🎉 Congratulations! You WON the match!")
elif user_score < comp_score:
    print("💻 Computer Wins the match! Better luck next time.")
else:
    print("🤝 It's a tie overall!")

print(f"Final Score -> You: {user_score} | Computer: {comp_score}")
print("\nThanks for playing, Giridhar! 👋")
