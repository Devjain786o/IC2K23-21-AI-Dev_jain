
"""
Knowledge Representation and Logical Reasoning
"""

# 1. Predicate Representation
print("1. PREDICATE REPRESENTATION")

facts = [
    ("student", "Student1"),
    ("studies", "Student1", "Artificial Intelligence"),
    ("has_topic", "Artificial Intelligence", "Machine Learning"),
    ("has_topic", "Artificial Intelligence", "Knowledge Representation")
]

for item in facts:
    print(item)


# 2. Logical Inference
print("\n2. LOGICAL INFERENCE")

new_facts = []

for item in facts:

    if item[0] == "studies":

        person = item[1]
        subject = item[2]

        for relation in facts:

            if relation[0] == "has_topic" and relation[1] == subject:

                result = ("learns", person, relation[2])
                new_facts.append(result)

print("Inferred Facts:")

for item in new_facts:
    print(item)


# 3. Semantic Network
print("\n3. SEMANTIC NETWORK")

network = {
    "Student1": {
        "is_a": "Student",
        "studies": "Artificial Intelligence"
    },

    "Artificial Intelligence": {
        "is_a": "Subject",
        "has_topic": [
            "Machine Learning",
            "Knowledge Representation"
        ]
    }
}

for name, details in network.items():
    print(name, "->", details)


# 4. Frame Representation
print("\n4. FRAME REPRESENTATION")

frame = {
    "Frame_Name": "Student",
    "Name": "Student1",
    "Course": "B.Tech",
    "Subject": "Artificial Intelligence",
    "Year": "Third Year"
}

for attribute, value in frame.items():
    print(attribute, ":", value)


# 5. Conceptual Dependency
print("\n5. CONCEPTUAL DEPENDENCY")

dependency = {
    "Actor": "Student1",
    "Action": "TRANSFER",
    "Object": "Book",
    "From": "Library",
    "To": "Classroom"
}

for attribute, value in dependency.items():
    print(attribute, ":", value)


# 6. Rule-Based System
print("\n6. RULE-BASED SYSTEM")

temperature = 32
is_present = True

if temperature > 30 and is_present:

    print("Rule: IF temperature > 30 AND person is present")
    print("THEN switch ON the fan")
    print("Decision: Fan switched ON")

else:

    print("Decision: Fan remains OFF")


print("\nAll operations completed successfully!")
