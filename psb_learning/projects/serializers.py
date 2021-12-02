from rest_framework import serializers

from .models import Project, ProjectFile, ProjectMember


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
            "organisation_links",
            "communication_links",
            "documentation_links",
            "design_links",
            "members",
            "files"
        ]
