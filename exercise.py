import webbrowser

user_input = input("Enter a URL: ")

webbrowser.open("https://www.google.com/search?q=" + user_input)