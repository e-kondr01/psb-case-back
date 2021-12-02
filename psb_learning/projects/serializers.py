from rest_framework import serializers

from .models import Project, ProjectFile, ProjectLink, ProjectMember


class ProjectLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLink
        fields = [
            "id",
            "name",
            "link"
        ]


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = [
            "id",
            "name",
            "role",
            "photo"
        ]


class ProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = [
            "id",
            "file"
        ]


class ProjectSerializer(serializers.ModelSerializer):

    members = ProjectMemberSerializer(
        many=True, read_only=True
    )

    files = ProjectFileSerializer(
        many=True, read_only=True
    )

    links = ProjectLinkSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "goals",
            "project_type",
            "events",
            "stages",
            "results",
            "technologies",
            "links",
            "members",
            "more_info",
            "files"
        ]
