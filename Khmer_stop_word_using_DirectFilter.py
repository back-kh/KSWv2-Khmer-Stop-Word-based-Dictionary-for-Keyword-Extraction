import csv

# Function to load stop words from a CSV file
def load_stop_words(file_path):
    stop_words = set()
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # Assuming each stop word is on a new line
            stop_words.add(row[0].strip())
    return stop_words

# Function to remove stop words from the input text (without word segmentation)
def remove_stop_words(text, stop_words):
    filtered_text = text  # Start with the original text
    for stop_word in stop_words:
        filtered_text = filtered_text.replace(stop_word, "")  # Remove stop words
    return filtered_text.strip()

# Example usage
if __name__ == "__main__":
    # Path to your CSV file containing Khmer stop words
    stop_words_file = "/content/Khmer-Stop-Word-1000.csv"

    # Load the stop words from the CSV file
    khmer_stop_words = load_stop_words(stop_words_file)

    # Example input text
    input_text = "នេះគឺជាប្រាសាទអង្គរវត្តស្ថិតនៅក្នុងខេត្តសៀមរាបប្រទេសកម្ពុជា"

    # Remove stop words from the input text
    filtered_text = remove_stop_words(input_text, khmer_stop_words)

    # Output the result
    print("Original Text:", input_text)
    print("Filtered Text:", filtered_text)
