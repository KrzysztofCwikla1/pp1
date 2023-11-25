question_1 = "Are you interested in computer science? (yes/no): "
question_2 = "Do you like playing computer games? (yes/no): "
question_3 = "Do you have an Instagram account? (yes/no): "

# Initialize logical type variables to store answers
interested_in_cs = input(question_1).lower() == 'yes'
like_playing_games = input(question_2).lower() == 'yes'
has_instagram_account = input(question_3).lower() == 'yes'

# Display survey results
print("\nSurvey Results:")
print("1. Interested in computer science: {}".format("Yes" if interested_in_cs else "No"))
print("2. Like playing computer games: {}".format("Yes" if like_playing_games else "No"))
print("3. Has an Instagram account: {}".format("Yes" if has_instagram_account else "No"))