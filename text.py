import random

def repeat_text_with_emoji(text, count):
    emojis = ["😊", "🎉", "🔥", "❤️", "👍", "😄", "🌟", "🌈", "💖", "🐾"]
    repeated_text = text * count
    random_emoji = random.choice(emojis)
    repeated_text_with_emoji = repeated_text + " " + random_emoji
    return repeated_text_with_emoji

input_text = input("Enter the text to repeat: ")
input_count = int(input("Enter the number of times to repeat: "))

repeated_text_with_emoji = repeat_text_with_emoji(input_text, input_count)

# Save text to a file
filename = "text.txt"
with open(filename, "w") as file:
    file.write(repeated_text_with_emoji)

print(f"Repeated text with random emoji saved to {filename}")
