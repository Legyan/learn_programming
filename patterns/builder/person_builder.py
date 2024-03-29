class Person:
    def __init__(self):
        # address
        self.street_address = None
        self.post_code = None
        self.city = None
        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return (f'Address {self.street_address}, '
                f'{self.post_code}, {self.city}\n'
                f'Employment ad {self.company_name} '
                f'as {self.position} earning {self.annual_income}')


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.post_code = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == '__main__':
    pb = PersonBuilder()
    pb.lives.at('Gagarina 2').with_postcode('222222').in_city('Moscow')\
        .works.at('Google').as_a('developer').earning('200 000 $')
    print(pb)
    person = pb.build()
    print(person)
