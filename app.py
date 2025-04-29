# app.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import gradio as gr

# 1. Model ve Tokenizer'ı yükle
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 2. Cevap Üretme Fonksiyonu
def generate_response(user_input, chat_history=[]):
    # Girdiyi tokenize et
    inputs = tokenizer.encode(
        user_input + tokenizer.eos_token, 
        return_tensors="pt"
    )
    
    # Cevap oluştur
    outputs = model.generate(
        inputs,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=100,
        top_p=0.7,
        temperature=0.8
    )
    
    # Cevabı decode et
    response = tokenizer.decode(
        outputs[:, inputs.shape[-1]:][0], 
        skip_special_tokens=True
    )
    
    return response

# 3. Gradio Arayüzü
def chat_ui(user_input, history):
    response = generate_response(user_input)
    history.append((user_input, response))
    return history, history

# 4. Uygulamayı Başlat
with gr.Blocks(title="Sohbet Botu") as demo:
    gr.Markdown("## 🤖 DialoGPT ile Sohbet Edin!")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Mesajınızı yazın", placeholder="Bir şeyler yazın...")
    clear = gr.Button("Sohbeti Temizle")

    msg.submit(chat_ui, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch()