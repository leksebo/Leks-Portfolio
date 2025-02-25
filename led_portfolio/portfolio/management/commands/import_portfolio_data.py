import json
from django.core.management.base import BaseCommand
from portfolio.models import PersonalInfo, Project, ContactInfo

class Command(BaseCommand):
    help = 'Imports portfolio data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                
                # Import PersonalInfo
                personal_data = data['personal_info']
                PersonalInfo.objects.update_or_create(
                    name=personal_data['name'],
                    defaults={
                        'description': personal_data['description'],
                        'bio': personal_data['bio'],
                        'role': personal_data['role'],
                        'additional_info': personal_data['additional_info']
                    }
                )
                
                # Import Projects
                Project.objects.all().delete()
                for project_data in data['projects']:
                    Project.objects.create(
                        title=project_data['title'],
                        description=project_data['description'],
                        link=project_data['link'],
                        technologies=project_data['technologies'],
                        is_featured=project_data['is_featured']
                    )
                
                # Import ContactInfo
                contact_data = data['contact_info']
                ContactInfo.objects.update_or_create(
                    email=contact_data['email'],
                    defaults={
                        'social_media_links': contact_data['social_media_links'],
                        'cv_link': contact_data['cv_link'],
                        'additional_contacts': contact_data['additional_contacts']
                    }
                )
                
                self.stdout.write(self.style.SUCCESS('Successfully imported portfolio data'))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing data: {str(e)}'))
