import json
import openai

def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config

config = load_config()
openai.api_key = config["openai_api_key"]

def categorize_comment(comment, categories, max_attempts=3):
    initial_prompt = f"Please categorize the following comment: \"{comment}\". Categories: {', '.join(categories)}."
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=initial_prompt,
        temperature=0.4,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    predicted_category = response.choices[0].text.strip()
    if predicted_category in categories:
        return predicted_category

    attempts = 0
    while attempts < max_attempts:
        refinement_prompt = f"Is the comment about \"{predicted_category}\"? Comment: \"{comment}\" Yes or No."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=refinement_prompt,
            temperature=0.4,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )
        answer = response.choices[0].text.strip().lower()
        if "yes" in answer:
            return predicted_category
        elif "no" in answer:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=initial_prompt,
                temperature=0.4,
                max_tokens=60,
                top_p=1.0,
                frequency_penalty=0.5,
                presence_penalty=0.0
            )
            predicted_category = response.choices[0].text.strip()
        attempts += 1
    
    return "unknown"

def main():
    with open('categories.json', 'r') as file:
        categories = json.load(file)

    with open('comments.json', 'r') as file:
        comments = json.load(file)

    categorized_comments = {}
    for comment in comments:
        category = categorize_comment(comment, categories)
        if category not in categorized_comments:
            categorized_comments[category] = [comment]
        else:
            categorized_comments[category].append(comment)

    with open('categorized_comments.json', 'w') as file:
        json.dump(categorized_comments, file, indent=4)

if __name__ == "__main__":
    main()
