from rest_framework import serializers


class CovidDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    iso_code = serializers.CharField(max_length=10)
    continent = serializers.CharField(max_length=20)
    location = serializers.CharField(max_length=50)
    date = serializers.DateField()
    total_cases = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
    new_cases = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
    new_cases_smoothed = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
    total_deaths = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
    new_deaths = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
    new_deaths_smoothed = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
    total_cases_per_million = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
    new_cases_per_million = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
    new_cases_smoothed_per_million = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
    total_deaths_per_million = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
    new_deaths_per_million = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
    new_deaths_smoothed_per_million = serializers.DecimalField(max_digits=10, decimal_places=2,allow_null=True, required=False)
