from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".", template_folder=".")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.json
    style = data.get("style", "karnatic")
    swara_set = data.get("swara_set", "")
    shruti_lattice = data.get("shruti_lattice", "")
    target_langs = data.get("target_languages", ["en"])

    # In real code: use swara_set + shruti_lattice to:
    # - match or generate a rāga‑class
    # - link/generate krithis with multi‑lang lyrics
    # Here we return a fixed example to match the front‑end.

    return jsonify({
        "matched_ragas": [
            {
                "rāga_id": 123,
                "name_en": "Generated‑Raga‑ABCD12",
                "name_hindi": "जनरेटेड‑राग‑ABCD12",
                "name_kannada": "ಜನರೇಟೆಡ್‑ರಾಗ‑ABCD12",
                "name_tamil": "ஜெனரேட்டட்‑ராகா‑ABCD12",
                "name_tulu": "Gen‑Raga‑ABCD12",
                "name_marathi": "उत्पन्न‑राग‑ABCD12",
                "style": style,
                "aarooha": "S R2 G3 M1 P D2 N3 S",
                "avaroha": "S N3 D2 P M1 G3 R2 S",
                "notes_en": "A raga created from your chosen swara‑sthanas and 22‑śruti lattice.",
                "notes_hindi": "यह राग आपके चुने हुए स्वर‑स्थानों से बनाया गया है।",
                "notes_kannada": "ನೀವು ಆಯ್ಕೆ ಮಾಡಿದ ಸ್ವರ‑ಸ್ಥಾನಗಳಿಂದ ಸೃಷ್ಟಿಸಿದ ರಾಗ.",
                "notes_tamil": "நீங்கள் தேர்ந்தெடுத்த சுவரா-ஸ்தானங்களால் உருவாக்கப்பட்ட ராகா.",
                "notes_tulu": "ನಿಮ್ಮ ಆಯ್ಕೆಯ ಸ್ವರ‑ಸ್ಥಾನಗಳಿಂದ ಸೃಷ್ಟಿಸಲಾದ ರಾಗ.",
                "notes_marathi": "आपण निवडलेल्या स्वर‑स्थानांवर आधारित राग."
            }
        ],
        "krithis": [
            {
                "krithi_id": 1001,
                "title_en": "Infinite‑Raga‑Song‑1",
                "lyrics_en": "Sādhanā rāga vibhāti, bhakti madhura kīrtaṇa...\nLine‑2\nLine‑3",
                "lyrics_hindi": "साधना राग विभाति, भक्ति मधुर कीर्तन...\nपंक्ति‑2\nपंक्ति‑3",
                "lyrics_kannada": "ಸಾಧನಾ ರಾಗ ವಿಭಾತಿ, ಭಕ್ತಿ ಮಧುರ ಕೀರ್ತನ...\nಸಾಲ‑2\nಸಾಲ‑3",
                "lyrics_tamil": "சாதனா ராக விபாதி, பக்தி மதுர கீர்தன...\nவரி‑2\nவரி‑3",
                "lyrics_tulu": "ಸಾಧನಾ ರಾಗ ವಿಭಾತಿ, ಭಕ್ತಿ ಮಧುರ ಕೀರ್ತನ...\nಸಾಲಿ‑2\nಸಾಲಿ‑3",
                "lyrics_marathi": "साधना राग विभाति, भक्ति मधुर कीर्तन...\nओळ‑2\nओळ‑3",
                "swara_notation": "S R2 G3 M1 P D2 N3 S\nP N3 D2 P M1 G3 R2 S\nS R2 G3 M1 P D2 N3 S",
                "western_notation": "C D E F G A B C\nG B A G F E D C\nC D E F G A B C"
            }
        ],
        "target_languages": target_langs
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
