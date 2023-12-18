import pandas as pd
import os

datasets_name = ['e-tax-service', 'patent_tax', 'registration_tax', 'specific_tax',
                 'tax_on_property_rental', 'tax_on_property', 'tax_on_salary', 'tax_on_transportation', 'tax_on_unused_land', 'vat', 'withholding_tax']


def convert_to_csv():
    for i in datasets_name:
        data = pd.read_json(f"datasets/{i}.json")
        data.to_csv(f"{i}.csv", index=False)
    print("Convert Data: Completed")


def merge_csv():
    df_tax = pd.DataFrame()
    for i in datasets_name:
        individual_tax_file = f"{i}.csv"
        df_specific_tax = pd.read_csv(individual_tax_file)
        df_tax = pd.concat([df_tax, df_specific_tax], ignore_index=True)
        if os.path.exists(individual_tax_file):
            os.remove(individual_tax_file)
    df_tax.to_csv("tax_data.csv", index=False)
    print("Merged Data: Completed")


def clean_data():
    df = pd.read_csv("tax_data.csv")
    df_cleaned = df[df.pattern != "[]"]
    df_cleaned.to_csv("tax_data.csv", index=False)
    print("Clean Data: Completed")


def filter_data():
    def manipulate(text):
        text = text.lower()
        if 'e-filing' in text:
            return text
        return text.replace('-', ' ')
    df = pd.read_csv("tax_data.csv")
    df.intent = df.intent.apply(manipulate)
    df.to_csv("tax_data.csv", index=False)
    print("Filter Data: Completed")


def add_tax_payer_data():
    df = pd.read_json(f"datasets/taxpayer.json")
    df.drop(columns='tagKH', inplace=True)
    df_tax = pd.read_csv("tax_data.csv")
    df_tax = pd.concat([df_tax, df], ignore_index=True)
    df_tax.to_csv("tax_data.csv", index=False)
    print("Add Tax Payer Data: Completed")


def manipulate_data():
    df = pd.read_csv("tax_data.csv")
    df.rename(columns={"responses": "response"}, inplace=True)
    df['response'] = df['response'].str.replace(
        r'\[|\]|\'+|\"+', '', regex=True)
    df.to_csv("tax_data.csv", index=False)
    print("Manipulated Data: Completed")


def mining_data():
    df = pd.read_csv("tax_data.csv")
    ls = []
    for _, row in df.iterrows():
        patterns = row['pattern'].split(', ')
        for i, pattern in enumerate(patterns):
            new_row = {
                'intent': row['intent'],
                'pattern': "".join([c for c in pattern if c not in ["[", "]", "'", "\\", "u", "2", "0", "b"]]),
                'response': row['response']
            }
            ls.append(new_row)

    df_tax = pd.DataFrame(ls, columns=[
        'intent', 'pattern', 'response'])
    df_tax.to_csv("tax_data.csv", index=False)
    print("Mining Data: Completed")


convert_to_csv()
merge_csv()
clean_data()
filter_data()
add_tax_payer_data()
manipulate_data()
mining_data()
