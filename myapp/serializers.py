from rest_framework import serializers
from myapp.models import Employee
from rest_framework import serializers


class EmployeeModelSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

class NameSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=70)

# def multiples_of_1000(value):
#     print("validations by using validator")
#     if value % 1000 != 0:
#         raise serializers.ValidationError("Salary Should be multiples of 1000")

class EmployeeSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=45)
    esal=serializers.FloatField()
    passw=serializers.CharField(max_length=40)
    rpass=serializers.CharField(max_length=40)

    # def validate_esal(self,value):
    #     if value < 50000:
    #         raise serializers.ValidationError("Employee salary should be minimum 5000")
    #         return value
    # def validate(self,data):
    #     print("validations at object level")
    #     ename=data.get('ename')
    #     eno=data.get('eno')
    #     esal=data.get('esal')
    #     passw=data.get('passw')
    #     rpass=data.get('rpass')
    #     if ename.lower()=='kitty':
    #         if esal < 50000:
    #             raise serializers.ValidationError('Kitty salary should not be less than 50000')
    #     return data
    #     if passw != rpass:
    #         raise serializers.ValidationError("Passw and rpass must be same")
    #
    def create(self,validated_data):
        return Employee.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.passw=validated_data.get('passw',instance.passw)
        instance.rpass=validated_data.get('rpass',instance.rpass)
        instance.save()
        return instance
    #
    #
