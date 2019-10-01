class Personne:
    def __init__(self, age, name, last_name, gender):
        self.__age = age
        self.__name = name
        self.__last_name = last_name
        self.__gender = gender

    def __str__(self):
        return "Person is {} {}, age {}, gender {}".format(self.__name, self.__last_name, self.__age, self.__gender)
