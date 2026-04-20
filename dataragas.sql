PRAGMA foreign_keys = ON;

-- Table: rāgas (known + generated)
DROP TABLE IF EXISTS ragas;
CREATE TABLE ragas (
    rāga_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_en TEXT NOT NULL,
    name_hindi TEXT,
    name_kannada TEXT,
    name_tamil TEXT,
    name_tulu TEXT,
    name_marathi TEXT,
    style TEXT NOT NULL CHECK(style IN ('karnatic', 'hindustani', 'western')),
    system TEXT,
    aarooha TEXT NOT NULL,
    avaroha TEXT NOT NULL,
    swara_set TEXT NOT NULL,
    shruti_lattice TEXT,
    is_janya BOOLEAN DEFAULT 0,
    parent_melakarta INTEGER,
    parent_thaat TEXT,
    origin TEXT NOT NULL CHECK(origin IN ('known', 'generated')),
    combo_hash TEXT UNIQUE,
    notes_en TEXT,
    notes_hindi TEXT,
    notes_kannada TEXT,
    notes_tamil TEXT,
    notes_tulu TEXT,
    notes_marathi TEXT
);

-- Table: krithis (songs / krithis)
DROP TABLE IF EXISTS krithis;
CREATE TABLE krithis (
    krithi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title_en TEXT NOT NULL,
    title_hindi TEXT,
    title_kannada TEXT,
    title_tamil TEXT,
    title_tulu TEXT,
    title_marathi TEXT,
    composer_en TEXT,
    composer_kannada TEXT,
    composer_hindi TEXT,
    composer_tamil TEXT,
    composer_tulu TEXT,
    composer_marathi TEXT,
    raaga_id INTEGER NOT NULL,
    language TEXT NOT NULL,
    style TEXT NOT NULL,
    is_template BOOLEAN DEFAULT 0,
    lyrics_en TEXT,
    lyrics_hindi TEXT,
    lyrics_kannada TEXT,
    lyrics_tamil TEXT,
    lyrics_tulu TEXT,
    lyrics_marathi TEXT,
    swara_notation TEXT,
    western_notation TEXT,
    FOREIGN KEY (raaga_id) REFERENCES ragas(rāga_id) ON DELETE CASCADE
);

-- Table: pitch_combinations (for infinite search)
DROP TABLE IF EXISTS pitch_combinations;
CREATE TABLE pitch_combinations (
    combo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shruti_lattice_string TEXT,
    swara_set_string TEXT,
    style TEXT NOT NULL,
    matched_raga_ids TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
