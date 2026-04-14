import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # seen = set()
    # n = len(person)

    # for i in range(n):
    #     if person[i]['email'] in seen:

    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset=["email"], inplace=True)
