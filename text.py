import random

def repeat_text_with_emoji(text, count):
    emojis = ["😊", "😍", "😒", "❤️", "🥹", "🥰", "😘", "💗", "💖", "🖤"]
    repeated_text = text * count
    random_emoji = random.choice(emojis)
    repeated_text_with_emoji = repeated_text + random_emoji
    return repeated_text_with_emoji

input_text = input("Enter the text to repeat: ")
input_count = int(input("Enter the number of times to repeat: "))

# Generate repeated text with emojis
repeated_texts_with_emojis = []
for _ in range(input_count):
    repeated_text_with_emoji = repeat_text_with_emoji(input_text, 1)
    repeated_texts_with_emojis.append(repeated_text_with_emoji)

# Save texts to a file
filename = "text.txt"
with open(filename, "w") as file:
    file.write('\n'.join(repeated_texts_with_emojis))

print(f"Repeated texts with random emojis saved to {filename}")
