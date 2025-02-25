import json
from django.core.management.base import BaseCommand
from portfolio.models import PersonalInfo, Project, ContactInfo
from django.core.serializers.json import DjangoJSONEncoder

class Command(BaseCommand):
    help = 'Exports portfolio data to JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to save JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        
        try:
            data = {
                'personal_info': self.get_personal_info(),
                'projects': self.get_projects(),
                'contact_info': self.get_contact_info()
            }
            
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2, cls=DjangoJSONEncoder)
                
            self.stdout.write(self.style.SUCCESS(f'Successfully exported data to {file_path}'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error exporting data: {str(e)}'))

    def get_personal_info(self):
        personal_info = PersonalInfo.objects.first()
        if personal_info:
            return {
                'name': personal_info.name,
                'description': personal_info.description,
                'bio': personal_info.bio,
                'role': personal_info.role,
                'additional_info': personal_info.additional_info
            }
        return {}

    def get_projects(self):
        projects = Project.objects.all()
        return [{
            'title': project.title,
            'description': project.description,
            'link': project.link,
            'technologies': project.technologies,
            'is_featured': project.is_featured
        } for project in projects]

    def get_contact_info(self):
        contact_info = ContactInfo.objects.first()
        if contact_info:
            return {
                'email': contact_info.email,
                'social_media_links': contact_info.social_media_links,
                'cv_link': contact_info.cv_link,
                'additional_contacts': contact_info.additional_contacts
            }
        return {}
