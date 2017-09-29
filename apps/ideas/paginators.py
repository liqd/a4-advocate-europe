from django.core.paginator import Page, Paginator
from django.utils.functional import cached_property


class DeltaFirstPagePaginator(Paginator):
    delta = 1

    def page(self, number):
        """
        Returns first page with `per_page` - `delta` entries.
        """
        number = self.validate_number(number)
        if number == 1:
            bottom = 0
            top = self.per_page - self.delta
        else:
            bottom = (number - 1) * self.per_page - self.delta
            top = bottom + self.per_page

        if top + self.orphans >= self.count:
            top = self.count

        return Page(self.object_list[bottom:top], number, self)

    @cached_property
    def count(self):
        """
        Return the total number of objects + 'delta' entries,
        across all pages.
        """
        try:
            return (self.object_list.count() + self.delta)
        except (AttributeError, TypeError):
            # AttributeError if object_list has no count() method.
            # TypeError if object_list.count() requires arguments
            # (i.e. is of type list).
            return (len(self.object_list) + self.delta)
