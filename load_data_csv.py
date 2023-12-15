import pandas as pd
import os

datasets_name = ['e-tax-service', 'patent_tax', 'registration_tax', 'specific_tax',
                 'tax_on_property_rental', 'tax_on_property', 'tax_on_salary', 'tax_on_transportation', 'tax_on_unused_land', 'vat', 'withholding_tax']


def convert_to_csv():
    for i in datasets_name:
        data = pd.read_json(f"datasets/{i}.json")
        data.to_csv(f"{i}.csv", index=False)


def merge_csv():
    df_tax = pd.DataFrame()
    for i in datasets_name:
        individual_file = f"{i}.csv"
        df_specific_tax = pd.read_csv(individual_file)
        df_tax = pd.concat([df_tax, df_specific_tax], ignore_index=True)
        if os.path.exists(individual_file):
            os.remove(individual_file)
            print(f"Deleted '{individual_file}'")
    df_tax.to_csv("tax_data.csv", index=False)


def clean_data():
    df = pd.read_csv("tax_data.csv")
    df_cleaned = df[df.pattern != "[]"]
    df_cleaned.to_csv("tax_data.csv", index=False)


def manipulate_data():
    def manipulate(text):
        text = text.lower()
        if 'e-filing' in text:
            return text
        return text.replace('-', ' ')

    df = pd.read_csv("tax_data.csv")
    df.intent = df.intent.apply(manipulate)
    df.to_csv("tax_data.csv", index=False)


convert_to_csv()
merge_csv()
clean_data()
manipulate_data()
