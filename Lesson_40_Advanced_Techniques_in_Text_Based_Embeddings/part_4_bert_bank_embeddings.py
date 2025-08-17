from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

sentence_1 = "I went to the bank to deposit money."
sentence_2 = "The river bank was flooded."

inputs_1 = tokenizer(sentence_1, return_tensors='pt')
inputs_2 = tokenizer(sentence_2, return_tensors='pt')

with torch.no_grad():
    outputs_1 = model(**inputs_1)
    outputs_2 = model(**inputs_2)

# Get the embeddings for the first token (the word "bank")
bank_embedding_1 = outputs_1.last_hidden_state[0, 5]  # 5 corresponds to the token "bank"
bank_embedding_2 = outputs_2.last_hidden_state[0, 5]

print(bank_embedding_1)
print(bank_embedding_2)
