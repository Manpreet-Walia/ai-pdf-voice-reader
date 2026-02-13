from transformers import pipeline

# Load text-generation pipeline with T5 model
summarizer = pipeline(
    "text-generation",
    model="t5-small"
)

# Read extracted text
with open("extracted_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Take a safe portion (first ~400 words)
words = text.split()
sample_text = "summarize: " + " ".join(words[:400])

# Generate summary
output = summarizer(
    sample_text,
    max_length=150,
    do_sample=False
)

print("\n--- SUMMARY ---\n")
print(output[0]["generated_text"])

