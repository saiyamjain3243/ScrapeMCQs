import json
from bs4 import BeautifulSoup

def convert_html_to_json(html_text):
    # Parse the HTML text using BeautifulSoup
    soup = BeautifulSoup(html_text, 'html.parser')

    # Extract the question and answer
    question_element = soup.find('div', class_='mc-quiz-question--question-prompt--2_dlz')
    question = question_element.text.strip() if question_element else ""

    answer_element = soup.find('div', id='question-explanation')
    answer = answer_element.text.strip() if answer_element else ""

    # Extract the multiple-choice options
    mchoice = []
    options = soup.find_all('li', class_='mc-quiz-question--answer--eCdL3')
    for option in options:
        answer_nbr = option.find('input')['data-index']
        answer_text_element = option.find('div', class_='mc-quiz-answer--answer-body--1JtTQ')
        answer_text = answer_text_element.text.strip() if answer_text_element else ""
        is_correct = 1 if 'mc-quiz-answer--correct--is6Db' in option['class'] else 0
        mchoice.append({
            'answerNbr': int(answer_nbr),
            'answer': answer_text,
            'correct': is_correct
        })

    # Create the JSON object
    json_data = [{
        'question': question,
        'answer': answer,
        'categories': [],
        'mchoice': mchoice
    }]

    # Convert the JSON object to a JSON string
    json_string = json.dumps(json_data, indent=4)

    # Print the JSON string
    print(json_string)

    # Write the JSON string to a file
    with open('output.json', 'w') as file:
        file.write(json_string)

# Example usage
html_text = '<div class="detailed-result-panel--panel-row--2aE8z detailed-result-panel--question-container--7NyiS"><form class="mc-quiz-question--container--3GZ4h"><span>Question 5: </span><div class="ud-badge ud-heading-xs mc-quiz-question--skipped--pLGiT">Skipped</div><div data-purpose="safely-set-inner-html:rich-text-viewer:html" class="ud-text-bold mc-quiz-question--question-prompt--2_dlz rt-scaffolding" id="question-prompt">At the time of course publication, which SAP BTP service did SAP Build Work Zone rely on instead of SAP Task Center?</div><ul role="group" aria-labelledby="question-prompt" class="ud-unstyled-list"><li class="mc-quiz-question--answer--eCdL3"><label class="mc-quiz-answer--answer--11thr mc-quiz-answer--reviewing--36GXi ud-toggle-input-container ud-toggle-input-block-container ud-toggle-input-disabled" for="radio--889"><input name="answer" disabled="" data-index="0" class="ud-sr-only ud-custom-focus-visible ud-real-toggle-input" id="radio--889" type="radio"><span class="ud-fake-toggle-input ud-fake-toggle-radio ud-fake-toggle-radio-large"></span><div class="ud-toggle-input-block-outline"></div><div class="ud-heading-md"><div class="mc-quiz-answer--answer-inner--3WH_P"><div data-purpose="safely-set-inner-html:rich-text-viewer:html" class="mc-quiz-answer--answer-body--1JtTQ rt-scaffolding">SAP Workflow Management</div></div></div></label></li><li class="mc-quiz-question--answer--eCdL3"><label class="mc-quiz-answer--answer--11thr mc-quiz-answer--reviewing--36GXi ud-toggle-input-container ud-toggle-input-block-container ud-toggle-input-disabled" for="radio--890"><input name="answer" disabled="" data-index="1" class="ud-sr-only ud-custom-focus-visible ud-real-toggle-input" id="radio--890" type="radio"><span class="ud-fake-toggle-input ud-fake-toggle-radio ud-fake-toggle-radio-large"></span><div class="ud-toggle-input-block-outline"></div><div class="ud-heading-md"><div class="mc-quiz-answer--answer-inner--3WH_P"><div data-purpose="safely-set-inner-html:rich-text-viewer:html" class="mc-quiz-answer--answer-body--1JtTQ rt-scaffolding">SAP SuccessFactors</div></div></div></label></li><li class="mc-quiz-question--answer--eCdL3"><label class="mc-quiz-answer--answer--11thr mc-quiz-answer--correct--is6Db mc-quiz-answer--reviewing--36GXi ud-toggle-input-container ud-toggle-input-block-container ud-toggle-input-disabled" for="radio--891"><input name="answer" disabled="" data-index="2" class="ud-sr-only ud-custom-focus-visible ud-real-toggle-input" id="radio--891" type="radio"><span class="ud-fake-toggle-input ud-fake-toggle-radio ud-fake-toggle-radio-large"></span><div class="ud-toggle-input-block-outline"></div><div class="ud-heading-md"><div class="mc-quiz-answer--answer-inner--3WH_P"><div data-purpose="safely-set-inner-html:rich-text-viewer:html" class="mc-quiz-answer--answer-body--1JtTQ rt-scaffolding">SAP Workflow service</div><div class="ud-heading-sm mc-quiz-answer--correctness--3pFQG">(Correct)</div></div></div></label></li><li class="mc-quiz-question--answer--eCdL3"><label class="mc-quiz-answer--answer--11thr mc-quiz-answer--reviewing--36GXi ud-toggle-input-container ud-toggle-input-block-container ud-toggle-input-disabled" for="radio--892"><input name="answer" disabled="" data-index="3" class="ud-sr-only ud-custom-focus-visible ud-real-toggle-input" id="radio--892" type="radio"><span class="ud-fake-toggle-input ud-fake-toggle-radio ud-fake-toggle-radio-large"></span><div class="ud-toggle-input-block-outline"></div><div class="ud-heading-md"><div class="mc-quiz-answer--answer-inner--3WH_P"><div data-purpose="safely-set-inner-html:rich-text-viewer:html" class="mc-quiz-answer--answer-body--1JtTQ rt-scaffolding">SAP Process Automation</div></div></div></label></li><li class="mc-quiz-question--answer--eCdL3"><label class="mc-quiz-answer--answer--11thr mc-quiz-answer--reviewing--36GXi ud-toggle-input-container ud-toggle-input-block-container ud-toggle-input-disabled" for="radio--893"><input name="answer" disabled="" data-index="4" class="ud-sr-only ud-custom-focus-visible ud-real-toggle-input" id="radio--893" type="radio"><span class="ud-fake-toggle-input ud-fake-toggle-radio ud-fake-toggle-radio-large"></span><div class="ud-toggle-input-block-outline"></div><div class="ud-heading-md"><div class="mc-quiz-answer--answer-inner--3WH_P"><div data-purpose="safely-set-inner-html:rich-text-viewer:html" class="mc-quiz-answer--answer-body--1JtTQ rt-scaffolding">SAP Intelligent Robotic Process Automation (RPA)</div></div></div></label></li></ul><div class="mc-quiz-question--explanation--Q5KHQ"><h4 class="ud-heading-md">Explanation</h4><div data-purpose="safely-set-inner-html:rich-text-viewer:html" id="question-explanation" class="rt-scaffolding">SAP Build Work Zone relied on SAP Workflow service at the time of course publication, as it didn\'t have integration with SAP Task Center. SAP Workflow service provided capabilities to execute and monitor workflows in SAP Build Work Zone.</div></div></form></div>'
convert_html_to_json(html_text)
