from rest_framework import serializers

from .models import Cat, Owner, Achievement


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = ('id', 'name')


class CatSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True,
                                         required=False)

    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year',
                  'owner', 'achievements')
        
    def create(self, validated_data):
        # Если в исходном запросе не было поля achievements
        if 'achievements' not in self.initial_data:
            # То создаём запись о котике без его достижений
            cat = Cat.objects.create(**validated_data)
            return cat
        # Уберём список достижений из словаря validated_data
        # и сохраним его
        achievments = validated_data.pop('achievements')
        # Создадим нового котика пока без достижений, данных нам достаточно
        cat = Cat.objects.create(**validated_data)
        # Для каждого достижения из списка достижений
        for achievement in achievments:
            # Создадим новую запись или получим
            # существующий экземпляр из БД
            current_achievments, status = Achievement.objects.get_or_create(
                **achievement)
            # поместим ссылку на каждое достижение во вспомогательную таблицу
            # не забываем указать к какому коту оно относится
            Achievement.objects.create(achievement=current_achievments,
                                      cat=cat)
        return cat



class OwnerSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True,
                                          read_only=True)

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'cats')

