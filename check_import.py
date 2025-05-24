import google.generativeai as genai
print(genai)
print(genai.__file__ if hasattr(genai, '__file__') else 'No __file__ attribute')
print(dir(genai))
