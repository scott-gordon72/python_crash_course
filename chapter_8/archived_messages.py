text_messages = [
        'hello there', 'hey willie', 'wanna do me?', 'well, hello there..']
sent_messages = []

def send_messages(messages):
    while messages:
        for message in messages:
            print(message)
            current_message = messages.pop()
            sent_messages.append(current_message)

send_messages(text_messages[:])
print(f"text_messages list: {text_messages}")
print(f"sent_messages list: {sent_messages}")
