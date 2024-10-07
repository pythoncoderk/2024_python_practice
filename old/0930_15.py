def show_name():
    name = "kirishima"

    def give_an_honorific():
        nonlocal name
        name += "san"

    print(name)
    give_an_honorific()
    print(name)


show_name()
