from models import Branch, Master, Reg_Types, RegNo_Details
from rest_framework import serializers


class CompanyMasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Master
        fields = "__all__"


class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class RegTypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reg_Types
        fields = "__all__"


class RegNoDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegNo_Details
        fields = "__all__"
