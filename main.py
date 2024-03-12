from openai import OpenAI
import os
import json

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  response_format={"type": "json_object"},
  messages=[
    {"role": "system", "content": "You are a fitness assistant, skilled in creating workout plans for users. Produce a json_object response"},
    # {"role": "user", "content": "Put together a workout plan for a 25 year old person.  They want a mix of cardio and strength exercises."}
    {"role": "user", "content": """{
        "age": 25,
        "goal": "strength exercises for a push, pull, legs split, for this entry, a push day with focus on chest and triceps",
        "experience": "intermediate",
        "equipment": "gym",
        "return format": "return a json list of exercises with name, type (cardio or strength), target muscle, and description of the exercise. Also include a brief description of the workout plan."
    }"""
    },
  ]
)

print(completion.choices[0].message.content)

# Assuming `completion` is your ChatCompletionMessage object
json_content = completion.choices[0].message.content

# Convert the JSON string to a Python dictionary
data = json.loads(json_content)

# Write the data to a JSON file
with open('workout_plan.json', 'w') as f:
    json.dump(data, f, indent=4)