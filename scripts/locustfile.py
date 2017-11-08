from locust import HttpLocust, TaskSet, task
from pyquery import PyQuery
import random


class AeBrowser(TaskSet):
    def on_start(self):
        self.index()
        self.urls = []

    @task(20)
    def index(self):
        self.client.get("/")

    @task(10)
    def ideaspace(self, status="", ordering=""):
        r = self.client.get(
            "/ideas?ordering={ordering}&status={status}".format(
                status=status,
                ordering=ordering
            )
        )

        pq = PyQuery(r.content)
        link_elements = pq("a").filter(".idealist-image")
        self.urls = [
            a.attrib["href"] for a in link_elements
        ]

    @task(8)
    def idea_filter(self):
        status = random.choice([
            "winner", "proposal", "idea_sketch", "shortlist"
        ])
        ordering = random.choice([
            "newest", "comments", "support", "title"
        ])
        self.ideaspace(status=status, ordering=ordering)

    @task(5)
    def load_page(self):
        try:
            url = random.choice(self.urls)
            self.client.get(url)
        except IndexError:
            pass

    @task(5)
    def stories(self):
        r = self.client.get("/blog")
        pq = PyQuery(r.content)
        link_elements = pq("a").filter(".hover-child-img")
        self.urls = [
            a.attrib["href"] for a in link_elements
        ]

    @task(1)
    def about(self):
        self.client.get("/about")

    @task(1)
    def terms(self):
        self.client.get("/terms-use")

    @task(1)
    def login(self):
        self.client.get("/accounts/login")

    @task(1)
    def register(self):
        self.client.get("/accounts/signup")


class WebsiteUser(HttpLocust):
    # to call via
    #   $ locust -f locustfile.py --host <host>
    task_set = AeBrowser
