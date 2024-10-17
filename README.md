# Khmer Stop Word Dictionary for Keyword Extraction and Semantic Search Engine

## Overview
This project focuses on developing and utilizing **Khmer stop word dictionaries** to improve keyword extraction for a **semantic search engine**. By removing non-informative words, the effectiveness of text processing and search engine results is enhanced. This repository provides:

- Two stop word dictionaries: **300+ and 1000+ entries**.
- Code demonstrations of different filtering approaches:
  - **Direct filtering without segmentation**
  - **Filtering with segmentation using khmercut**
  - **Filtering with segmentation using Khmer-NLTK**

---

## Project Structure

### Stop Word Dictionaries
We created two stop word dictionaries:
- **300+ stop words**: For basic text filtering.
- **1000+ stop words**: For advanced filtering and NLP tasks.

Both dictionaries contain common Khmer function words, particles, and filler words that do not contribute to meaningful search results.

---

## Demonstration of Different Filtering Approaches

### 1. Direct Stop Word Filtering (Without Segmentation)
This approach directly matches and removes stop words from the input text without using word segmentation.

**Example:**
```bash
**Original Text: នេះគឺជាប្រាសាទអង្គរវត្តស្ថិតនៅក្នុងខេត្តសៀមរាបប្រទេសកម្ពុជា**

**Filtered Text: ប្រាសាទអង្គរវត្តស្ថិតខេត្តសៀមរាបប្រទេសកម្ពុជា**

---

### 2. Stop Word Filtering with Segmentation (Using khmercut)
In this approach, the text is segmented using [khmercut](https://github.com/seanghay/khmercut-rs) before filtering out the stop words.

**Example:**
```bash
**Original Text: នេះគឺជាប្រាសាទអង្គរវត្តស្ថិតនៅក្នុងខេត្តសៀមរាបប្រទេសកម្ពុជា** 
**Segmented Words: ['នេះ', 'គឺជា', 'ប្រាសាទ', 'អង្គរវត្ត', 'ស្ថិត', 'នៅក្នុង', 'ខេត្ត', 'សៀមរាប', 'ប្រទេស', 'កម្ពុជា']** 
**Filtered Words: ['ប្រាសាទ', 'អង្គរវត្ត', 'ស្ថិត', 'ខេត្ត', 'សៀមរាប', 'ប្រទេស', 'កម្ពុជា']** 
**Filtered Text: ប្រាសាទ អង្គរវត្ត ស្ថិត ខេត្ត សៀមរាប ប្រទេស កម្ពុជា**

---

### 3. Stop Word Filtering with Segmentation (Using Khmer-NLTK)
This approach demonstrates the use of [Khmer-NLTK](https://github.com/VietHoang1512/khmer-nltk) for text segmentation before filtering.

**Example:**
```bash
Original Text: នេះគឺជាប្រាសាទអង្គរវត្តស្ថិតនៅក្នុងខេត្តសៀមរាបប្រទេសកម្ពុជា
Segmented Words: ['នេះ', 'គឺជា', 'ប្រាសាទ', 'អង្គរវត្ត', 'ស្ថិត', 'នៅក្នុង', 'ខេត្ត', 'សៀមរាប', 'ប្រទេស', 'កម្ពុជា']
Filtered Words: ['ប្រាសាទ', 'អង្គរវត្ត', 'ស្ថិត', 'ខេត្ត', 'សៀមរាប', 'ប្រទេស', 'កម្ពុជា']
Filtered Text: ប្រាសាទ អង្គរវត្ត ស្ថិត ខេត្ត សៀមរាប ប្រទេស កម្ពុជា

---

## Usage Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/khmer-stopword-dictionary.git
   cd khmer-stopword-dictionary
    Install dependencies:
    pip install khmercut khmer-nltk
   Run the code:

Load stop words from the provided CSV files.
Use segmentation tools (khmercut or khmer-nltk) to segment text.
Filter out stop words using the provided functions.
