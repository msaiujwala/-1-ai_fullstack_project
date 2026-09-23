import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role" : "system",
            "content": "Give answers in 2 lines only."
        },
        {
            "role": "user",
            "content": "explain ai"
        }
    ]
)

print(response["message"]["content"])