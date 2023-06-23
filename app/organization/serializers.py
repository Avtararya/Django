from rest_framework import serializers

from core.models import MasterOrg


class MasterOrgSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterOrg
        fields = '__all__'
        read_only_fields = ['id']


    def create(self, validated_data):
        master_org = MasterOrg.objects.create(**validated_data)
        return master_org

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

