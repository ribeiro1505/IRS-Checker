import nifs
import keywords

def is_description_from_categorie(input_string, string_array):
    for substring in string_array:
        if substring in input_string:
            return True
    return False

def process_entries(file_path, category, possible_nifs, key_words):
    # Iterates the data to find possible nifs by previous cases or naming
    with open(file_path, 'r') as file:
        for line in file:
            line = line.replace('"', '')
            values = line.strip().split(';')

            setor = values[0].strip()
            name = values[1].strip()
            nif = name.split('-')[0].strip()

            if category in setor or is_description_from_categorie(name.upper(), key_words):
                if nif not in possible_nifs:
                    possible_nifs.append(nif)

    # Fetch for entries with possible misclassification
    with open(file_path, 'r') as file:
        for line in file:
            line = line.replace('"', '')
            values = line.strip().split(';')

            setor = values[0].strip()
            name = values[1].strip()
            date = values[5].strip()
            nif = name.split('-')[0].strip()
            price = values[7].replace("€", "").strip()

            if year in date and "Outros" in setor and nif in possible_nifs:
                print(f'{date}: NIF {name} classified as {setor} might be classified as {category}')


file_path = 'e-fatura.csv'
year = "2023"

process_entries(file_path, "restauração", nifs.food, keywords.food)
process_entries(file_path, "Educação", nifs.education, keywords.education)
process_entries(file_path, "Ginásios", nifs.gym, keywords.gym)
process_entries(file_path, "automóveis", nifs.car, keywords.car)
process_entries(file_path, "Saúde", nifs.health, keywords.health)
process_entries(file_path, "veterinárias", nifs.vet, keywords.vet)
process_entries(file_path, "transportes públicos", nifs.transportation, keywords.transportation)
process_entries(file_path, "cabeleireiro", nifs.hairdress, keywords.hairdress)