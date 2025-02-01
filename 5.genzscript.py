from transformers import pipeline


text_generator = pipeline("text-generation", model="facebook/opt-1.3b", device="cpu")  


def generate_genz_script(text):
   
    prompt = (
        f"Rewrite this in a fun, engaging GenZ style for a 25-30 sec reel: \n\n"
        f"{text}\n\n"
        "Keep it punchy, use emojis, slang, and make it super engaging. No academic tone, just pure vibes! 🚀🔥"
    )


    genz_script = text_generator(
        prompt,
        max_length=300, 
        num_return_sequences=1,
        temperature=0.9,
        top_p=0.85, 
        do_sample=True, 
        truncation=True 
    )


    return genz_script[0]['generated_text']


final_summary_short = generate_genz_script(final_summary)
print("GenZ Script:\n", final_summary)