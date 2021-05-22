import csv, json, argparse

parser = argparse.ArgumentParser(description='Language parser from CSV to JSON.')
parser.add_argument("--file", help="Input CSV file", required=True)
parser.add_argument("--language", help="Output language. Current supported languages: en-GB, de-DE, fr-FR, es-ES, ru-RU, pt-BR", required=True)

args = parser.parse_args()
print("Extracting " + args.language + " translations from " + args.file)

# Convert language codes to ISO language codes, because standards.
if args.language == "en-GB":
    lang = "UK"
elif args.language == "de-DE":
    lang = "DE"
elif args.language == "fr-FR":
    lang = "FR"
elif args.language == "es-ES":
    lang = "ES"
elif args.language == "ru-RU":
    lang = "RU"
elif args.language == "pt-BR":
    lang = "Pr/BR"


data = {}
csvfile = open(args.file, 'r')
jsonfile = open(args.language + '.json', 'w')

csvReader = csv.DictReader( csvfile, delimiter=';')
for row in csvReader:
    key = row['Name']
    data[key] = {"Name": row[lang + " Name"],"Description": row[lang + " Discript"]}

json.dump(data, jsonfile, indent=4)
