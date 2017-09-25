from django.core.paginator import Page, Paginator


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
