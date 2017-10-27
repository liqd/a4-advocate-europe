import os

from django.core.management.base import BaseCommand

from apps.ideas.models import Idea


class Command(BaseCommand):

    def handle(self, *args, **options):

        # for file in os.listdir(path):
            # filename, extension = os.path.splitext(file)
            # if not extension:
                # self.stdout.write(path+file+' --> '+path+file+'.jpg')
                # os.rename(path+file, path+file+'.jpg')

        # os.rename(model.direct_file.path, new_path)
        # model.direct_file.name = new_name
        # model.save()

        ideas = Idea.objects.all()
        for idea in ideas:
            self.stdout.write(idea.idea_image.name)
            if idea.idea_image:
                filename, extension = os.path.splitext(idea.idea_image.name)
                if not extension:
                    self.stdout.write(idea.idea_image.name
                                      + ' --> ' +
                                      idea.idea_image.name + '.jpg')
                    os.rename(idea.idea_image.path,
                              idea.idea_image.path + '.jpg')
                    # add image magic!
                    # and rename files in model!
