# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Germany"] = "Rhine"
rivers["Egypt"] = "Nile"
print(rivers)
# Display all the keys
rivers.keys()
print(rivers.keys())
# Display all the values
rivers.values()
print(rivers.values())
# Display all the key:value pairs, as tuples
rivers.items()
print(rivers.items())
# Delete an entry from the rivers database
del rivers["London"]
print(rivers)
