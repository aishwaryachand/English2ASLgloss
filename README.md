
## 🧠 English to ASL Gloss Translator (T5-based)

This project implements a lightweight translation pipeline that converts English sentences to American Sign Language (ASL) gloss. It leverages a fine-tuned [`t5-small`](https://huggingface.co/t5-small) model and provides an easy-to-use interface via [Streamlit](https://streamlit.io/).

---
![WhatsApp Image 2025-05-03 at 2 28 56 PM](https://github.com/user-attachments/assets/29910e50-d8e5-44bf-a6ee-70aa88e80f92)


### 🚀 Features

* ✅ Converts English text to ASL gloss format
* ✅ Fine-tuned on expert-labelled and pseudo-labelled datasets
* ✅ Streamlit web app for interactive testing
* ✅ Lightweight and easy to deploy locally

---

### 📂 Project Structure

```
.
├── app.py                       # Streamlit web app
├── requirements.txt            # Dependencies
├── final_t5_gloss_model/       # Fine-tuned T5 model (not included here)
└── README.md                   # You're reading this!
```

---

### ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/aishwaryachand/English2ASLgloss.git
cd English2ASLgloss
```

2. **(Optional) Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Download the model (if not included)**

> Due to GitHub file size limits, the fine-tuned model is not stored in this repo.

📥 [Download model folder (`final_t5_gloss_model/`) from Google Drive](https://your-download-link.com)
Then place it in the root directory.

---

### 🖥️ Run the Streamlit App

```bash
streamlit run app.py
```

Visit: [http://localhost:8501](http://localhost:8501)

---

### ✨ Sample Usage

Input:

```
The children are playing in the park.
```

Output (Gloss):

```
CHILDREN PLAY PARK
```

---

### 🛠️ Model Details

* **Base model:** `t5-small`
* **Pretraining:** Pseudo-labeled noisy gloss data
* **Fine-tuning:** Expert-annotated English–Gloss pairs
* **Tokenization:** SentencePiece-based T5 tokenizer

---

### 📌 TODO

* [ ] Add Hugging Face demo space
* [ ] Improve gloss accuracy via multi-task finetuning
* [ ] Add ASL video synthesis pipeline (future work)

---

### 📄 License

MIT License © 2025 Aishwarya Chand

