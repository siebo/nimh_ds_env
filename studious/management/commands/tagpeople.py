from django.core.management.base import BaseCommand
from studious.models import ProjectPaper
from studious.models import Person

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        vals = Person.objects.values('id','full_name')
        people = vals.distinct().order_by('id')
        
        for person in people:
        	Orgs.objects.filter(contact_pi_project_leader=person.fullname).update(pi_id=person.id)

        print ("import complete")

