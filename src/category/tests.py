# coding=utf-8
from django.test import TestCase
from halls.models import Hall, CategoryHalls, Category
from rest_framework.test import APIClient


class ObjectsTestCase(TestCase):
    def setUp(self):
        self.hall1 = Hall.objects.create(tag="1A253")
        self.hall2 = Hall.objects.create(tag="1A254")
        self.hall3 = Hall.objects.create(tag="1A255")
        self.hall4 = Hall.objects.create(tag="1A256")

        self.category1 = Category.objects.create(name="Massas", description="Massas para cozinha.")
        self.category2 = Category.objects.create(name="Águas", description="Águas.")
        self.category3 = Category.objects.create(name="Vinhos", description="Vinhos portugueses")
        self.category4 = Category.objects.create(name="Congelados", description="Gelados")

        self.categoryHall1 = CategoryHalls.objects.create(category=self.category1,
                                                          hall=self.hall1)
        self.categoryHall2 = CategoryHalls.objects.create(category=self.category2,
                                                          hall=self.hall2)
        self.categoryHall3 = CategoryHalls.objects.create(category=self.category3,
                                                          hall=self.hall3)
        self.categoryHall4 = CategoryHalls.objects.create(category=self.category4,
                                                          hall=self.hall4)

    def test_products(self):
        client = APIClient()

        url = "/api/v1/category/details/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

        url = "/api/v1/category/details/" + str(self.category1.id) + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.category1.id))

        url = "/api/v1/category/hall/" + self.hall1.tag + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
