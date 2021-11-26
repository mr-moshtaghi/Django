from .models import Question, Answer
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
	answers = serializers.SerializerMethodField(method_name='answer')

	class Meta:
		model = Question
		fields = '__all__'

	def answers(self, obj):
		result = obj.answers.all()
		return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = '__all__'
