# Support Triage AI

An AI-powered customer support triage assistant that analyzes customer messages, detects sentiment, classifies the issue, and suggests the next best action — all with support for comparing multiple LLMs (Granite, Llama3, Mixtral).

Built with **Flask**, **LangChain**, and **WatsonX / Hugging Face models**, this project showcases applied AI integration in real-world workflows.

---

Live Demo

[TBD]

---

Features

Accepts free-form customer messages
Uses LLMs to:
Classify issues (Billing, Tech, Complaint, etc.)
Assess sentiment (0–100 scale)
Summarize the message
Suggest a next step
Compares responses from multiple models side-by-side
Clean web interface with Flask
Displays response time per model
Keeps API keys secure via `.env`

---

Tech Stack

| Layer         | Tech                     |
|---------------|---------------------------|
| Backend       | Flask (Python)            |
| AI Framework  | LangChain                 |
| LLMs          | IBM watsonx.ai (Granite), Hugging Face (Llama3, Mixtral) |
| UI            | HTML + JavaScript         |
| Deployment    | Render (recommended)      |

---

Screenshots





Getting Started

1. Clone the repository

```bash
git clone https://github.com/your-username/support-triage-ai.git
cd support-triage-ai

2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure .env
Create a .env file based on the example:
WATSONX_APIKEY=your_key_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_PROJECT_ID=your_project_id

5. Run the app
python app.py

Then go to http://localhost:5000

Prompt Logic
The app sends a system prompt like:
"You are an AI support assistant. Your job is to analyze a customer message, categorize the issue, assess sentiment (0–100), summarize it, and suggest the next step. Respond in structured JSON format only."
The output is parsed and rendered in a clean table for comparison.

🧰 Folder Structure
support-triage-ai/
│
├── app.py               # Flask routes and logic
├── model.py             # LangChain + LLM logic
├── templates/
│   └── index.html       # Frontend UI
├── .env.example         # Environment config template
├── .gitignore
├── requirements.txt
└── README.md

🌟 Use Cases
This app can be adapted into:
Customer support assistants
1. Email triage tools
2. LLM evaluation platforms
3. Product feedback analyzers


License
MIT License

🙋‍♂️ Author
Eric M Seukep. 
I built this as a hands-on GenAI + Flask project
Let’s connect on LinkedIn (/in/emseukep/) and collaborate!
