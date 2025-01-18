def var_to_dict():
    # Liste de tuples fournie
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]

    # Transformation en dictionnaire
    result = {}
    for name, year in d:
        if year in result:
            result[year] += f" {name}"
        else:
            result[year] = name

    # Affichage du dictionnaire
    for year, names in result.items():
        print(f"{year} : {names}")


if __name__ == "__main__":
    var_to_dict()
