from rest_framework import serializers
from .models import Person , Country
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('Username not fund')
    def validate(self, data):
        if User.objects.filter(email = data['email']).exists():
            raise serializers.ValidationError('email not fund')
        return data
    
    def create(self, validated_data):
        user= User.objects.create(username = validated_data['username'], email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
        print(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = '__all__'


class PeopleSerializer(serializers.ModelSerializer):
    # country = CountrySerializer()
    # country_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Person
        # exclude = ['name', 'age']
        fields = '__all__'
        depth = 1 #To find country name
    # def get_country_info(self, c_i):
    #     country_c_i = country_c_i.objects.get(id = c_i.country.id)
        # return {'country_name': '}
        
    #For validation
    def validate(self, data):
        
        if data ['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        

        spectial = "!@#$%^&*()_+"
        if any(c in spectial for c in data['name']):
            raise serializers.ValidationError('Name cannot contain Special char')
        
        return data
    
