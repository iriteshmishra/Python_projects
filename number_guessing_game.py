import random

number_to_guess = random.randint(1, 100)
while True:
  try:
    guess = int(input('Guess the number between 1 and 100: '))

    if guess < number_to_guess:
      print('Too Low!')
    elif guess > number_to_guess:
      print('To High!')
    else:
      print('Congratulations! You guessed the number.')
      break
  except ValueError:
      print('Please enter a valid number')


# generate a random number
# Loop
# Ask the user to make a guess
# If not a valid number
#   print an error
# if number< guess
#   print to low
# if number > guess
#   print to high
# else
#   print well done

