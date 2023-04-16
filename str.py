name = "Harry"
print(type(name))
greeting = "Good Morning"
print(greeting + name)
c = greeting + name
print(c)

# Concatenting two strings
name = "Harry"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[0:3])
print(name[:4])
print(name[1:])
c = name[-4:-1]
print(c)

d = name[1:4:1]
print(d)
e = name[1:4:2]
print(e)


story =  "Once upon a time there was a youtuber name harry who uploaded python course with notes"
print(story[0:5])
print(len(story))

print(story.endswith("sdjflsdfj"))
print(story.endswith("notes"))


print(story.count("o"))
print(story.count("a"))
print(story.count("course"))
print(story.capitalize())

print(story.find("harry"))
print(story.find("Once"))
print(story.replace("harry","code with harry"))


# Escape sequence character
story = "Shraddha is good.\n She \t is very good"
print(story)





 Q 2-------
st = "This is a string with double -- spaces"
st = st.replace(" "," ")
print(st)ss