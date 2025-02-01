from IPython import get_ipython
from IPython.display import display
!pip install PyMuPDF transformers

import fitz
from transformers import pipeline, AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    return text

pdf_path = "Addressing_the_Productivity_Paradox_in_Healthcare_with_Retrieval_Augmented_Generative_AI_Chatbots.pdf"
text = extract_text_from_pdf(pdf_path)

if not text.strip():
    raise ValueError("Extracted text is empty. Check if the PDF has selectable text.")

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer=tokenizer) 


def split_text(text, chunk_size=256): 
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

text_chunks = split_text(text, chunk_size=256) 


summaries = [summarizer(chunk, max_length=200, min_length=50, do_sample=False, truncation=True)[0]['summary_text'] for chunk in text_chunks]

final_summary = "\n".join(summaries)

print("Final Summary:\n", final_summary)