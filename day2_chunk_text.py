# Day 2: Text Chunking

CHUNK_SIZE = 100  # words per chunk

with open("extracted_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()
chunks = []

for i in range(0, len(words), CHUNK_SIZE):
    chunk = words[i:i + CHUNK_SIZE]
    chunks.append(" ".join(chunk))

print("Total chunks created:", len(chunks))

# Print first 2 chunks as verification
for idx, chunk in enumerate(chunks[:2]):
    print(f"\n--- Chunk {idx + 1} ---")
    print(chunk[:500], "...")
