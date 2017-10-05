from math import ceil

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
    def num_pages(self):
        """
        Return the total number of pages.
        Add delta elements to the count to get all pages.
        """
        if self.count == 0 and not self.allow_empty_first_page:
            return 0
        hits = max(1, self.count + self.delta - self.orphans)
        return ceil(hits / self.per_page)
