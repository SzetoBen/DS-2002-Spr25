#!/Program Files/Python311
import os

FAV_ANIMAL = input('What is your favorite animal?')
FAV_COLOR = input('What is your favorite color?')
YEAR = input('What year are you at UVA?')

os.environ["FAV_ANIMAL"] = FAV_ANIMAL
os.environ["FAV_COLOR"] = FAV_COLOR
os.environ["YEAR"] = YEAR

print(os.getenv("FAV_ANIMAL"))
print(os.getenv("FAV_COLOR"))
print(os.getenv("YEAR"))