from openai import OpenAI
import os
import json

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)
def create_workout_plan():
  return client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={"type": "json_object"},
    messages=[
      {"role": "system", "content": "You are a fitness assistant, skilled in creating workout plans for users. Produce a json_object response"},
      # {"role": "user", "content": "Put together a workout plan for a 25 year old person.  They want a mix of cardio and strength exercises."}
      {"role": "user", "content": """
          The following fields should be used to determine a workout plan:
          "workout_name": "Push Day",
          "age": 25,
          "gender": male,
          "weight": 250,
          "height": 72",
          "goal": I know I want to do regular and incline bench, I also want to do some lateral raises towards the end of the workout,
          "experience": intermediate,
          "time": 1 hour,
          "target_muscle": [chest, triceps, shoulders],
          "equipment": home gym with bench and dumbbells,
          Use all of the above to create a plan, if a field is empty, use your best judgement to produce the plan.
          return a json object in the following format:
          "workout_name": "Workout Name",
          "notes": "Any helpful notes on the workout plan",
          "exercises": [
              {
                  "name": "Exercise Name",
                  "type": "type (strength, cardio, stretch)",
                  "muscle": "muscle",
                  "equipment": "equipment",
                  "description": "A description of the exercise",
              }
          ]
      """
      },
    ]
  )

completion = create_workout_plan()

print(completion.choices[0].message.content)

# Assuming `completion` is your ChatCompletionMessage object
json_content = completion.choices[0].message.content

# Convert the JSON string to a Python dictionary
data = json.loads(json_content)

# Write the data to a JSON file
with open('push_home.json', 'w') as f:
    json.dump(data, f, indent=4)