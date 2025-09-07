from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
msg = "I feel hopeless today"
print(classifier(msg))
