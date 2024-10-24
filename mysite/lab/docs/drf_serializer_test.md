# DRF Serializer Test

## OsobaSerializer Test

```python
from lab.models import Osoba, Stanowisko
from lab.serializers import OsobaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# 1. Create a new instance of Osoba
stanowisko = Stanowisko.objects.create(nazwa='Developer', opis='Software Developer')
osoba = Osoba(imie='Adam', nazwisko='Nowak', plec=1, stanowisko=stanowisko)

# Save the instance to the database
osoba.save()

# 2. Initialize serializer
serializer = OsobaSerializer(osoba)
serializer.data
# Expected output - Python dictionary
# {'id': 1, 'imie': 'Adam', 'nazwisko': 'Nowak', 'plec': 1, 'stanowisko': 1, 'data_dodania': '2024-10-23'}

# 3. Serialize the data to JSON
content = JSONRenderer().render(serializer.data)
content

# Expected output
# b'{"id":1,"imie":"Adam","nazwisko":"Nowak","plec":1,"stanowisko":1,"data_dodania":"2024-10-23"}'

# 4. Deserialize the JSON content
stream = io.BytesIO(content)
data = JSONParser().parse(stream)

# Create serializer with deserialized data
deserializer = OsobaSerializer(data=data)

# 5. Check if the deserialized data is valid
deserializer.is_valid()
# Expected output: True

# 6. Check the deserialized fields
deserializer.validated_data
# Expected output
# OrderedDict([('imie', 'Adam'), ('nazwisko', 'Nowak'), ('plec', 1), ('stanowisko', 1), ('data_dodania', '2024-10-23')])

# 7. Save the deserialized data
deserializer.save()

# Check serialized data after saving
deserializer.data
