# water_resource_flask_app

## How to Run

1. Create virtual environment  
   - `python -m venv venv`  
   - Activate:  
     - Windows CMD → `venv\Scripts\activate`  
     - Windows PowerShell → `.\venv\Scripts\Activate.ps1`  
     - Mac/Linux → `source venv/bin/activate`

2. Install packages  
   - `pip install -r requirements.txt`

3. Start the app  
   - `cd water_resource_flask`  
   - `python app.py`

4. Open in browser → [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Features
- Home page with modules + calculator  
- Calculator uses `/calculate` API  
- Upload CSV for basic analytics (saved in `uploads/`)  
- Contact form saves data in `uploads/contacts.jsonl`  
- Narration audio in `static/assets/`  
