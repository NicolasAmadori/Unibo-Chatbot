import os
from collections import defaultdict, Counter
import re

def get_all_files(directory):
    """
    Recursively get all files from the directory and its subdirectories.
    """
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

def read_file(file_path):
    """
    Read the content of a file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def find_common_word_sequences(files, sequence_length=3):
    """
    Find common sequences of words in the given files.
    """
    sequence_counter = defaultdict(int)
    
    for file_path in files:
        content = read_file(file_path)
        # Tokenize the content into words using a simple regex
        words = re.findall(r'\b\w+\b', content.lower())
        
        # Create sequences of words
        for i in range(len(words) - sequence_length + 1):
            sequence = tuple(words[i:i + sequence_length])
            sequence_counter[sequence] += 1
    
    # Find sequences that appear in more than one file
    common_sequences = Counter(sequence_counter)
    common_sequences = {seq: count for seq, count in common_sequences.items() if count > 1}
    
    return common_sequences

def main(directory, sequence_length=3):
    files = get_all_files(directory)
    common_sequences = find_common_word_sequences(files, sequence_length)
    
    # Print common sequences and their counts
    for sequence, count in common_sequences.items():
        if count > 8:
            print(f"Sequence: {' '.join(sequence)}, Count: {count}")

if __name__ == "__main__":
    directory = "unibo/pagine"
    sequence_length = 300
    main(directory, sequence_length)
