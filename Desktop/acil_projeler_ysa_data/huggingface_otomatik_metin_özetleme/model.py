from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Model ve Tokenizer'ı yükle
model_name = "facebook/bart-large-cnn"  # Alternatif: "t5-small", "google/pegasus-xsum"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Özetleme pipeline'ını başlat
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)