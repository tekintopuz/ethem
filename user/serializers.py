from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission, Group
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from address.serializers import AddressSerializer
from attachment.serializers import AttachmentSerializer
from user.models import User, MembershipDeletionDemand


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        representation['permissions'] = PermissionSerializer(obj.permissions, many=True).data
        return representation


class UserSerializer(serializers.ModelSerializer):
    user_permissions = serializers.SerializerMethodField(read_only=True)
    groups = serializers.SerializerMethodField(read_only=True)
    addresses = serializers.SerializerMethodField()
    basket = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id",
                  "username",
                  "email",
                  "first_name",
                  "last_name",
                  "avatar",
                  "phone",
                  "role",
                  "is_email_verified",
                  "email_verified_at",
                  "is_mobile_verified",
                  "mobile_verified_at",
                  "date_joined",
                  "groups",
                  "user_permissions",
                  "kintshop_sms_allowed",
                  "kintshop_email_allowed",
                  "kintshop_phone_allowed",
                  "addresses",
                  "basket",
                  "is_active",
                  "is_deleted",
                  "deleted_at",
                  "last_login"
                  )
        read_only_fields = ('username', 'email', 'role', 'date_joined',)

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        representation['avatar'] = AttachmentSerializer(obj.avatar).data if obj.avatar else None
        return representation

    def get_user_permissions(self, obj):
        return PermissionSerializer(obj.user_permissions.all(), many=True).data

    def get_groups(self, obj):
        return GroupSerializer(obj.groups.all(), many=True).data

    def get_addresses(self, obj):
        return AddressSerializer(obj.address_set.filter(is_active=True, is_deleted=False), many=True).data

    def get_basket(self, obj):
        from basket.models import Basket
        from basket.serializers import BasketSerializer
        if not Basket.objects.filter(owner=obj).exists():
            Basket.objects.create(owner=obj)

        return BasketSerializer(obj.basket, context=self.context).data


class MyAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password", ),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            # To authenticate call simply returns None for is_active=False users.
            # (Assuming the default ModelBackend authentication backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['role'] = user.role
        return token

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        return data


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for register user
    """
    role = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = User
        fields = ['role', 'first_name', 'last_name', 'email', 'password']
        required = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.username = user.email
        user.save()
        return user

    def validate(self, data):
        if 'first_name' not in data:
            raise serializers.ValidationError(_("First Name is required"))
        elif 'last_name' not in data:
            raise serializers.ValidationError(_("Last Name is required"))
        elif 'email' not in data:
            raise serializers.ValidationError(_("Email is required"))
        elif 'password' not in data:
            raise serializers.ValidationError(_("Password is required"))

        return data

    def validate_email(self, email):
        """
        Check that the message post is about Django.
        """
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(_("This email is already registered!"))
        elif '@' not in email or email == '':
            raise serializers.ValidationError(_("wrong email"))
        return email

    def validate_first_name(self, first_name):
        """
        Check that the message post is about Django.
        """
        if first_name == '':
            raise serializers.ValidationError(_("FirstName cannot be empty"))
        return first_name

    def validate_password(self, password):
        """
        Check that the message post is about Django.
        """
        if len(password) < 6:
            raise serializers.ValidationError(_("Password must have at least 6 length."))
        return password


class ProfileSerializer(serializers.ModelSerializer):
    addresses = serializers.SerializerMethodField()
    avatar = AttachmentSerializer()

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "avatar", "phone", "role",
                  "is_email_verified", "email_verified_at", "is_mobile_verified", "mobile_verified_at",
                  "date_joined", "groups", "user_permissions", "addresses", "is_superuser", "is_staff")

    # def get_vendor(self, obj):
    #     if obj.vendor:
    def get_addresses(self, obj):
        return AddressSerializer(obj.address_set.filter(is_active=True, is_deleted=False), many=True).data

    def create(self, validated_data):
        return super(ProfileSerializer, self).create(validated_data)

    def get_user_permissions(self, obj):
        pass


class UserPublicSerializer(serializers.ModelSerializer):
    avatar = AttachmentSerializer()

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "avatar")


class MembershipDeletionDemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipDeletionDemand
        fields = ("id",
                  "created_by",
                  "reason",
                  "detail")

        extra_kwargs = {
            'reason': {'required': True, 'read_only': False},
            'detail': {'required': True, 'read_only': False},
        }

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        representation['user'] = UserSerializer(obj.created_by).data

        return representation

    def validate(self, data):
        if MembershipDeletionDemand.objects.filter(created_by=data["created_by"], is_active=True):
            raise serializers.ValidationError("There is already a demand belongs to this user")
        return data


class MembershipDeletionDemandSerializerForAdmin(serializers.ModelSerializer):
    class Meta:
        model = MembershipDeletionDemand
        fields = '__all__'

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        representation['user'] = UserSerializer(obj.created_by).data

        return representation
