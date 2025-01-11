def my_var():
    # Déclaration des variables
    integer_var = 42
    string_var_number = "42"
    string_var_text = "quarante-deux"
    float_var = 42.0
    boolean_var = True
    list_var = [42]
    dict_var = {42: 42}
    tuple_var = (42,)
    set_var = set()

    # Affichage des variables et de leurs types
    print(f"{integer_var} est de type {type(integer_var)}")
    print(f"{string_var_number} est de type {type(string_var_number)}")
    print(f"{string_var_text} est de type {type(string_var_text)}")
    print(f"{float_var} est de type {type(float_var)}")
    print(f"{boolean_var} est de type {type(boolean_var)}")
    print(f"{list_var} est de type {type(list_var)}")
    print(f"{dict_var} est de type {type(dict_var)}")
    print(f"{tuple_var} est de type {type(tuple_var)}")
    print(f"{set_var} est de type {type(set_var)}")

if __name__ == "__main__":
    my_var()
