print("Welcome to Madlibs! Fill in the blanks to create your own story. 😊")

noun1 = input("Enter a noun: ")
verb_past = input("Enter a verb (past tense): ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
noun2 = input("Enter another noun: ")

story = f"""
On a bright morning, a {adjective} {noun1} decided to visit {place}.  
As it {verb_past} through the streets, it stumbled upon a strange {noun2}.  
Curious and excited, it picked it up and discovered something magical inside!  
What could it be? The adventure begins now!
"""

print("\nHere's your story:")
print(story)
