#Make a game summary at the end of the game.
game_summary = []

rounds_lost = 0
rounds_won = 0
rounds_played = 0
score = 0

#Get results for rounds lost and tied
for item in range(1, 6):
    result = input("Choose results: ")

    if result == "win" or result == "w":
        rounds_played += 1
        rounds_won += 1
        score += 100
    
    elif result == "loss" or result == "l":
        rounds_played += 1
        rounds_lost += 1

    else:
        print("Win or loss only")

    outcome = f"Round {item}: {result}"

    game_summary.append(outcome)

#Calculate Game Stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

print()
print("*** Game History ***")
for game in game_summary:
    print(game)

print()

#Displays game stats with % values to the nearest whole number
print("*** Game Statistics ***")
print(f"Win: {rounds_won}, {percent_win:.0f}% \nLoss: {rounds_lost}, {percent_lose:.0f}%")
print(f"Score: {score} pts")
print()
print("Thank you for playing my game 🙃")