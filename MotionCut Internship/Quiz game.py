def ask_question(question, options, answer):
  """Asks a question with multiple-choice options and checks the answer.

  Args:
    question: The question string.
    options: A list of strings representing the answer choices.
    answer: The index of the correct answer in the options list.

  Returns:
    True if the user answers correctly, False otherwise.
  """
  print(question)
  for i, option in enumerate(options):
    print(f"{i+1}. {option}")
  user_answer = input("Enter your answer (1-4): ")

  try:
    user_answer = int(user_answer) - 1
    if user_answer == answer:
      print("\u2B50 Correct! \u2B50")
      return True
    else:
      print("Incorrect! The correct answer is:", options[answer])
      return False
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 4.")
    return ask_question(question, options, answer)

def main():
  """Runs the quiz and displays the final score."""
  questions = [
    ("What is the capital of France?", ["Paris", "London", "Madrid", "Berlin"], 0),
    ("In which country did the Industrial Revolution begin?", ["Germany", "Great Britain", "Thailand", "India"], 1),
    ("What is the scientific name for a human?", ["Homo sapiens", "Homo erectus", "Australopithecus afarensis", "Neanderthal"], 0),
    ("Which country is known as the Land of the Rising Sun?", ["South Korea", "Taiwan", "Japan", "China" ], 2),
    ("Who is the current President of India?", ["Droupadi Murmu", "Manmohan Singh", "Narendra Modi", "Salman Khan"],0),
    ("Where is India’s Silicon Valley located?", ["Bombay", "Delhi", "Chennai", "Bangalore"], 3)
    
  ]


  score = 0
  for question in questions:
    if ask_question(*question):
      score += 1

  print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
  main()
