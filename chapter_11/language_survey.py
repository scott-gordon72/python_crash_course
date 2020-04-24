"""
Defines a question ("What language did you first learn to speak?") and
creates and Anonymous survey object with that question
"""

from survey import AnonymousSurvey

# Define a question, and make a survey.
QUESTION = "What language did you first learn to speak?"
MY_SURVEY = AnonymousSurvey(QUESTION)

# Show the question, and store responses to the question.
MY_SURVEY.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    RESPONSE = input("Language: ")
    if RESPONSE == 'q':
        break
    MY_SURVEY.store_response(RESPONSE)
    # Show the survey results.
    print("\nThank you to everyone who participated in the survey!")
    MY_SURVEY.show_results()
