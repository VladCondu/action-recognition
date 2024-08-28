class Paginator:
    def __init__(self, items, items_per_page):
        self.items = items
        self.items_per_page = items_per_page
        self.current_page = 0

    def next_page(self):
        if self.current_page < self.total_pages() - 1:
            self.current_page += 1

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1

    def total_pages(self):
        return (len(self.items) + self.items_per_page - 1) // self.items_per_page

    def get_current_page_items(self):
        start = self.current_page * self.items_per_page
        end = start + self.items_per_page
        return self.items[start:end]
