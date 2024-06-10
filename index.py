import os
import textwrap
import pathlib
import google.generativeai as genai


def get_meaning_response():
  #retrieve the API KEY
  api_key = os.getenv("API_KEY")

  if not api_key:
    raise Exception("API_KEY not set")

  genai.configure(api_key=api_key)
  """Fetches a response about the meaning of life using genai"""
  model = genai.GenerativeModel('gemini-1.5-flash')
  response = model.generate_content("What is the meaning of life?")
  return (response.text)

meaning_response = get_meaning_response()

print(meaning_response)

