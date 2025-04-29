from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def auto_summarize(text):
    model_name = "facebook/bart-large-cnn"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    inputs = tokenizer([text], max_length=1024, truncation=True, return_tensors="pt")
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=150,
        min_length=50,
        length_penalty=2.0,
        num_beams=4
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Kullanım
input_text = """
Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to natural intelligence 
displayed by animals including humans. Leading AI textbooks define the field as the study of intelligent agents: 
any system that perceives its environment and takes actions that maximize its chance of achieving its goals. 
AI applications include advanced web search engines, recommendation systems, understanding human speech, 
self-driving cars, automated decision-making, and competing at the highest level in strategic game systems.
"""
print(auto_summarize(input_text))