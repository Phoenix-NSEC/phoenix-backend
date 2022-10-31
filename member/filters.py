import django_filters
from member.models import Member


class MemberFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains", label="Name"
    )
    email = django_filters.CharFilter(
        field_name="email", lookup_expr="icontains", label="Email"
    )
    verified = django_filters.BooleanFilter(
        field_name="is_verified", lookup_expr="exact", label="Verified"
    )

    class Meta:
        model = Member
        fields = ["name", "email", "is_verified"]
