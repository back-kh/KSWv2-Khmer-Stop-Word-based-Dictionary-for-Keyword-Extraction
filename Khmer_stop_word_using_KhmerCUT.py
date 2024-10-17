import csv
from khmercut import tokenize  # Import the tokenizer from khmercut

# Function to load stop words from a CSV file
def load_stop_words(file_path):
    stop_words = set()
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            stop_words.add(row[0].strip())
    return stop_words

# Function to segment text and remove stop words
def remove_stop_words(text, stop_words):
    # Segment the input text using khmercut
    words = tokenize(text)
    print("Segmented Words:", words)  # Debug: Display segmented words

    # Filter out the stop words
    filtered_words = [word for word in words if word not in stop_words]
    print("Filtered Words:", filtered_words)  # Debug: Display filtered words

    # Join the filtered words back into a string
    return " ".join(filtered_words)

# Example usage
if __name__ == "__main__":
    # Path to your CSV file containing Khmer stop words
    stop_words_file = "/content/Khmer-Stop-Word-1000.csv"
    input_text = "នេះគឺជាប្រាសាទអង្គរវត្តស្ថិតនៅក្នុងខេត្តសៀមរាបប្រទេសកម្ពុជា"
    print("Original Text:", input_text)
    # Load the stop words from the CSV file
    khmer_stop_words = load_stop_words(stop_words_file)

    # Example input text

    # Remove stop words from the input text
    filtered_text = remove_stop_words(input_text, khmer_stop_words)

    # Output the original and filtered text
    
    print("Filtered Text:", filtered_text)
