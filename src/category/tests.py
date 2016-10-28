# coding=utf-8
from django.test import TestCase
from halls.models import Hall, Category, SubHallConnection, SubHall, SubHallTag
from rest_framework.test import APIClient


class ObjectsTestCase(TestCase):
    def setUp(self):
        # hall 1
        self.hall1 = Hall.objects.create(name="1")
        self.sub_hall1 = SubHall.objects.create(name="1", parent_hall=self.hall1)
        self.tag1 = SubHallTag.objects.create(tag="1", parent_hall=self.sub_hall1)

        # hall 2
        self.hall2 = Hall.objects.create(name="2")
        self.sub_hall2 = SubHall.objects.create(name="2", parent_hall=self.hall2)
        self.tag2 = SubHallTag.objects.create(tag="2", parent_hall=self.sub_hall2)

        # hall 3
        self.hall3 = Hall.objects.create(name="3")
        self.sub_hall3 = SubHall.objects.create(name="3", parent_hall=self.hall3)
        self.tag3 = SubHallTag.objects.create(tag="3", parent_hall=self.sub_hall3)

        # hall 4
        self.hall4 = Hall.objects.create(name="4")
        self.sub_hall4 = SubHall.objects.create(name="4", parent_hall=self.hall4)
        self.tag4 = SubHallTag.objects.create(tag="4", parent_hall=self.sub_hall4)

        # hall 5
        self.hall5 = Hall.objects.create(name="5")
        self.sub_hall5 = SubHall.objects.create(name="5", parent_hall=self.hall5)
        self.tag5 = SubHallTag.objects.create(tag="5", parent_hall=self.sub_hall5)

        # hall 6
        self.hall6 = Hall.objects.create(name="6")
        self.sub_hall6 = SubHall.objects.create(name="6", parent_hall=self.hall6)
        self.tag6 = SubHallTag.objects.create(tag="6", parent_hall=self.sub_hall6)

        # hall 7
        self.hall7 = Hall.objects.create(name="7")
        self.sub_hall7 = SubHall.objects.create(name="7", parent_hall=self.hall7)
        self.tag7 = SubHallTag.objects.create(tag="7", parent_hall=self.sub_hall7)

        # hall 8
        self.hall8 = Hall.objects.create(name="8")
        self.sub_hall8 = SubHall.objects.create(name="8", parent_hall=self.hall8)
        self.tag8 = SubHallTag.objects.create(tag="8", parent_hall=self.sub_hall8)

        # hall 9
        self.hall9 = Hall.objects.create(name="9")
        self.sub_hall9 = SubHall.objects.create(name="9", parent_hall=self.hall9)
        self.tag9 = SubHallTag.objects.create(tag="9", parent_hall=self.sub_hall9)

        # hall 10
        self.hall10 = Hall.objects.create(name="10")
        self.sub_hall10 = SubHall.objects.create(name="10", parent_hall=self.hall10)
        self.tag10 = SubHallTag.objects.create(tag="10", parent_hall=self.sub_hall10)

        # hall 11
        self.hall11 = Hall.objects.create(name="11")
        self.sub_hall11 = SubHall.objects.create(name="11", parent_hall=self.hall11)
        self.tag11 = SubHallTag.objects.create(tag="11", parent_hall=self.sub_hall11)

        # hall 12
        self.hall12 = Hall.objects.create(name="12")
        self.sub_hall12 = SubHall.objects.create(name="12", parent_hall=self.hall12)
        self.tag12 = SubHallTag.objects.create(tag="12", parent_hall=self.sub_hall12)

        # hall 13
        self.hall13 = Hall.objects.create(name="13")
        self.sub_hall13 = SubHall.objects.create(name="13", parent_hall=self.hall13)
        self.tag13 = SubHallTag.objects.create(tag="13", parent_hall=self.sub_hall13)

        # hall 14
        self.hall14 = Hall.objects.create(name="14")
        self.sub_hall14 = SubHall.objects.create(name="14", parent_hall=self.hall14)
        self.tag14 = SubHallTag.objects.create(tag="14", parent_hall=self.sub_hall14)

        # hall 15
        self.hall15 = Hall.objects.create(name="15")
        self.sub_hall15 = SubHall.objects.create(name="15", parent_hall=self.hall15)
        self.tag15 = SubHallTag.objects.create(tag="15", parent_hall=self.sub_hall15)

        # hall 16
        self.hall16 = Hall.objects.create(name="16")
        self.sub_hall16 = SubHall.objects.create(name="16", parent_hall=self.hall16)
        self.tag16 = SubHallTag.objects.create(tag="16", parent_hall=self.sub_hall16)

        # hall 17
        self.hall17 = Hall.objects.create(name="17")
        self.sub_hall17 = SubHall.objects.create(name="17", parent_hall=self.hall17)
        self.tag17 = SubHallTag.objects.create(tag="17", parent_hall=self.sub_hall17)

        # hall 18
        self.hall18 = Hall.objects.create(name="18")
        self.sub_hall18 = SubHall.objects.create(name="18", parent_hall=self.hall18)
        self.tag18 = SubHallTag.objects.create(tag="18", parent_hall=self.sub_hall18)

        # hall 19
        self.hall19 = Hall.objects.create(name="19")
        self.sub_hall19 = SubHall.objects.create(name="19", parent_hall=self.hall19)
        self.tag19 = SubHallTag.objects.create(tag="19", parent_hall=self.sub_hall19)

        # hall 20
        self.hall20 = Hall.objects.create(name="20")
        self.sub_hall20 = SubHall.objects.create(name="20", parent_hall=self.hall20)
        self.tag20 = SubHallTag.objects.create(tag="20", parent_hall=self.sub_hall20)

        # categories example
        self.category1 = Category.objects.create(name="Arroz",
                                                 description="Arroz",
                                                 sub_hall=self.sub_hall1)

        self.category2 = Category.objects.create(name="Massas",
                                                 description="Massas",
                                                 sub_hall=self.sub_hall2)

        self.category3 = Category.objects.create(name="Especiarias",
                                                 description="Especiarias",
                                                 sub_hall=self.sub_hall3)

        self.category4 = Category.objects.create(name="Concentrados",
                                                 description="Concentrados",
                                                 sub_hall=self.sub_hall4)

        self.category5 = Category.objects.create(name="Pão",
                                                 description="Pão",
                                                 sub_hall=self.sub_hall5)

        self.category6 = Category.objects.create(name="Peixe",
                                                 description="Peixe",
                                                 sub_hall=self.sub_hall6)

        self.category7 = Category.objects.create(name="Carne",
                                                 description="Carne",
                                                 sub_hall=self.sub_hall7)

        self.category8 = Category.objects.create(name="Congelados",
                                                 description="Congelados",
                                                 sub_hall=self.sub_hall8)

        self.category9 = Category.objects.create(name="Bebidas",
                                                 description="Bebidas",
                                                 sub_hall=self.sub_hall9)

        self.category10 = Category.objects.create(name="Higiene",
                                                  description="Higiene",
                                                  sub_hall=self.sub_hall10)

        self.category11 = Category.objects.create(name="Eletrodomésticos",
                                                  description="Eletrodomésticos",
                                                  sub_hall=self.sub_hall11)

        self.category12 = Category.objects.create(name="Telemóveis",
                                                  description="Telemóveis",
                                                  sub_hall=self.sub_hall12)

        # connections
        # SUB HALL1
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall1,  connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall2,  connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall13, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall3,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall4,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall5,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall6,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall7,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall8,  connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall9,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall10, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall11, connected=False, distance=5)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall12, connected=False, distance=6)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall14, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall15, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall16, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall17, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall18, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall19, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall1, sub_hallB=self.sub_hall20, connected=False, distance=5)

        # SUB HALL2
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall1,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall3,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall14, connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall2,  connected=True,  distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall4,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall5,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall6,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall7,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall8,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall9,  connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall10, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall11, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall12, connected=False, distance=5)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall13, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall15, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall16, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall17, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall18, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall19, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall2, sub_hallB=self.sub_hall20, connected=False, distance=4)

        # SUB HALL3
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall2,  connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall4,  connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall15, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall3,  connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall1,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall5,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall6,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall7,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall8,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall9,  connected=False, distance=5)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall10, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall11, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall12, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall13, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall14, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall16, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall17, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall18, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall19, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall3, sub_hallB=self.sub_hall20, connected=False, distance=3)

        # SUB HALL 4
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall16, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall4,  connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall3,  connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall1,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall2,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall5,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall6,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall7,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall8,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall9,  connected=False, distance=5)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall10, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall11, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall12, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall13, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall14, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall15, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall17, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall18, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall19, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall4, sub_hallB=self.sub_hall20, connected=False, distance=3)

        # SUB HALL 5
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall17, connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall13, connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall6,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall5,  connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall1,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall2,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall3,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall4,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall7,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall8,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall9,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall10, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall11, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall12, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall14, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall15, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall16, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall18, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall19, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall5, sub_hallB=self.sub_hall20, connected=False, distance=3)

        # SUB HALL 6
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall6,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall5,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall7,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall18, connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall14, connected=True,  distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall1,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall2,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall3,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall4,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall8,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall9,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall10, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall11, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall12, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall13, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall15, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall16, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall17, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall19, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall6, sub_hallB=self.sub_hall20, connected=False, distance=2)

        # SUB HALL 7
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall7,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall6,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall19, connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall15, connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall16, connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall8,  connected=True,  distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall1,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall2,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall3,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall4,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall5,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall9,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall10, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall11, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall12, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall13, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall14, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall17, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall18, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall7, sub_hallB=self.sub_hall20, connected=False, distance=1)

        # SUB HALL 8
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall7,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall8,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall20, connected=True,  distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall1,  connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall2,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall3,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall4,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall5,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall6,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall9,  connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall10, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall11, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall12, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall13, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall14, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall15, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall16, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall17, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall18, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall8, sub_hallB=self.sub_hall19, connected=False, distance=1)

        # SUB HALL 9
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall9,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall10, connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall17, connected=True,  distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall1,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall2,  connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall3,  connected=False, distance=5)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall4,  connected=False, distance=5)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall5,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall6,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall7,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall8,  connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall11, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall12, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall13, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall14, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall15, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall16, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall18, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall19, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall9, sub_hallB=self.sub_hall20, connected=False, distance=3)

        # SUB HALL 10
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall9,  connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall10, connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall11, connected=True,  distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall18, connected=True,  distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall1,  connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall2,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall3,  connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall4,  connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall5,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall6,  connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall7,  connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall8,  connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall12, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall13, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall14, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall15, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall16, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall17, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall19, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall10, sub_hallB=self.sub_hall20, connected=False, distance=2)

        # SUB HALL 11
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall12, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall10, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall11, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall19, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall1, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall2, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall3, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall4, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall5, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall6, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall7, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall8, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall9, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall13, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall14, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall15, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall16, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall17, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall18, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall11, sub_hallB=self.sub_hall20, connected=False, distance=1)

        # SUB HALL 12
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall20, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall12, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall11, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall1, connected=False, distance=6)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall2, connected=False, distance=5)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall3, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall4, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall5, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall6, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall7, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall8, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall9, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall10, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall13, connected=False, distance=5)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall14, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall15, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall16, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall17, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall18, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall12, sub_hallB=self.sub_hall19, connected=False, distance=1)

        # SUB HALL 13
        SubHallConnection.objects.create(sub_hallA=self.sub_hall13, sub_hallB=self.sub_hall13, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall13, sub_hallB=self.sub_hall14, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall13, sub_hallB=self.sub_hall15, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall13, sub_hallB=self.sub_hall16, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall13, sub_hallB=self.sub_hall17, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall13, sub_hallB=self.sub_hall18, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall13, sub_hallB=self.sub_hall19, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall13, sub_hallB=self.sub_hall20, connected=False, distance=4)

        # SUB HALL 14
        SubHallConnection.objects.create(sub_hallA=self.sub_hall14, sub_hallB=self.sub_hall14, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall14, sub_hallB=self.sub_hall13, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall14, sub_hallB=self.sub_hall15, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall14, sub_hallB=self.sub_hall16, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall14, sub_hallB=self.sub_hall17, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall14, sub_hallB=self.sub_hall18, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall14, sub_hallB=self.sub_hall19, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall14, sub_hallB=self.sub_hall20, connected=False, distance=3)

        # SUB HALL 15
        SubHallConnection.objects.create(sub_hallA=self.sub_hall15, sub_hallB=self.sub_hall15, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall15, sub_hallB=self.sub_hall13, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall15, sub_hallB=self.sub_hall14, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall15, sub_hallB=self.sub_hall16, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall15, sub_hallB=self.sub_hall17, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall15, sub_hallB=self.sub_hall18, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall15, sub_hallB=self.sub_hall19, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall15, sub_hallB=self.sub_hall20, connected=False, distance=2)

        # SUB HALL 16
        SubHallConnection.objects.create(sub_hallA=self.sub_hall16, sub_hallB=self.sub_hall16, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall16, sub_hallB=self.sub_hall13, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall16, sub_hallB=self.sub_hall14, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall16, sub_hallB=self.sub_hall15, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall16, sub_hallB=self.sub_hall17, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall16, sub_hallB=self.sub_hall18, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall16, sub_hallB=self.sub_hall19, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall16, sub_hallB=self.sub_hall20, connected=False, distance=2)

        # SUB HALL 17
        SubHallConnection.objects.create(sub_hallA=self.sub_hall17, sub_hallB=self.sub_hall17, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall17, sub_hallB=self.sub_hall13, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall17, sub_hallB=self.sub_hall14, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall17, sub_hallB=self.sub_hall15, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall17, sub_hallB=self.sub_hall16, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall17, sub_hallB=self.sub_hall18, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall17, sub_hallB=self.sub_hall19, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall17, sub_hallB=self.sub_hall20, connected=False, distance=4)

        # SUB HALL 18
        SubHallConnection.objects.create(sub_hallA=self.sub_hall18, sub_hallB=self.sub_hall18, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall18, sub_hallB=self.sub_hall13, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall18, sub_hallB=self.sub_hall14, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall18, sub_hallB=self.sub_hall15, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall18, sub_hallB=self.sub_hall16, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall18, sub_hallB=self.sub_hall17, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall18, sub_hallB=self.sub_hall19, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall18, sub_hallB=self.sub_hall20, connected=False, distance=3)

        # SUB HALL 19
        SubHallConnection.objects.create(sub_hallA=self.sub_hall19, sub_hallB=self.sub_hall19, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall19, sub_hallB=self.sub_hall13, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall19, sub_hallB=self.sub_hall14, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall19, sub_hallB=self.sub_hall15, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall19, sub_hallB=self.sub_hall16, connected=False, distance=1)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall19, sub_hallB=self.sub_hall17, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall19, sub_hallB=self.sub_hall18, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall19, sub_hallB=self.sub_hall20, connected=False, distance=2)

        # SUB HALL 20
        SubHallConnection.objects.create(sub_hallA=self.sub_hall20, sub_hallB=self.sub_hall20, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=self.sub_hall20, sub_hallB=self.sub_hall13, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall20, sub_hallB=self.sub_hall14, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall20, sub_hallB=self.sub_hall15, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall20, sub_hallB=self.sub_hall16, connected=False, distance=2)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall20, sub_hallB=self.sub_hall17, connected=False, distance=4)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall20, sub_hallB=self.sub_hall18, connected=False, distance=3)
        SubHallConnection.objects.create(sub_hallA=self.sub_hall20, sub_hallB=self.sub_hall19, connected=False, distance=2)

        for sub_hall in SubHall.objects.all():
            count_connections = SubHallConnection.objects.filter(sub_hallA=sub_hall).count()
            if count_connections == 20:
                continue
            else:
                connections = SubHallConnection.objects.filter(sub_hallB=sub_hall)

                for connection in connections:
                    if SubHallConnection.objects.filter(sub_hallA=sub_hall, sub_hallB=connection.sub_hallA).count() == 0:
                        SubHallConnection.objects.create(sub_hallA=sub_hall, sub_hallB=connection.sub_hallA,
                                                         distance=connection.distance, connected=connection.connected)

        for sub_hall in SubHall.objects.all():
            count_connections = SubHallConnection.objects.filter(sub_hallA=sub_hall).count()
            if count_connections == 20:
                continue
            else:
                print "SubHall " + sub_hall.name
                print count_connections

    def test_products(self):
        client = APIClient()

        url = "/api/v1/category/details/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 12)

        url = "/api/v1/category/details/" + str(self.category1.id) + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.category1.id))

        url = "/api/v1/category/hall/" + self.tag1.tag + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        url = "/api/v1/category/search/12/" + str(self.category3.id) + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 6)

        self.assertEqual(response.data[0]["name"], self.sub_hall12.name)
        self.assertEqual(response.data[1]["name"], self.sub_hall11.name)
        self.assertEqual(response.data[2]["name"], self.sub_hall19.name)
        self.assertEqual(response.data[3]["name"], self.sub_hall7.name)
        self.assertEqual(response.data[4]["name"], self.sub_hall15.name)
        self.assertEqual(response.data[5]["name"], self.sub_hall3.name)

