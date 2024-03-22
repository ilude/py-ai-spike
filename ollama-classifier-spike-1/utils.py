import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def read_prompt(prompt_file):
  return open(os.path.join(current_dir, prompt_file), 'r').read()


def read_messages(messages_file):
  messages = []

  # Open the file
  with open(os.path.join(current_dir, messages_file), 'r') as file:
      # Read each line in the file
      current_message = ""
      for line in file:
          # Strip whitespace from the line
          line = line.strip()
          # Check if the line is not empty
          if line:
              # Check if the line starts with "Scam" or "Valid"
              if line.startswith("Scam:") or line.startswith("Valid:"):
                  # If there's a current message, add it to the list of messages
                  if current_message:
                      messages.append({'type': message_type, 'content': current_message})
                  # Get the message type
                  message_type = line.split(":")[0].strip()
                  # Start a new current message
                  current_message = line[len(message_type) + 1:].strip()
              else:
                  # Append the line to the current message
                  current_message += " " + line

      # Add the last message to the list of messages
      if current_message:
          messages.append({'type': message_type, 'content': current_message})

  return messages