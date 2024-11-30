import tkinter as tk
import random
import emoji

def generate_emoji_list():
    """Retrieve the full set of emojis from the emoji library."""
    all_emoji = emoji.EMOJI_DATA.keys()
    return list(all_emoji)

def generate_emoji_prompt():
    """Generate a random set of 9 unique emojis and update the display."""
    emoji_prompt = random.sample(EMOJI_LIST, 9)  # Ensure no duplicates
    display_emoji_in_grid(emoji_prompt)
    return emoji_prompt

def display_emoji_in_grid(emoji_prompt):
    """Display emojis in a 3x3 grid."""
    # Clear existing widgets in the grid frame
    for widget in grid_frame.winfo_children():
        widget.destroy()

    # Add emojis in a grid
    for i, emoji_char in enumerate(emoji_prompt):
        row, col = divmod(i, 3)  # Calculate row and column
        emoji_label = tk.Label(grid_frame, text=emoji_char, font=("Segoe UI Emoji", 36), padx=10, pady=10)
        emoji_label.grid(row=row, column=col)

def regenerate_prompt():
    """Regenerate the emoji prompt and display it."""
    global current_prompt
    current_prompt = generate_emoji_prompt()

def copy_to_clipboard():
    """Copy the current emoji prompt to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(' '.join(current_prompt))
    root.update()  # Ensures clipboard is updated
    copied_label.config(text="Copied to clipboard!")

# Load the full emoji list
EMOJI_LIST = generate_emoji_list()

# Initialize the application window
root = tk.Tk()
root.title("Emoji Story Prompt Generator")
root.geometry("500x500")

# Current emoji prompt
current_prompt = []

# UI Components
grid_frame = tk.Frame(root)
grid_frame.pack(pady=20)

generate_button = tk.Button(root, text="Generate an emoji story prompt", font=("Arial", 14), command=lambda: [regenerate_prompt(), generate_button.config(text="Regenerate")])
generate_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy to clipboard", font=("Arial", 14), command=copy_to_clipboard)
copy_button.pack(pady=10)

copied_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
copied_label.pack(pady=5)

# Run the application
root.mainloop()
