from rest_framework import serializers

from .models import Dna


class DnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dna
        fields = ["id", "animal_name", "species", "test_date", "milk_yield", "health_status", "created_at"]
