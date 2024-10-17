import csv
from khmernltk import word_tokenize  # Import word segmentation from khmer-nltk

# Function to load stop words from a CSV file
def load_stop_words(file_path):
    stop_words = set()
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            stop_words.add(row[0].strip())
    return stop_words

# Function to segment input text and remove stop words
def remove_stop_words(text, stop_words):
    # Step 1: Segment the input text using khmer-nltk
    segmented_words = word_tokenize(text)
    print("Segmented Words:", segmented_words)  # Display segmented words for debugging

    # Step 2: Filter out stop words
    filtered_words = [word for word in segmented_words if word not in stop_words]
    print("Filtered Words:", filtered_words)  # Display words after filtering

    # Step 3: Join the filtered words back into a string
    return " ".join(filtered_words)

# Example usage
if __name__ == "__main__":
    # Path to your CSV file containing Khmer stop words
    stop_words_file = "/content/Khmer-Stop-Word-1000.csv"
    input_text = "នេះគឺជាប្រាសាទអង្គរវត្តស្ថិតនៅក្នុងខេត្តសៀមរាបប្រទេសកម្ពុជា"
    print("Original Text:", input_text)
    # Load the stop words from the CSV file
    khmer_stop_words = load_stop_words(stop_words_file)

    # Example input text (with no spaces)
    

    # Remove stop words from the input text
    filtered_text = remove_stop_words(input_text, khmer_stop_words)

    # Output the original and filtered text
    
    print("Filtered Text:", filtered_text)
