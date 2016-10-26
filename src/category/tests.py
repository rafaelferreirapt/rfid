# coding=utf-8
from django.test import TestCase
from halls.models import Hall, Category, SubHallConnection, SubHall, SubHallTag
from rest_framework.test import APIClient


class ObjectsTestCase(TestCase):
    def setUp(self):
        """
        Assumimos entao que:
        O Hall 1 tem os seguintes sub-halls:
        - 1 (Início)
            tags:
            - 1
        - 2
            tags:
            - 2
        - 3
            tags:
            - 3
        - 4
            tags:
            - 4
        O Hall 2 tem os seguintes sub-halls:
        - 5
            tags:
            - 5
        - 6
            tags:
            - 7
        - 7
            tags:
            - 7
        - 8
            tags:
            - 8
        O Hall 3 tem os seguintes sub-halls:
        - 9
            tags:
            - 9
        - 10
            tags:
            - 10
        - 11
            tags:
            - 11
        - 12
            tags:
            - 12
        O Hall 4 tem os seguintes sub-halls:
        - 13
            tags:
            - 13
        O Hall 5 tem os seguintes sub-halls:
        - 14
            tags:
            - 14
        O Hall 6 tem os seguintes sub-halls:
        - 15
            tags:
            - 15
        O Hall 7 tem os seguintes sub-halls:
        - 16
            tags:
            - 16
        O Hall 8 tem os seguintes sub-halls:
        - 17
            tags:
            - 17
        O Hall 9 tem os seguintes sub-halls:
        - 18
            tags:
            - 18
        O Hall 10 tem os seguintes sub-halls:
        - 19
            tags:
            - 19
        O Hall 11 tem os seguintes sub-halls:
        - 20
            tags:
            - 20
        """
        # hall 1
        self.hall1 = Hall.objects.create(name="1")
        self.sub_hall1 = SubHall.objects.create(name="1", parent_hall=self.hall1)
        self.tag1 = SubHallTag.objects.create(tag="1", parent_hall=self.sub_hall1)

        self.sub_hall2 = SubHall.objects.create(name="2", parent_hall=self.hall1)
        self.tag2 = SubHallTag.objects.create(tag="2", parent_hall=self.sub_hall2)

        self.sub_hall3 = SubHall.objects.create(name="3", parent_hall=self.hall1)
        self.tag3 = SubHallTag.objects.create(tag="3", parent_hall=self.sub_hall3)

        self.sub_hall4 = SubHall.objects.create(name="4", parent_hall=self.hall1)
        self.tag4 = SubHallTag.objects.create(tag="4", parent_hall=self.sub_hall4)

        # hall 2
        self.hall2 = Hall.objects.create(name="2")
        self.sub_hall5 = SubHall.objects.create(name="5", parent_hall=self.hall2)
        self.tag5 = SubHallTag.objects.create(tag="5", parent_hall=self.sub_hall5)

        self.sub_hall6 = SubHall.objects.create(name="6", parent_hall=self.hall2)
        self.tag6 = SubHallTag.objects.create(tag="6", parent_hall=self.sub_hall6)

        self.sub_hall7 = SubHall.objects.create(name="7", parent_hall=self.hall2)
        self.tag7 = SubHallTag.objects.create(tag="7", parent_hall=self.sub_hall7)

        self.sub_hall8 = SubHall.objects.create(name="8", parent_hall=self.hall2)
        self.tag8 = SubHallTag.objects.create(tag="8", parent_hall=self.sub_hall8)

        # hall 3
        self.hall3 = Hall.objects.create(name="3")
        self.sub_hall9 = SubHall.objects.create(name="9", parent_hall=self.hall3)
        self.tag9 = SubHallTag.objects.create(tag="9", parent_hall=self.sub_hall5)

        self.sub_hall10 = SubHall.objects.create(name="10", parent_hall=self.hall3)
        self.tag10 = SubHallTag.objects.create(tag="10", parent_hall=self.sub_hall6)

        self.sub_hall11 = SubHall.objects.create(name="11", parent_hall=self.hall3)
        self.tag11 = SubHallTag.objects.create(tag="11", parent_hall=self.sub_hall7)

        self.sub_hall12 = SubHall.objects.create(name="12", parent_hall=self.hall3)
        self.tag12 = SubHallTag.objects.create(tag="12", parent_hall=self.sub_hall8)

        # hall 4
        self.hall4 = Hall.objects.create(name="4")
        self.sub_hall13 = SubHall.objects.create(name="13", parent_hall=self.hall4)

        # hall 5
        self.hall5 = Hall.objects.create(name="5")
        self.sub_hall14 = SubHall.objects.create(name="14", parent_hall=self.hall5)

        # hall 6
        self.hall6 = Hall.objects.create(name="6")
        self.sub_hall15 = SubHall.objects.create(name="15", parent_hall=self.hall6)

        # hall 7
        self.hall7 = Hall.objects.create(name="7")
        self.sub_hall16 = SubHall.objects.create(name="16", parent_hall=self.hall7)

        # hall 8
        self.hall8 = Hall.objects.create(name="8")
        self.sub_hall17 = SubHall.objects.create(name="17", parent_hall=self.hall8)

        # hall 9
        self.hall9 = Hall.objects.create(name="9")
        self.sub_hall18 = SubHall.objects.create(name="18", parent_hall=self.hall9)

        # hall 10
        self.hall10 = Hall.objects.create(name="10")
        self.sub_hall19 = SubHall.objects.create(name="19", parent_hall=self.hall10)

        # hall 11
        self.hall11 = Hall.objects.create(name="11")
        self.sub_hall20 = SubHall.objects.create(name="20", parent_hall=self.hall11)

        # categories example
        self.category1 = Category.objects.create(name="Massas", description="Massas para cozinha.",
                                                 sub_hall=self.sub_hall20)
        self.category2 = Category.objects.create(name="Águas", description="Águas.", sub_hall=self.sub_hall1)
        self.category3 = Category.objects.create(name="Vinhos", description="Vinhos portugueses",
                                                 sub_hall=self.sub_hall6)
        self.category6 = Category.objects.create(name="Congelados", description="Gelados", sub_hall=self.sub_hall9)
        self.category7 = Category.objects.create(name="Carnes", description="Carnes congeladas",
                                                 sub_hall=self.sub_hall16)

        # connections
        # SUB HALL1
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall1,  connected=True, distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall2,  connected=True, distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall13, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall3,  connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall4,  connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall5,  connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall6,  connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall7,  connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall8,  connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall9,  connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall10, connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall11, connected=False, distance=5)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall12, connected=False, distance=6)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall14, connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall15, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall16, connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall17, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall18, connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall19, connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall1, hallB=self.sub_hall20, connected=False, distance=5)

        # SUB HALL2
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall1,  connected=True,  distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall3,  connected=True,  distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall14, connected=True,  distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall2,  connected=True,  distance=0)
        # not connected
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall4,  connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall5,  connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall6,  connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall7,  connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall8,  connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall9,  connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall10, connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall11, connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall12, connected=False, distance=5)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall13, connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall15, connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall16, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall17, connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall18, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall19, connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall2, hallB=self.sub_hall20, connected=False, distance=4)

        # SUB HALL3
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall2,  connected=True, distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall4,  connected=True, distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall15, connected=True, distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall3,  connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall1,  connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall5,  connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall6,  connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall7,  connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall8,  connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall9,  connected=False, distance=5)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall10, connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall11, connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall12, connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall13, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall14, connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall16, connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall17, connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall18, connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall19, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall3, hallB=self.sub_hall20, connected=False, distance=3)

        # SUB HALL 4
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall16, connected=True, distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall4,  connected=True, distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall3,  connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall1,  connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall2,  connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall5,  connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall6,  connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall7,  connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall8,  connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall9,  connected=False, distance=6)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall10, connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall11, connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall12, connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall13, connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall14, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall15, connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall17, connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall18, connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall19, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall4, hallB=self.sub_hall20, connected=False, distance=3)

        # SUB HALL 5
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall17, connected=True,  distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall13, connected=True,  distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall6,  connected=True,  distance=0)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall5,  connected=False, distance=0)
        # not connected
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall1,  connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall2,  connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall3,  connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall4,  connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall7,  connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall8,  connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall9,  connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall10, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall11, connected=False, distance=3)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall12, connected=False, distance=4)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall14, connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall15, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall16, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall18, connected=False, distance=1)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall19, connected=False, distance=2)
        SubHallConnection.objects.create(hallA=self.sub_hall5, hallB=self.sub_hall20, connected=False, distance=3)

        # SUB HALL 6

        # SUB HALL 7

        # SUB HALL 8

        # SUB HALL 9

        # SUB HALL 10

        # SUB HALL 11

        # SUB HALL 12

        # SUB HALL 13

        # SUB HALL 14

        # SUB HALL 15

        # SUB HALL 16

        # SUB HALL 17

        # SUB HALL 18

        # SUB HALL 19

        # SUB HALL 20

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

        url = "/api/v1/category/hall/" + self.tag1.tag + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        """
        url = "/api/v1/category/search/" + self.hall1.tag + "/" + str(self.category3.id) + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        print response
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["tag"], self.hall1.tag)
        self.assertEqual(response.data[1]["tag"], self.hall6.tag)
        self.assertEqual(response.data[2]["tag"], self.hall3.tag)
        """

