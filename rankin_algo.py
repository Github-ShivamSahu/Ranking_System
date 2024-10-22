import pandas as pd

# List of players
players = ["shivam", "arpit", "satyam", "harsh"]

# Initialize votes list and rank dictionary
votes = []
rank = {player: 0 for player in players}  # Initializes rank with 0 votes for each player

# Total number of possible combinations
for i in range(len(players)):
    for j in range(i + 1, len(players)):
        # Input --> votes
        usr = input(f"Who is better? {players[i]} or {players[j]}: ").lower()
        
        # Append vote details to the votes list
        votes.append({'player1': players[i],
                      'player2': players[j],
                      'win': usr})
        
        # Update the number of wins received
        if usr in rank:
            rank[usr] += 1

# Convert the votes list into a DataFrame
df_votes = pd.DataFrame(votes)

# Function to check head-to-head results
def head_to_head(player1, player2):
    """Returns:
    1 if player1 won head-to-head,
    -1 if player2 won head-to-head,
    0 if they never competed."""
    
    # Find the match between player1 and player2
    match = df_votes[((df_votes['player1'] == player1) & (df_votes['player2'] == player2)) |
                     ((df_votes['player1'] == player2) & (df_votes['player2'] == player1))]
    
    if match.empty:
        return 0  # No match, no way to break the tie
    elif match.iloc[0]['win'] == player1:
        return 1  # player1 won head-to-head
    else:
        return -1  # player2 won head-to-head

# Sort players based on total wins, and break ties using head-to-head results
sorted_players = sorted(players, key=lambda x: (rank[x], [head_to_head(x, y) for y in players]), reverse=True)

# Create a DataFrame to display the sorted rank
df_rank = pd.DataFrame(sorted_players, columns=['player'])
df_rank['wins'] = df_rank['player'].map(rank)

# Display the ranked players
print("\nRanked Players:")
print(df_rank)
