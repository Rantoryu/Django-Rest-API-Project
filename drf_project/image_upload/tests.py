from django.test import TestCase
from unittest.mock import Mock
from image_upload import validators
from django.core.exceptions import ValidationError
import pytest

# Create your tests here.


class TestValidateMinimumSize:
    def test_does_not_raise_when_image_meets_requirements(self):
        mock_image = Mock(width=10, height=10)
        validator = validators.validate_maximum_size(width=10, height=10)

        validator(image=mock_image)

    def test_raises_if_image_is_too_big(self):
        mock_image = Mock(width=11, height=11)
        validator = validators.validate_maximum_size(width=10, height=10)

        with pytest.raises(ValidationError):
            validator(image=mock_image)
