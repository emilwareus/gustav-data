from tqdm import tqdm
import pandas as pd
import json
import os
import numpy as np

_columns_to_drop = ['access', 'access_to_own_car', 'driving_license', 'driving_license_required', 'experience_required', 'logo_url', 'removed', 'removed_date', 'source_type', 'timestamp', 'webpage_url', 'application_details_email', 'application_details_information', 'application_details_other', 'application_details_reference', 'application_details_via_af', 'description_needs', 'description_requirements', 'description_text_formatted', 'duration_concept_id', 'duration_legacy_ams_taxonomy_id', 'employer_email', 'employer_organization_number', 'employer_phone_number', 'employer_url', 'employment_type_concept_id', 'employment_type_legacy_ams_taxonomy_id', 'must_have_languages', 'must_have_skills', 'must_have_work_experiences', 'nice_to_have_languages', 'nice_to_have_skills',
                    'nice_to_have_work_experiences', 'occupation_concept_id', 'occupation_label', 'occupation_field_concept_id', 'occupation_field_label', 'occupation_field_legacy_ams_taxonomy_id', 'occupation_group_concept_id', 'occupation_group_label', 'occupation_group_legacy_ams_taxonomy_id', 'salary_type_concept_id', 'salary_type_legacy_ams_taxonomy_id', 'scope_of_work_max', 'scope_of_work_min', 'working_hours_type_concept_id', 'working_hours_type_legacy_ams_taxonomy_id', 'workplace_address_coordinates', 'workplace_address_country_code', 'workplace_address_country_concept_id', 'workplace_address_municipality', 'workplace_address_municipality_code', 'workplace_address_municipality_concept_id', 'workplace_address_region', 'workplace_address_region_code', 'workplace_address_region_concept_id']


def open_file(filename):
    with open(filename) as f:
        output = json.loads(f.read())

    return output


def expand_dict(df, col_name):

    if type(df[col_name].values[0]) == dict:
        col_df = pd.DataFrame(df[col_name].values.tolist())
        names = {name: col_name + "_" + name for name in list(col_df)}
        col_df = col_df.rename(names, axis=1)
        return col_df
    else:
        return None


def expand_cols(df_r):
    df = df_r.copy()
    old_cols = []
    while old_cols != list(df):
        old_cols = list(df)
        for col_name in list(df):
            col_df = expand_dict(df, col_name)
            if col_df is not None:
                df[list(col_df)] = col_df
                df = df.drop(col_name, axis=1)
    return df


def preprocess_file(filename):
    # Read as dict
    af_y = open_file(filename)

    # To dataframe
    af_y_df = pd.DataFrame(af_y)

    # Expand nested dicts
    df = expand_cols(af_y_df)

    # Drop cols with a lot of Nones
    df = df.drop(_columns_to_drop, axis=1)  # more than 4/5 are None

    # Convert to proper timestamps
    df['application_deadline'] = pd.to_datetime(
        df['application_deadline'], errors='coerce')
    df['last_publication_date'] = pd.to_datetime(
        df['last_publication_date'], errors='coerce')
    df['publication_date'] = pd.to_datetime(
        df['publication_date'], errors='coerce')

    return df


def append_iter_csv(df, name):
    chunks = int(df.shape[0] / 1000)
    for chunk in tqdm(np.array_split(df, chunks)):
        chunk.to_csv(name, mode='a', header=False,
                     encoding='ISO-8859-1', errors='replace')


def preprocess_all_files():
    files = os.listdir("downloads")

    first = True
    for file in files:
        print(f"parsing {file}")
        df = preprocess_file("./downloads/" + file)

        if first:
            df.head(0).to_csv('af_prepro.csv', encoding='ISO-8859-1')
            first = False

        append_iter_csv(df, 'af_prepro.csv')


if __name__ == '__main__':
    preprocess_all_files()
