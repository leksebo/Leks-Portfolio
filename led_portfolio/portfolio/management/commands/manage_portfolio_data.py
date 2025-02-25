from django.core.management.base import BaseCommand
from portfolio.management.commands.import_portfolio_data import Command as ImportCommand
from portfolio.management.commands.export_portfolio_data import Command as ExportCommand

class Command(BaseCommand):
    help = 'Manage portfolio data import/export operations'

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(dest='command', required=True)
        
        # Import subcommand
        import_parser = subparsers.add_parser('import')
        import_parser.add_argument('file_path', type=str, help='Path to JSON file')
        
        # Export subcommand
        export_parser = subparsers.add_parser('export')
        export_parser.add_argument('file_path', type=str, help='Path to save JSON file')

    def handle(self, *args, **kwargs):
        command = kwargs['command']
        file_path = kwargs['file_path']
        
        if command == 'import':
            ImportCommand().handle(file_path=file_path)
        elif command == 'export':
            ExportCommand().handle(file_path=file_path)
        else:
            self.stdout.write(self.style.ERROR('Invalid command'))
