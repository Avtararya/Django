from rest_framework import serializers

from .models import Branch, Master, Reg_Types, RegNo_Details


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class RegTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reg_Types
        fields = "__all__"

class RegNoDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegNo_Details
        fields = "__all__"
