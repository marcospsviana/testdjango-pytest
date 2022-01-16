import pytest
from model_bakery import baker
from testpytest.user.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user()
    assert User.objects.count() == 1


@pytest.fixture
def user(db):
    return baker.make(User)


def test_user(user):
    assert user.pk == 1
