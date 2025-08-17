
with open("input.txt", "w") as f:
    f.write("Python is amazing!\n")
    f.write("File handling is fun.\n")
    f.write("We can read and write files.\n")

with open("input.txt", "r") as f:
    content = f.read()

lines = content.splitlines()
modified_lines = [f"{i+1}: {line.upper()}" for i, line in enumerate(lines)]
modified_text = "\n".join(modified_lines)

with open("output.txt", "w") as f:
    f.write(modified_text)

print("Modified file created as 'output.txt'")
