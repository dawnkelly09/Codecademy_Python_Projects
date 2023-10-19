letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# zip lists to create a dictionary mapping each letter to a value
letter_to_points = {
  key:value
  for key, value
  in zip(letters, points)
}

# add a key:value for the 0 point blank tile
letter_to_points[" "] = 0

# function to score each word played
def score_word(word):
    # initialize point total to 0
  point_total = 0
  for letter in word:
      # add the value of each letter to the point total
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")
# print(brownie_points)

# create new dictionary
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"], 
  "wordNerd": ["EARTH", "EYES", "MACHINE"], 
  "LexiCon": ["ERASER", "BELLY", "HUSKY"], 
  "ProfReader": ["ZAP", "COMA", "PERIOD"]
}
# print(player_to_words)


#start with blank dictionary
player_to_points = {}
# iterate through each player and their words
for player, words in player_to_words.items():
    # initialize player points to 0
  player_points = 0
  for word in words:
      # add the result of score_word func for each word to player_points
    player_points += score_word(word)
    # using current player as key, add player_points to player_to_points dictionary
  player_to_points[player] = player_points
# print(player_to_points)