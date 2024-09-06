import pandas as pd
from difflib import SequenceMatcher

def domain_similarity(domain1, domain2):
    return SequenceMatcher(None, domain1, domain2).ratio()

def load_phishing_domains(file_path):
    try:
        data = pd.read_csv(file_path, header=None, names=['domain'])
        return data['domain'].tolist()
    except Exception as e:
        print("Error loading data:", e)
        return []

def detect_phishing_domains(target_domains, phishing_domains, output_file, threshold=0.7):
    with open(output_file, 'w') as file:
        for domain in phishing_domains:
            for target_domain in target_domains:
                similarity = domain_similarity(domain, target_domain)
                if similarity > threshold and domain != target_domain:
                    output = f"Potential phishing domain: {domain} (similarity to {target_domain}: {similarity})"
                    print(output)
                    file.write(output + '\n')
def main():
    target_domains = ['turkcell.com', 'vodafone.com', 'garantibbva.com']
    file_path = r'C:\Users\azizd\Masaüstü\cert\url-list.txt' #girdi(usom)
    output_file = r'C:\Users\azizd\Masaüstü\cert\output.txt'  #çıktı
    phishing_domains = load_phishing_domains(file_path)
    detect_phishing_domains(target_domains, phishing_domains, output_file)

if __name__ == "__main__":
    main()
