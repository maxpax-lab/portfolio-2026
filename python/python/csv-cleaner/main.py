import pandas as pd

def clean_csv(input_file, output_file):
    # Carica il file CSV
    df = pd.read_csv(input_file)

    # Rimuove duplicati
    df = df.drop_duplicates()

    # Rimuove spazi iniziali/finali nelle colonne stringa
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Rinomina colonne in formato standard (minuscolo + underscore)
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Salva il file pulito
    df.to_csv(output_file, index=False)
    print(f"File pulito salvato come: {output_file}")


if __name__ == "__main__":
    # Esempio di utilizzo
    clean_csv("input.csv", "output_clean.csv")

