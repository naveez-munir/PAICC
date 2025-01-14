# Read transcript file and store contents
with open('./transcript.txt', 'r') as file:
    transcript_content = file.read()

# Print first 100 characters as preview
print("First 100 characters of transcript:")
print(transcript_content[:100])
