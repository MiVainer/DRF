from rest_framework import generics
from .models import Skill
from .serializer import SkillSerializer

class SkillAPIView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
