from rest_framework import serializers
from .models import Team, Person, Shop, Stanowisko, Osoba, MONTHS, GENDER, SHIRT_SIZES

class TeamSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    kraj = serializers.CharField(required=True)

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance
class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ['id']

class PersonSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    shirt_size = serializers.ChoiceField(choices=SHIRT_SIZES, required=True, default=SHIRT_SIZES[0][0])
    miesiac_dodania = serializers.ChoiceField(choices=MONTHS, required=True, default=MONTHS[0][0])

    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.team = validated_data.get('team', instance.team)
        instance.save()
        return instance

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ['id']

class ShopSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    dodana = serializers.DateField(read_only=True)
    pracownicy = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.dodana = validated_data.get('dodana', instance.dodana)
        instance.pracownicy = validated_data.get('pracownicy', instance.pracownicy)
        instance.save()
        return instance

class ShopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        read_only_fields = ['id']

class StanowiskoSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    opis = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Stanowisko.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance

class StanowiskoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = '__all__'
        read_only_fields = ['id']

class OsobaSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    plec = serializers.ChoiceField(choices=GENDER, required=True, default=GENDER[0][0])
    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())
    data_dodania = serializers.DateField(required=True)

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.save()
        return instance

class OsobaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = '__all__'
        read_only_fields = ['id']
