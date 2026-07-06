import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username="pizza", password="123")
    assert user.username == "pizza"
    assert user.check_password("123")
