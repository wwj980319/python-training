import logging
from collections import Counter
logging.basicConfig(level=logging.INFO)

def read_file(file_path: str):
    content = ''

    try:
        f = open(file_path, 'r')
        content = f.read()
        logging.info(f'\nThe file content is: \n{content}')
        f.close()
    except FileNotFoundError as e:
        logging.exception(e)

    return content

def words_counter(content: str):
    words = content.split('\n')
    counter = Counter(words).most_common()
    logging.info(f'\nThe frequence of every word: \n{counter}')
    return counter

def top_ten_words(counter: list):
    sorted_words = sorted(counter, key=lambda x: x[1], reverse=True)
    logging.info(f'\nThe words in top ten frequence: \n{sorted_words[:10]}')
    return sorted_words[:10]

# def main():
#     file_content = read_file('words1.txt')
#     words_counter = words_counter(file_content)
#     top_ten_words = top_ten_words(words_counter)


if __name__ == '__main__':
    file_content = read_file('words1.txt')
    words_counter = words_counter(file_content)
    top_ten_words = top_ten_words(words_counter)

