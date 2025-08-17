model.eval()
test_dataset = MovieReviewDataset(test_texts, test_labels, tokenizer, max_length=128)
test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)

predictions = []
with torch.no_grad():
    for batch in test_loader:
        input_ids = batch['input_ids']
        attention_mask = batch['attention_mask']
        outputs = model(input_ids, attention_mask=attention_mask)
        preds = torch.argmax(outputs.logits, dim=1)
        predictions.extend(preds.cpu().numpy())
