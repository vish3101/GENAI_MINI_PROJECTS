# GENAI_MINI_PROJECTS

This repository contains three mini projects built using **Google's Gemini 1.5 Flash Model**, showcasing both **text** and **vision-based** GenAI use cases with **Streamlit**, **prompt engineering**, and more.

---

## Technologies Used

- Google Gemini 1.5 Flash Model  
- Streamlit  
- Prompt Engineering  
- Python  

---

## Project Overview

### Q&A Bot
Ask any question and Gemini will respond with an answer. Using `st.session_state`, the bot remembers the context of the ongoing session — giving it a memory effect.

**Features:**
- Ask anything using the Streamlit interface.
- Gemini responds in real time.
- Session memory is maintained per user session.

**Run:**
```bash
streamlit run q_a_bot.py
```

---

### Image to Text Prompt

Upload an image, and test how much and how accurately Gemini 1.5 Flash can extract text from it. Simple, direct visual understanding.

**Features:**

* Upload any image file.
* Gemini Vision model processes it directly.
* Extracted text is shown on screen.

**Run:**

```bash
streamlit run image_to_text_prompt.py
```

---

### Invoice Extractor

A two-step GenAI pipeline for extracting specific information from invoice images:

1. Extract raw text from the invoice using Gemini.
2. Use a prompt to extract specific invoice fields like invoice number, date, total, etc.

**Features:**

* Supports `.jpg` and `.png` invoice formats.
* Users can define what details they want to extract.
* Clean Streamlit interface.

**Run:**

```bash
streamlit run invoice_extractor.py
```

---

## Setup Instructions

Clone the repo and install dependencies.

```bash
git clone https://github.com/vish3101/GENAI_MINI_PROJECTS.git
cd GENAI_MINI_PROJECTS
pip install -r requirements.txt
```

Make sure you’ve set up access to Gemini via API key (set as an environment variable or inside the code).

---

##  Sample Files

* `invoice1.jpg`
* `invoice2.png`

These are sample images for testing the invoice extractor module.

---

## About Gemini 1.5 Flash

* Supports both text and image inputs.
* Lightweight and fast response model.
* Great for real-time GenAI applications.

---


---

## Acknowledgements

Built by **Vishva Chaudhary**  
This project explores practical applications of Google's Gemini models using simple Streamlit-based UIs for learning and experimentation.

---
