import os

from django.core.management.base import BaseCommand
from magic import Magic

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
        mime = Magic(mime=True)
        filetypes = {
            'jpeg': 0,
            'png': 0,
            'other': 0
        }

        for idea in ideas:
            self.stdout.write(idea.idea_image.name)
            if idea.idea_image:
                filename, extension = os.path.splitext(idea.idea_image.name)
                if not extension:
                    filetype = mime.from_file(idea.idea_image.path)
                    fileext = filetype.split('/')[1]
                    try:
                        filetypes[fileext] += 1
                    except KeyError:
                        filetypes['other'] += 1
                    self.stdout.write(idea.idea_image.name
                                      + ' --> ' +
                                      idea.idea_image.name
                                      + '.' + fileext)
                    os.rename(idea.idea_image.path,
                              idea.idea_image.path
                              + '.' + fileext)
                    idea.idea_image.name = (idea.idea_image.name
                                            + '.' + fileext)
                    idea.save()

        self.stdout.write('jpeg: ' + str(filetypes['jpeg']))
        self.stdout.write('png: ' + str(filetypes['png']))
        self.stdout.write('other: ' + str(filetypes['other']))
