import glob
import re

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()

    # Wrap fontToggle
    content = re.sub(
        r"document\.getElementById\('fontToggle'\)\.addEventListener",
        r"if(document.getElementById('fontToggle')) document.getElementById('fontToggle').addEventListener",
        content
    )
    # Wrap darkToggle
    content = re.sub(
        r"document\.getElementById\('darkToggle'\)\.addEventListener",
        r"if(document.getElementById('darkToggle')) document.getElementById('darkToggle').addEventListener",
        content
    )
    # Wrap chantToggle / chantingToggle
    content = re.sub(
        r"document\.getElementById\('chant(ing)?Toggle'\)\.addEventListener",
        r"if(document.getElementById('chant\1Toggle')) document.getElementById('chant\1Toggle').addEventListener",
        content
    )

    with open(file, "w") as f:
        f.write(content)
print("Done fixing HTML files")
