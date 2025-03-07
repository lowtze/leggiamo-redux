import re

def process_translations(text):
    # Regex to find all translations enclosed in (=...)
    translation_pattern = re.compile(r'(\w+)\s*\(=(.*?)\)')

    # Find all translations and their positions
    translations = []
    def replace_with_footnote(match):
        word = match.group(1)  # The word before the translation
        translation = match.group(2)  # The translation
        footnote_id = len(translations) + 1
        translations.append((footnote_id, translation))
        return f'{word}[^{footnote_id}]'  # Place footnote directly after the word

    # Replace translations with footnotes in the main text
    processed_text = translation_pattern.sub(replace_with_footnote, text)

    # Add translations as footnotes at the end of the document
    if translations:
        processed_text += '\n\n---\n\n### Translations\n\n'
        for footnote_id, translation in translations:
            processed_text += f'[^{footnote_id}]: {translation}\n'

    return processed_text

# Read the input document
input_file = 'ch5.txt'  # Replace with your input file path
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Process the text
output_text = process_translations(text)

# Write the output to a new file
output_file = 'ch5.md'  # Replace with your desired output file path
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(output_text)

print(f"Processed text saved to {output_file}")