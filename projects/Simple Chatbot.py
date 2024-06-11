def chatbot():
  responses = {
      'hello': 'Hi there!',
      'how are you': 'I am a bot, I am always fine.',
      'bye': 'Goodbye!'
  }

  print("Chatbot: Type 'bye' to exit.")
  while True:
      user_input = input('You: ').lower()
      if user_input in responses:
          print(f"Chatbot: {responses[user_input]}")
      else:
          print("Chatbot: I don't understand that.")
      if user_input == 'bye':
          break

# Example usage
chatbot()
