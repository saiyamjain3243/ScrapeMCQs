# Web Scraping and MCQ Upload Tool

This Python script allows you to scrape multiple-choice questions (MCQs) from a webpage and then upload them to another website, saving you valuable time in the process.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Web scraping is a common task for gathering data from websites, and it can be particularly useful when you need to collect a large number of MCQs from a specific webpage. This tool automates the process of scraping MCQs and uploading them to another site, streamlining the workflow.

## Prerequisites

Before you can use this tool, make sure you have the following prerequisites installed:

- Python 3.x
- pip (Python package manager)

You can install Python from the official website: [Python Downloads](https://www.python.org/downloads/)

## Installation

1. Clone this GitHub repository to your local machine:

   ```bash
   git clone https://github.com/saiyamjain3243/ScrapeMCQs/
   ```

2. Navigate to the project directory:

   ```bash
   cd https://github.com/saiyamjain3243/ScrapeMCQs/
   ```

3. Install the required Python packages using pip:

   ```bash
   pip3 install -r beautifulsoup4
   ```

## Usage

To use this tool, follow these steps:

1. Run the script:

   ```bash
   python Qna.py
   ```

2. The script will prompt you for the URL of the webpage containing the MCQs.

3. After providing the URL, the script will scrape the MCQs and save them to a file.

4. Next, the script will prompt you to provide the URL of the website where you want to upload the MCQs.

5. The script will then upload the MCQs to the specified website.

6. Check the output for any errors or success messages.

## Configuration

You can configure the tool by modifying the `Output.json` file. This file allows you to customize various settings such as the file format for saving MCQs, login credentials for the target website, and more.

```json
{
   "question": "your question here",
        "answer": "your answer",
        "categories": [],
        "mchoice": [
            {
                "answerNbr": 0,
                "answer": "a",
                "correct": 0
            },
            {
                "answerNbr": 1,
                "answer": "b",
                "correct": 0
            }
      ]
}
```

Make sure to update the `output_format` and `target_website` values as needed.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.

2. Clone your fork to your local machine.

3. Create a new branch for your feature or bug fix.

4. Make your changes and test them thoroughly.

5. Commit your changes with clear commit messages.

6. Push your changes to your GitHub fork.

7. Create a pull request to the original repository.

## License

This project is licensed under an Apache 2.0 license.

---

Feel free to customize this README template to include any additional information or instructions specific to your project. Make sure to keep it well-organized and informative to help others understand and use your code effectively.
