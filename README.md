# Product Comments Categorizer

This Python script categorizes user comments on a product into predefined categories using OpenAI's GPT-3. It reads comments and categories from JSON files, categorizes each comment using GPT-3, and outputs the results to another JSON file.

## Installation

1. Clone this repository to your local machine.
2. Ensure Python 3.x is installed on your system.
3. Install the required Python packages:

```bash
pip install openai
```

4. Create a `config.json` file in the root directory with your OpenAI API key:

```json
{
    "openai_api_key": "your_openai_api_key_here"
}
```

## Usage

1. Update `comments.json` with your product comments.
2. Update `categories.json` with the categories relevant to your product.
3. Run the script:

```bash
python categorize_comments.py
```

4. Check `categorized_comments.json` for the categorized comments.

## Security Note

Do not commit `config.json` to your repository. Ensure it's listed in your `.gitignore` file to prevent exposing your OpenAI API key.