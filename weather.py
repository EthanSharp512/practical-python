from pydoc import tempfilepager


temperature = 75
forecast = "rain"

if temperature > 80 or temperature < 60:
    print("It's too hot!")
else:
    print("Enjoy the outdoors!")


if not forecast == "rain":
    print("Go outside!")
else:
    print("Stay inside!")