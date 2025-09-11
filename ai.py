from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Based on the following transcript, generate a quiz in valid JSON format.\n\nThe quiz must follow this exact structure:\n\n{{\n\n  \"title\": \"Create a concise quiz title based on the topic of the transcript.\",\n\n  \"description\": \"Summarize the transcript in no more than 150 characters. Do not include any quiz questions or answers.\",\n\n  \"questions\": [\n\n    {{\n\n      \"question_title\": \"The question goes here.\",\n\n      \"question_options\": [\"Option A\", \"Option B\", \"Option C\", \"Option D\"],\n\n      \"answer\": \"The correct answer from the above options\"\n\n    }},\n\n    ...\n\n    (exactly 10 questions)\n\n  ]\n\n}}\n\nRequirements:\n\n- Each question must have exactly 4 distinct answer options.\n\n- Only one correct answer is allowed per question, and it must be present in 'question_options'.\n\n- The output must be valid JSON and parsable as-is (e.g., using Python's json.loads).\n\n- Do not include explanations, comments, or any text outside the JSON." + 
)

print(response.text)