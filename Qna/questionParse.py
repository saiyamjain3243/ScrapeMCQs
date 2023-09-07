import json
from bs4 import BeautifulSoup

def convert_html_to_json(html_text):
    # Parse the HTML text using BeautifulSoup
    soup = BeautifulSoup(html_text, 'html.parser')

    # Find all div elements with the class detailed-result-panel--question-container--7NyiS
    question_divs = soup.find_all('div', class_='detailed-result-panel--question-container--7NyiS')

    # Create an empty list to store JSON data for each question
    json_data = []

    # Loop through each question div
    for question_div in question_divs:
        question_element = question_div.find('div', class_='mc-quiz-question--question-prompt--2_dlz')
        question = question_element.decode_contents() if question_element else ""

        answer_element = question_div.find('div', id='question-explanation')
        answer = answer_element.decode_contents() if answer_element else ""

        # Extract the multiple-choice options
        mchoice = []
        options = question_div.find_all('li', class_='mc-quiz-question--answer--eCdL3')
        for option in options:
            answer_nbr = option.find('input')['data-index']
            answer_text_element = option.find('div', class_='mc-quiz-answer--answer-body--1JtTQ')
            answer_text = answer_text_element.decode_contents() if answer_text_element else ""
            is_correct = 1 if 'mc-quiz-answer--correct--is6Db' in option.find('label')['class'] else 0
            mchoice.append({
                'answerNbr': int(answer_nbr),
                'answer': answer_text,
                'correct': is_correct
            })

        # Append data for this question to the JSON list
        json_data.append({
            'question': question,
            'answer': answer,
            'categories': [],
            'mchoice': mchoice
        })

    return json_data

# Read HTML content from the file
input_file_path = r"C:\Users\SaiyamJain\Qna\input.html"  # Example input file path
with open(input_file_path, 'r', encoding="utf-8") as html_file:
    html_code = html_file.read()

# Call the function to convert HTML to JSON
json_data = convert_html_to_json(html_code)

# Convert the JSON data list to a JSON string
json_string = json.dumps(json_data, indent=4)

# Print the JSON string
print(json_string)

# Specify the desired output file path and name
output_file_path = r"C:\Users\SaiyamJain\Qna\output.json"  # Example output file path

# Write the JSON string to the specified output file
with open(output_file_path, 'w') as file:
    file.write(json_string)

print(f"JSON data has been written to {output_file_path}")
