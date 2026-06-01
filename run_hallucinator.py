import bibtexparser
from hallucinator import Validator, ValidatorConfig, Reference

print("1. Lecture du fichier dissertation.bib...")
with open("Thesis/dissertation.bib", "r", encoding="utf-8") as f:
    bib_database = bibtexparser.load(f)

references_objets = []
for entry in bib_database.entries:
    if 'title' in entry:
        title = entry['title'].replace('{', '').replace('}', '')
        auteurs_bruts = entry.get('author', '')
        auteurs = [a.strip() for a in auteurs_bruts.replace('\n', ' ').split(' and ') if a.strip()]
        references_objets.append(Reference(title, authors=auteurs))

print(f"2. {len(references_objets)} références structurées avec succès.")
print("3. Initialisation du validateur...")

config = ValidatorConfig()
validator = Validator(config)

print("4. Requêtes de validation en cours (cela peut prendre quelques secondes par papier)...")
results = validator.check(references_objets)

print("\n--- RÉSULTATS OFFICIELS ---")
for r in results:
    print(f"[{r.status}] {r.title}")
