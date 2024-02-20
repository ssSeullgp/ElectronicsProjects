def count_words(text):
    """Counts the number of words in a given text, handling potential errors and edge cases.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.

    Raises:
        ValueError: If the input text is empty or only contains whitespace.
    """

    if not text.strip():
        raise ValueError("Input text cannot be empty or only whitespace.")

    # Split the text into words, ensuring proper handling of whitespace and punctuation
    words = text.split()

    # Filter out non-word characters from each word
    filtered_words = [word.strip() for word in words if word.strip()]

    return len(filtered_words)

def main():
    """Prompts the user for input, calls the word_count function, and displays the results."""

    print("\U0001F320 Welcome to the Word Counter! \U0001F320")

    while True:
        try:
            text = input("Enter a sentence or paragraph: ")

            word_count = count_words(text)
            print("The number of words is:", word_count)

            # Offer another count or exit
            choice = input("Do you want to count another text? (y/n): ")
            if choice.lower() != 'y':
                break

        except ValueError as e:
            print(e)
            print("Please enter valid text.")

if __name__ == "__main__":
    main()
