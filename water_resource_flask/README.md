
Water Resource Management - Flask Demo

1. Create a Python virtualenv:
   python -m venv venv
   venv\Scripts\activate   (Windows)
   source venv/bin/activate  (Mac/Linux)

2. Install requirements:
   pip install -r requirements.txt

3. Run:
   python app.py
   Open http://127.0.0.1:5000 in your browser.

Features:
- Home page with modules and calculator
- Calculator calls /calculate API
- CSV upload for basic analytics (uploads saved to uploads/)
- Contact form saves submissions to uploads/contacts.jsonl
- Narration audio included in static/assets/
