#!/usr/bin/env python3
"""
ByteStackLab Icon Generator
Generates SVG icons using the ByteStackLab Material Theme color palette
"""

import os

# === ByteStackLab Color Palette ===
COLORS = {
    "teal":    "#80CBC4",
    "blue":    "#82AAFF",
    "purple":  "#C792EA",
    "yellow":  "#FFCB6B",
    "green":   "#C3E88D",
    "red":     "#f07178",
    "orange":  "#F78C6C",
    "cyan":    "#89DDFF",
    "white":   "#EEFFFF",
    "bg":      "#212121",
    "dark_teal": "#546E7A",
    "darker_teal": "#37474F",
    "pink":    "#ff9cac",
}

ICONS_DIR = os.path.join(os.path.dirname(__file__), "icons", "files")
FOLDERS_DIR = os.path.join(os.path.dirname(__file__), "icons", "folders")
os.makedirs(ICONS_DIR, exist_ok=True)
os.makedirs(FOLDERS_DIR, exist_ok=True)


def file_base(body_color, label_color=None, letter="", corner_color=None):
    """Generates a base file SVG with a dog-ear corner."""
    body = body_color
    corner = corner_color or label_color or body_color
    text = ""
    if letter:
        text = f'<text x="12" y="17" text-anchor="middle" font-family="monospace" font-weight="bold" font-size="7" fill="{label_color or COLORS["white"]}">{letter}</text>'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="{body}" d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
  <polyline fill="{corner}" points="13 2 13 9 20 9"/>
  {text}
</svg>"""


def folder_svg(color, open_state=False):
    """Generates a folder SVG."""
    if open_state:
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="{color}" d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
  <path fill="{color}CC" d="M2 10h20"/>
</svg>"""
    else:
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="{color}" d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
</svg>"""


# ========================================================
# FILE ICON DEFINITIONS
# (name, body_color, letter, letter_color, corner_color)
# ========================================================
FILE_ICONS = [
    # Default
    ("file",        COLORS["dark_teal"],  "",    None,               COLORS["darker_teal"]),

    # Web / Frontend
    ("html",        COLORS["orange"],     "H",   COLORS["bg"],       "#E64A19"),
    ("css",         COLORS["blue"],       "C",   COLORS["bg"],       "#1565C0"),
    ("scss",        COLORS["pink"],       "S",   COLORS["bg"],       "#AD1457"),
    ("sass",        COLORS["pink"],       "S",   COLORS["bg"],       "#AD1457"),
    ("less",        COLORS["purple"],     "L",   COLORS["bg"],       "#6A1B9A"),
    ("js",          COLORS["yellow"],     "JS",  COLORS["bg"],       "#F57F17"),
    ("jsx",         COLORS["cyan"],       "JX",  COLORS["bg"],       "#00838F"),
    ("ts",          COLORS["blue"],       "TS",  COLORS["bg"],       "#1565C0"),
    ("tsx",         COLORS["teal"],       "TX",  COLORS["bg"],       "#00695C"),
    ("vue",         COLORS["green"],      "V",   COLORS["bg"],       "#2E7D32"),
    ("svelte",      COLORS["red"],        "SV",  COLORS["white"],    "#B71C1C"),

    # Data / Config
    ("json",        COLORS["yellow"],     "{}",  COLORS["bg"],       "#F57F17"),
    ("yaml",        COLORS["red"],        "Y",   COLORS["white"],    "#B71C1C"),
    ("yml",         COLORS["red"],        "Y",   COLORS["white"],    "#B71C1C"),
    ("toml",        COLORS["orange"],     "T",   COLORS["bg"],       "#E64A19"),
    ("xml",         COLORS["orange"],     "X",   COLORS["bg"],       "#E64A19"),
    ("csv",         COLORS["green"],      "CSV", COLORS["bg"],       "#2E7D32"),
    ("env",         COLORS["teal"],       "E",   COLORS["bg"],       "#00695C"),

    # Backend / Languages
    ("py",          COLORS["blue"],       "Py",  COLORS["bg"],       "#1565C0"),
    ("rb",          COLORS["red"],        "Rb",  COLORS["white"],    "#B71C1C"),
    ("php",         COLORS["purple"],     "PHP", COLORS["white"],    "#6A1B9A"),
    ("java",        COLORS["red"],        "Ja",  COLORS["white"],    "#B71C1C"),
    ("kt",          COLORS["purple"],     "Kt",  COLORS["white"],    "#6A1B9A"),
    ("go",          COLORS["cyan"],       "Go",  COLORS["bg"],       "#00838F"),
    ("rs",          COLORS["orange"],     "Rs",  COLORS["bg"],       "#E64A19"),
    ("c",           COLORS["blue"],       "C",   COLORS["bg"],       "#1565C0"),
    ("cpp",         COLORS["blue"],       "C++", COLORS["bg"],       "#1565C0"),
    ("cs",          COLORS["purple"],     "C#",  COLORS["white"],    "#6A1B9A"),
    ("swift",       COLORS["orange"],     "Sw",  COLORS["bg"],       "#E64A19"),
    ("lua",         COLORS["blue"],       "Lu",  COLORS["bg"],       "#1565C0"),
    ("r",           COLORS["blue"],       "R",   COLORS["bg"],       "#1565C0"),

    # Shell / Scripts
    ("sh",          COLORS["green"],      "$",   COLORS["bg"],       "#2E7D32"),
    ("bash",        COLORS["green"],      "$",   COLORS["bg"],       "#2E7D32"),
    ("zsh",         COLORS["green"],      "Z$",  COLORS["bg"],       "#2E7D32"),
    ("ps1",         COLORS["blue"],       "PS",  COLORS["bg"],       "#1565C0"),

    # Docs
    ("md",          COLORS["white"],      "M",   COLORS["bg"],       "#546E7A"),
    ("mdx",         COLORS["teal"],       "MX",  COLORS["bg"],       "#00695C"),
    ("txt",         COLORS["white"],      "T",   COLORS["bg"],       "#546E7A"),
    ("pdf",         COLORS["red"],        "PDF", COLORS["white"],    "#B71C1C"),

    # Images
    ("png",         COLORS["purple"],     "IMG", COLORS["white"],    "#6A1B9A"),
    ("jpg",         COLORS["purple"],     "IMG", COLORS["white"],    "#6A1B9A"),
    ("jpeg",        COLORS["purple"],     "IMG", COLORS["white"],    "#6A1B9A"),
    ("gif",         COLORS["purple"],     "GIF", COLORS["white"],    "#6A1B9A"),
    ("svg",         COLORS["teal"],       "SVG", COLORS["bg"],       "#00695C"),
    ("webp",        COLORS["purple"],     "IMG", COLORS["white"],    "#6A1B9A"),

    # Database
    ("sql",         COLORS["cyan"],       "SQL", COLORS["bg"],       "#00838F"),
    ("prisma",      COLORS["teal"],       "P",   COLORS["bg"],       "#00695C"),

    # Config / Build
    ("gitignore",   COLORS["orange"],     "GI",  COLORS["bg"],       "#E64A19"),
    ("dockerfile",  COLORS["cyan"],       "🐳",  COLORS["bg"],       "#00838F"),
    ("lock",        COLORS["red"],        "🔒",  COLORS["white"],    "#B71C1C"),

    # Package managers
    ("package",     COLORS["red"],        "npm", COLORS["white"],    "#B71C1C"),
]

# ========================================================
# FOLDER ICON DEFINITIONS
# ========================================================
FOLDER_ICONS = [
    ("folder",           COLORS["yellow"],  False),
    ("folder-open",      COLORS["yellow"],  True),
    ("folder-src",       COLORS["blue"],    False),
    ("folder-src-open",  COLORS["blue"],    True),
    ("folder-test",      COLORS["green"],   False),
    ("folder-test-open", COLORS["green"],   True),
    ("folder-node",      COLORS["green"],   False),
    ("folder-node-open", COLORS["green"],   True),
    ("folder-git",       COLORS["orange"],  False),
    ("folder-git-open",  COLORS["orange"],  True),
    ("folder-dist",      COLORS["red"],     False),
    ("folder-dist-open", COLORS["red"],     True),
    ("folder-public",    COLORS["teal"],    False),
    ("folder-public-open", COLORS["teal"], True),
    ("folder-img",       COLORS["purple"],  False),
    ("folder-img-open",  COLORS["purple"],  True),
    ("folder-doc",       COLORS["white"],   False),
    ("folder-doc-open",  COLORS["white"],   True),
    ("folder-components",COLORS["cyan"],    False),
    ("folder-components-open", COLORS["cyan"], True),
    ("folder-config",    COLORS["orange"],  False),
    ("folder-config-open", COLORS["orange"], True),
    ("folder-scripts",   COLORS["green"],   False),
    ("folder-scripts-open", COLORS["green"], True),
]


def generate_icons():
    count = 0
    # File icons
    for name, body, letter, letter_color, corner in FILE_ICONS:
        svg = file_base(body, letter_color, letter, corner)
        path = os.path.join(ICONS_DIR, f"{name}.svg")
        with open(path, "w") as f:
            f.write(svg)
        count += 1

    # Folder icons
    for name, color, open_state in FOLDER_ICONS:
        svg = folder_svg(color, open_state)
        path = os.path.join(FOLDERS_DIR, f"{name}.svg")
        with open(path, "w") as f:
            f.write(svg)
        count += 1

    print(f"✅ Generated {count} icons successfully!")
    print(f"   📁 File icons:   {ICONS_DIR}")
    print(f"   📁 Folder icons: {FOLDERS_DIR}")


if __name__ == "__main__":
    generate_icons()
