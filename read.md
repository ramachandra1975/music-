# Infinite Rāga Swara‑Sthāna Song Explorer

This is a web app that lets you:

- Input **swara‑sthanas** (e.g., S R2 G3 M1 P D2 N3)  
- Input **22‑śruti lattice** (indices like 2‑4‑7‑9‑12‑14‑17)  
- Choose **languages** (English, Hindi, Kannada, Tamil, Tulu, Marathi)  
- Get **generated songs** (with lyrics + swara & Western notations) for **Karnatic, Hindustani, and Western** styles.

## How to run

1. Create a virtual environment (optional):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   # or: venv\Scripts\activate  # Windows
   ```

2. Install Flask:

   ```bash
   pip install flask
   ```

3. Run the server:

   ```bash
   python server.py
   ```

4. Open in browser:

   Go to `http://localhost:5000` and use the form.

## Next steps (for you)

- Add a real `ragas` and `krithis` database (SQLite/PostgreSQL)  
- Replace the stub `/api/generate` with **infinite rāga‑generation and song‑template logic** based on 7 notes, 22 śrutis, and 12 swara‑sthanas.  
  - Enumerate all valid 7‑note, 6‑note, 5‑note rāga‑skeletons within 12‑swara‑sthanas. [web:34][web:36]  
  - Use 22‑śruti indices to model microtonal “flavor” of each rāga. [web:8][web:39]  
  - For each generated rāga‑class, either:
    - Fetch existing krithis from your database, or  
    - Generate a small templated krithi with lyrics in all selected languages.  
  - Ensure the front‑end continues to receive a JSON like:

    ```json
    {
      "matched_ragas": [ ... ],
      "krithis": [
        {
          "title_en": "...",
          "lyrics_en": "...",
          "lyrics_hindi": "...",
          "lyrics_kannada": "...",
          "lyrics_tamil": "...",
          "lyrics_tulu": "...",
          "lyrics_marathi": "...",
          "swara_notation": "...",
          "western_notation": "..."
        }
      ],
      "target_languages": ["en", "hindi", "kannada", "tamil", "tulu", "marathi"]
    }
