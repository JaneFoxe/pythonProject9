from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import LinkValidator
from users.models import Payments


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field='slug')]


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ["name", "preview", "description", "lessons_count", "lessons"]


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    """Класс сериализатора для модели Subscription"""

    class Meta:
        model = Subscription
        fields = "__all__"
