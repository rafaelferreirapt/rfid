# coding=utf-8
from django.test import TestCase
from halls.models import Hall, CategoryHalls, Category, HallConnection
from rest_framework.test import APIClient


class ObjectsTestCase(TestCase):
    def setUp(self):
        self.hall1 = Hall.objects.create(tag="1A253")  # top
        self.hall2 = Hall.objects.create(tag="1A254")  # middle
        self.hall3 = Hall.objects.create(tag="1A255")  # bottom
        self.hall6 = Hall.objects.create(tag="1A256")  # left
        self.hall7 = Hall.objects.create(tag="1A257")  # right

        self.category1 = Category.objects.create(name="Massas", description="Massas para cozinha.")
        self.category2 = Category.objects.create(name="Águas", description="Águas.")
        self.category3 = Category.objects.create(name="Vinhos", description="Vinhos portugueses")
        self.category6 = Category.objects.create(name="Congelados", description="Gelados")
        self.category7 = Category.objects.create(name="Carnes", description="Carnes congeladas")

        """
        CATEGORY HALLS
        """
        CategoryHalls.objects.create(category=self.category1,
                                     hall=self.hall1)
        CategoryHalls.objects.create(category=self.category2,
                                     hall=self.hall2)
        CategoryHalls.objects.create(category=self.category3,
                                     hall=self.hall3)
        CategoryHalls.objects.create(category=self.category6,
                                     hall=self.hall6)
        CategoryHalls.objects.create(category=self.category7,
                                     hall=self.hall7)

        """
        CONNECTIONS
        """
        HallConnection.objects.create(hallA=self.hall1, hallB=self.hall1, connected=True,  distance=0)
        HallConnection.objects.create(hallA=self.hall1, hallB=self.hall6, connected=True,  distance=0)
        HallConnection.objects.create(hallA=self.hall1, hallB=self.hall7, connected=True,  distance=0)
        HallConnection.objects.create(hallA=self.hall1, hallB=self.hall2, connected=False, distance=1)
        HallConnection.objects.create(hallA=self.hall1, hallB=self.hall3, connected=False, distance=1)

        HallConnection.objects.create(hallA=self.hall6, hallB=self.hall6, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall6, hallB=self.hall1, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall6, hallB=self.hall2, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall6, hallB=self.hall3, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall6, hallB=self.hall7, connected=False, distance=1)

        HallConnection.objects.create(hallA=self.hall7, hallB=self.hall7, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall7, hallB=self.hall1, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall7, hallB=self.hall2, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall7, hallB=self.hall3, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall7, hallB=self.hall6, connected=False, distance=1)

        HallConnection.objects.create(hallA=self.hall2, hallB=self.hall2, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall2, hallB=self.hall6, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall2, hallB=self.hall7, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall2, hallB=self.hall1, connected=False, distance=1)
        HallConnection.objects.create(hallA=self.hall2, hallB=self.hall3, connected=False, distance=1)

        HallConnection.objects.create(hallA=self.hall3, hallB=self.hall3, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall3, hallB=self.hall6, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall3, hallB=self.hall7, connected=True, distance=0)
        HallConnection.objects.create(hallA=self.hall3, hallB=self.hall1, connected=False, distance=1)
        HallConnection.objects.create(hallA=self.hall3, hallB=self.hall2, connected=False, distance=1)

    def test_products(self):
        client = APIClient()

        url = "/api/v1/category/details/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)

        url = "/api/v1/category/details/" + str(self.category1.id) + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.category1.id))

        url = "/api/v1/category/hall/" + self.hall1.tag + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        url = "/api/v1/category/search/" + self.hall1.tag + "/" + str(self.category3.id) + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0], self.hall1.tag)
        self.assertEqual(response.data[1], self.hall6.tag)
        self.assertEqual(response.data[2], self.hall3.tag)

