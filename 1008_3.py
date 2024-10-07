def introduce(**people):
    for name, greeting in people.items():
        print("私は" + name + "です。" + greeting)
    print(people)

introduce(hero="初めまして", villager="こんにちは", soldier="よろしくお願いします")
