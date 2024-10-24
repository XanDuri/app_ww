from .models import Person
from lab.serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# 1. stworzenie nowej instancji klasy Person (opcjonalne, mamy panel admin do tego również)
person = Person(name='Adam', miesiac_dodania=1)
# utrwalenie w bazie danych
person.save()

# 2. inicjalizacja serializera
serializer = PersonSerializer(person)
serializer.data
# output - natywny typ danych Pythona (dictionary)
{'id': 16, 'name': 'Adam', 'shirt_size': ('S', 'Small'), 'miesiac_dodania': 1, 'team': None}

# warto również zwrócić uwagę na wartość zmiennej shirt_size, która przyjęła wartość jako krotkę (która została zamieniona na typ str), gdyż w modelu został domyślny wybór określony jako SHIRT_SIZE[0] co jest pierwszą krotką dla tej kolekcji o wartości ('S', 'Small')
# zamiana na SHIRT_SIZE[0][0] wskazałaby wartość 'S' i powinna również działać poprawnie dla modelu Person
# output po zmianach w modelu
# {'id': 19, 'name': 'Genowefa', 'shirt_size': 'S', 'miesiac_dodania': 1, 'team': None}

# 3. serializacja danych do formatu JSON
content = JSONRenderer().render(serializer.data)
content

# output
b'{"id":16,"name":"Adam","shirt_size":"S","miesiac_dodania":1,"team":null}'

# w takiej formie możemy przesłać obiekt (lub cały graf obiektów) przez sieć i po "drugiej stronie" dokonać deserializacji odtwarzając graf i stan obiektów

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

# tworzymy obiekt dedykowanego serializera i przekazujemy sparsowane dane
deserializer = PersonSerializer(data=data)
# sprawdzamy, czy dane przechodzą walidację (aktualnie tylko domyślna walidacja, dedykowana zostanie przedstawiona na kolejnych zajęciach)
deserializer.is_valid()
# output
# False

# to oznacza pojawienie się błędu walidacji
deserializer.errors
# output
# {'team': [ErrorDetail(string='Pole nie może mieć wartości null.', code='null')]}

# w samym modelu określone są dwa atrybuty null=True, blank=True, ale jak widać serializer nie bierze tego pod uwagę
# musimy w klasie PersonSerializer zmodyfikować wartość dla pola team
# dodając atrybut allow_null=True i uruchomić całe testowanie raz jeszcze

# aby upewnić się w jaki sposób wyglądają pola wczytanego serializera/deserializera, możemy wywołać zmienną deserializer.fields, aby wyświetlić te dane
deserializer.fields

# lub
repr(deserializer)

# po powyższych zmianach walidacja powinna już się powieść
# możemy sprawdzić jak wyglądają dane obiektów po deserializacji i walidacji
deserializer.validated_data
# output
# OrderedDict([('name', 'Adam'), ('shirt_size', 'S'), ('miesiac_dodania', 1), ('team', None)])

# oraz utrwalamy dane
deserializer.save()
# sprawdzamy m.in. przyznane id
deserializer.data