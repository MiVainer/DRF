# -------------------------#
# ---Program by MiVainer---#
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Skills

class SkillSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Skills # Обращение к классу skill в models.py
        fields = "__all__"









#class SkillModel:
#    def __int__(self, skill, opisanie, full_text, cat):
#        self.skill = skill
#        self.opisanie = opisanie
#        self.full_text = full_text
#        self.cat = cat

#class SkillSerializer(serializers.Serializer):
#    skill = serializers.CharField(max_length=50)
#    opisanie = serializers.CharField()
#    full_text = serializers.CharField()
#    cat_id = serializers.CharField()

    # Добавление данных
#    def create(self, validated_data):
#        return Skill.objects.create(**validated_data)

    # Изменяем запись в базе данных
#    def update(self, instance, validated_data):
#        instance.skill = validated_data.get("skill", instance.skill)
#        instance.opisanie = validated_data.get("opisanie", instance.opisanie)
#        instance.full_text = validated_data.get("full_text", instance.full_text)
#        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        # сохраняем изменённые данные
#        instance.save()
#        return instance


#def encode():
    # преобразуем объекты в словарь, для передачи клинету
#   model = SkillModel('Git', 'Система контроля версий', 'Git позволяет совместно работать над программным продуктом, выстроить систему изменений, откатов кода', '4')
#   model_sr = SkillSerializer(model)
#   print(model_sr.data, type(model_sr.data), sep='\n')
    # преобразуем словарь (объект сериализации) в байтовую json строку, можно отдавать клиенту
#   json = JSONRenderer().render(model_sr.data)
#   print(json)

