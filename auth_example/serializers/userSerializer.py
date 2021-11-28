from auth_example.models.user    import User
from rest_framework              import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'password', 'name', 'email']

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        return {
            'id'      : user.id,
            'username': user.username,
            'name'    : user.name,
            'email'   : user.email,
        }