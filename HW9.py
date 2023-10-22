#Creating the file
source_filename = 'source.txt'
destination_filename = 'destination.txt'
def create_sample_source_file(filename, content):
    """Create a sample source file with given content."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

# Sample text for the source.txt
sample_content = """
To be, or not to be, that is the question,
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep.
"""

# Create source.txt with the sample content
create_sample_source_file(source_filename, sample_content)

'''
1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова, що складаються не менше ніж з семи літер.
'''

def copy_large_words(source_filename, destination_filename):
    with open(source_filename, 'r', encoding='utf-8') as source:
        with open(destination_filename, 'w', encoding='utf-8') as dest:
            for line in source:
                words = line.split()
                for word in words:
                    if len(word) >= 7:
                        dest.write(word + ' ')
            dest.write('\n')

copy_large_words(source_filename, destination_filename)


'''
2. Даний текстовий файл. Підрахувати кількість слів у ньому.
'''
def count_words(filename):
    count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            count += len(words)
    return count

number_of_words = count_words(source_filename)
print(f"There are {number_of_words} words in the file.")

'''
Додатково: 
Створіть програму, яка перевіряє текст на неприпустимі слова.
Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
За підсумками роботи програми необхідно показати статистику дій.
Неприпустиме слово: die.
'''

def replace_forbidden_words(text, forbidden_word):
    replaced_count = text.lower().count(forbidden_word.lower())
    replaced_text = text.replace(forbidden_word, '*' * len(forbidden_word))
    return replaced_text, replaced_count


forbidden_word = "die"
replaced_text, replaced_count = replace_forbidden_words(sample_content, forbidden_word)

print(replaced_text)
print(f"Statistics: {replaced_count} replacements of the word {forbidden_word}.")