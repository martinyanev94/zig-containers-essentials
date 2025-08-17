from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

input_text = "Once upon a time in a land far away,"
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate text
outputs = model.generate(input_ids, max_length=50, num_return_sequences=3)

for i, output in enumerate(outputs):
    print(f"Generated Text {i + 1}: {tokenizer.decode(output, skip_special_tokens=True)}")
