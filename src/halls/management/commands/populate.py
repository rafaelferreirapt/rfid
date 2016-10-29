# coding=utf-8
from django.core.management.base import BaseCommand
from halls.models import Hall, SubHall, Category, SubHallTag, ContentSubHall, SubHallConnection


class Command(BaseCommand):
    help = 'This script inserts the scripts for you'

    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **options):
        # hall 1
        hall1 = Hall.objects.create(name="1")
        sub_hall1 = SubHall.objects.create(name="1", parent_hall=hall1)
        tag1 = SubHallTag.objects.create(tag="1", parent_hall=sub_hall1)

        # hall 2
        hall2 = Hall.objects.create(name="2")
        sub_hall2 = SubHall.objects.create(name="2", parent_hall=hall2)
        tag2 = SubHallTag.objects.create(tag="2", parent_hall=sub_hall2)

        # hall 3
        hall3 = Hall.objects.create(name="3")
        sub_hall3 = SubHall.objects.create(name="3", parent_hall=hall3)
        tag3 = SubHallTag.objects.create(tag="3", parent_hall=sub_hall3)

        # hall 4
        hall4 = Hall.objects.create(name="4")
        sub_hall4 = SubHall.objects.create(name="4", parent_hall=hall4)
        tag4 = SubHallTag.objects.create(tag="4", parent_hall=sub_hall4)

        # hall 5
        hall5 = Hall.objects.create(name="5")
        sub_hall5 = SubHall.objects.create(name="5", parent_hall=hall5)
        tag5 = SubHallTag.objects.create(tag="5", parent_hall=sub_hall5)

        # hall 6
        hall6 = Hall.objects.create(name="6")
        sub_hall6 = SubHall.objects.create(name="6", parent_hall=hall6)
        tag6 = SubHallTag.objects.create(tag="6", parent_hall=sub_hall6)

        # hall 7
        hall7 = Hall.objects.create(name="7")
        sub_hall7 = SubHall.objects.create(name="7", parent_hall=hall7)
        tag7 = SubHallTag.objects.create(tag="7", parent_hall=sub_hall7)

        # hall 8
        hall8 = Hall.objects.create(name="8")
        sub_hall8 = SubHall.objects.create(name="8", parent_hall=hall8)
        tag8 = SubHallTag.objects.create(tag="8", parent_hall=sub_hall8)

        # hall 9
        hall9 = Hall.objects.create(name="9")
        sub_hall9 = SubHall.objects.create(name="9", parent_hall=hall9)
        tag9 = SubHallTag.objects.create(tag="9", parent_hall=sub_hall9)

        # hall 10
        hall10 = Hall.objects.create(name="10")
        sub_hall10 = SubHall.objects.create(name="10", parent_hall=hall10)
        tag10 = SubHallTag.objects.create(tag="10", parent_hall=sub_hall10)

        # hall 11
        hall11 = Hall.objects.create(name="11")
        sub_hall11 = SubHall.objects.create(name="11", parent_hall=hall11)
        tag11 = SubHallTag.objects.create(tag="11", parent_hall=sub_hall11)

        # hall 12
        hall12 = Hall.objects.create(name="12")
        sub_hall12 = SubHall.objects.create(name="12", parent_hall=hall12)
        tag12 = SubHallTag.objects.create(tag="12", parent_hall=sub_hall12)

        # hall 13
        hall13 = Hall.objects.create(name="13")
        sub_hall13 = SubHall.objects.create(name="13", parent_hall=hall13)
        tag13 = SubHallTag.objects.create(tag="13", parent_hall=sub_hall13)

        # hall 14
        hall14 = Hall.objects.create(name="14")
        sub_hall14 = SubHall.objects.create(name="14", parent_hall=hall14)
        tag14 = SubHallTag.objects.create(tag="14", parent_hall=sub_hall14)

        # hall 15
        hall15 = Hall.objects.create(name="15")
        sub_hall15 = SubHall.objects.create(name="15", parent_hall=hall15)
        tag15 = SubHallTag.objects.create(tag="15", parent_hall=sub_hall15)

        # hall 16
        hall16 = Hall.objects.create(name="16")
        sub_hall16 = SubHall.objects.create(name="16", parent_hall=hall16)
        tag16 = SubHallTag.objects.create(tag="16", parent_hall=sub_hall16)

        # hall 17
        hall17 = Hall.objects.create(name="17")
        sub_hall17 = SubHall.objects.create(name="17", parent_hall=hall17)
        tag17 = SubHallTag.objects.create(tag="17", parent_hall=sub_hall17)

        # hall 18
        hall18 = Hall.objects.create(name="18")
        sub_hall18 = SubHall.objects.create(name="18", parent_hall=hall18)
        tag18 = SubHallTag.objects.create(tag="18", parent_hall=sub_hall18)

        # hall 19
        hall19 = Hall.objects.create(name="19")
        sub_hall19 = SubHall.objects.create(name="19", parent_hall=hall19)
        tag19 = SubHallTag.objects.create(tag="19", parent_hall=sub_hall19)

        # hall 20
        hall20 = Hall.objects.create(name="20")
        sub_hall20 = SubHall.objects.create(name="20", parent_hall=hall20)
        tag20 = SubHallTag.objects.create(tag="20", parent_hall=sub_hall20)

        # categories example
        category1 = Category.objects.create(name="Arroz",
                                                 description="Arroz",
                                                 sub_hall=sub_hall1)

        category2 = Category.objects.create(name="Massas",
                                                 description="Massas",
                                                 sub_hall=sub_hall2)

        category3 = Category.objects.create(name="Especiarias",
                                                 description="Especiarias",
                                                 sub_hall=sub_hall3)

        category4 = Category.objects.create(name="Concentrados",
                                                 description="Concentrados",
                                                 sub_hall=sub_hall4)

        category5 = Category.objects.create(name="Pao",
                                                 description="Pao",
                                                 sub_hall=sub_hall5)

        category6 = Category.objects.create(name="Peixe",
                                                 description="Peixe",
                                                 sub_hall=sub_hall6)

        category7 = Category.objects.create(name="Carne",
                                                 description="Carne",
                                                 sub_hall=sub_hall7)

        category8 = Category.objects.create(name="Congelados",
                                                 description="Congelados",
                                                 sub_hall=sub_hall8)

        category9 = Category.objects.create(name="Bebidas",
                                                 description="Bebidas",
                                                 sub_hall=sub_hall9)

        category10 = Category.objects.create(name="Higiene",
                                                  description="Higiene",
                                                  sub_hall=sub_hall10)

        category11 = Category.objects.create(name="Eletrodomesticos",
                                                  description="Eletrodomesticos",
                                                  sub_hall=sub_hall11)

        category12 = Category.objects.create(name="Telemoveis",
                                                  description="Telemoveis",
                                                  sub_hall=sub_hall12)

        # connections
        # SUB HALL1
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall1, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall2, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall13, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall3, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall4, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall5, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall6, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall7, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall8, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall9, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall10, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall11, connected=False,
                                         distance=5)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall12, connected=False,
                                         distance=6)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall14, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall15, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall16, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall17, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall18, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall19, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall1, sub_hallB=sub_hall20, connected=False,
                                         distance=5)

        # SUB HALL2
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall1, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall3, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall14, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall2, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall4, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall5, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall6, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall7, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall8, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall9, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall10, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall11, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall12, connected=False,
                                         distance=5)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall13, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall15, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall16, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall17, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall18, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall19, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall2, sub_hallB=sub_hall20, connected=False,
                                         distance=4)

        # SUB HALL3
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall2, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall4, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall15, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall3, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall1, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall5, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall6, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall7, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall8, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall9, connected=False,
                                         distance=5)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall10, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall11, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall12, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall13, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall14, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall16, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall17, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall18, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall19, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall3, sub_hallB=sub_hall20, connected=False,
                                         distance=3)

        # SUB HALL 4
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall16, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall4, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall3, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall1, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall2, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall5, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall6, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall7, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall8, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall9, connected=False,
                                         distance=5)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall10, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall11, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall12, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall13, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall14, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall15, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall17, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall18, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall19, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall4, sub_hallB=sub_hall20, connected=False,
                                         distance=3)

        # SUB HALL 5
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall17, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall13, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall6, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall5, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall1, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall2, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall3, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall4, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall7, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall8, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall9, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall10, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall11, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall12, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall14, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall15, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall16, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall18, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall19, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall5, sub_hallB=sub_hall20, connected=False,
                                         distance=3)

        # SUB HALL 6
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall6, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall5, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall7, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall18, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall14, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall1, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall2, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall3, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall4, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall8, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall9, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall10, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall11, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall12, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall13, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall15, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall16, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall17, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall19, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall6, sub_hallB=sub_hall20, connected=False,
                                         distance=2)

        # SUB HALL 7
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall7, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall6, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall19, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall15, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall16, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall8, connected=True, distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall1, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall2, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall3, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall4, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall5, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall9, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall10, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall11, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall12, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall13, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall14, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall17, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall18, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall7, sub_hallB=sub_hall20, connected=False,
                                         distance=1)

        # SUB HALL 8
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall7, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall8, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall20, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall1, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall2, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall3, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall4, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall5, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall6, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall9, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall10, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall11, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall12, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall13, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall14, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall15, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall16, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall17, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall18, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall8, sub_hallB=sub_hall19, connected=False,
                                         distance=1)

        # SUB HALL 9
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall9, connected=True, distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall10, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall17, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall1, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall2, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall3, connected=False,
                                         distance=5)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall4, connected=False,
                                         distance=5)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall5, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall6, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall7, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall8, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall11, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall12, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall13, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall14, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall15, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall16, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall18, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall19, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall9, sub_hallB=sub_hall20, connected=False,
                                         distance=3)

        # SUB HALL 10
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall9, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall10, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall11, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall18, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall1, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall2, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall3, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall4, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall5, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall6, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall7, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall8, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall12, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall13, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall14, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall15, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall16, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall17, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall19, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall10, sub_hallB=sub_hall20, connected=False,
                                         distance=2)

        # SUB HALL 11
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall12, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall10, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall11, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall19, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall1, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall2, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall3, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall4, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall5, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall6, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall7, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall8, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall9, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall13, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall14, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall15, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall16, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall17, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall18, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall11, sub_hallB=sub_hall20, connected=False,
                                         distance=1)

        # SUB HALL 12
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall20, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall12, connected=True,
                                         distance=0)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall11, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall1, connected=False,
                                         distance=6)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall2, connected=False,
                                         distance=5)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall3, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall4, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall5, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall6, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall7, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall8, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall9, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall10, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall13, connected=False,
                                         distance=5)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall14, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall15, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall16, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall17, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall18, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall12, sub_hallB=sub_hall19, connected=False,
                                         distance=1)

        # SUB HALL 13
        SubHallConnection.objects.create(sub_hallA=sub_hall13, sub_hallB=sub_hall13, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall13, sub_hallB=sub_hall14, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall13, sub_hallB=sub_hall15, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall13, sub_hallB=sub_hall16, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall13, sub_hallB=sub_hall17, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall13, sub_hallB=sub_hall18, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall13, sub_hallB=sub_hall19, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall13, sub_hallB=sub_hall20, connected=False,
                                         distance=4)

        # SUB HALL 14
        SubHallConnection.objects.create(sub_hallA=sub_hall14, sub_hallB=sub_hall14, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall14, sub_hallB=sub_hall13, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall14, sub_hallB=sub_hall15, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall14, sub_hallB=sub_hall16, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall14, sub_hallB=sub_hall17, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall14, sub_hallB=sub_hall18, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall14, sub_hallB=sub_hall19, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall14, sub_hallB=sub_hall20, connected=False,
                                         distance=3)

        # SUB HALL 15
        SubHallConnection.objects.create(sub_hallA=sub_hall15, sub_hallB=sub_hall15, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall15, sub_hallB=sub_hall13, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall15, sub_hallB=sub_hall14, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall15, sub_hallB=sub_hall16, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall15, sub_hallB=sub_hall17, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall15, sub_hallB=sub_hall18, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall15, sub_hallB=sub_hall19, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall15, sub_hallB=sub_hall20, connected=False,
                                         distance=2)

        # SUB HALL 16
        SubHallConnection.objects.create(sub_hallA=sub_hall16, sub_hallB=sub_hall16, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall16, sub_hallB=sub_hall13, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall16, sub_hallB=sub_hall14, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall16, sub_hallB=sub_hall15, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall16, sub_hallB=sub_hall17, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall16, sub_hallB=sub_hall18, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall16, sub_hallB=sub_hall19, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall16, sub_hallB=sub_hall20, connected=False,
                                         distance=2)

        # SUB HALL 17
        SubHallConnection.objects.create(sub_hallA=sub_hall17, sub_hallB=sub_hall17, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall17, sub_hallB=sub_hall13, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall17, sub_hallB=sub_hall14, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall17, sub_hallB=sub_hall15, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall17, sub_hallB=sub_hall16, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall17, sub_hallB=sub_hall18, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall17, sub_hallB=sub_hall19, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall17, sub_hallB=sub_hall20, connected=False,
                                         distance=4)

        # SUB HALL 18
        SubHallConnection.objects.create(sub_hallA=sub_hall18, sub_hallB=sub_hall18, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall18, sub_hallB=sub_hall13, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall18, sub_hallB=sub_hall14, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall18, sub_hallB=sub_hall15, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall18, sub_hallB=sub_hall16, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall18, sub_hallB=sub_hall17, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall18, sub_hallB=sub_hall19, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall18, sub_hallB=sub_hall20, connected=False,
                                         distance=3)

        # SUB HALL 19
        SubHallConnection.objects.create(sub_hallA=sub_hall19, sub_hallB=sub_hall19, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall19, sub_hallB=sub_hall13, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall19, sub_hallB=sub_hall14, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall19, sub_hallB=sub_hall15, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall19, sub_hallB=sub_hall16, connected=False,
                                         distance=1)
        SubHallConnection.objects.create(sub_hallA=sub_hall19, sub_hallB=sub_hall17, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall19, sub_hallB=sub_hall18, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall19, sub_hallB=sub_hall20, connected=False,
                                         distance=2)

        # SUB HALL 20
        SubHallConnection.objects.create(sub_hallA=sub_hall20, sub_hallB=sub_hall20, connected=True,
                                         distance=0)
        # not connected
        SubHallConnection.objects.create(sub_hallA=sub_hall20, sub_hallB=sub_hall13, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall20, sub_hallB=sub_hall14, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall20, sub_hallB=sub_hall15, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall20, sub_hallB=sub_hall16, connected=False,
                                         distance=2)
        SubHallConnection.objects.create(sub_hallA=sub_hall20, sub_hallB=sub_hall17, connected=False,
                                         distance=4)
        SubHallConnection.objects.create(sub_hallA=sub_hall20, sub_hallB=sub_hall18, connected=False,
                                         distance=3)
        SubHallConnection.objects.create(sub_hallA=sub_hall20, sub_hallB=sub_hall19, connected=False,
                                         distance=2)

        for sub_hall in SubHall.objects.all():
            count_connections = SubHallConnection.objects.filter(sub_hallA=sub_hall).count()
            if count_connections == 20:
                continue
            else:
                connections = SubHallConnection.objects.filter(sub_hallB=sub_hall)

                for connection in connections:
                    if SubHallConnection.objects.filter(sub_hallA=sub_hall,
                                                        sub_hallB=connection.sub_hallA).count() == 0:
                        SubHallConnection.objects.create(sub_hallA=sub_hall, sub_hallB=connection.sub_hallA,
                                                         distance=connection.distance, connected=connection.connected)

        for sub_hall in SubHall.objects.all():
            count_connections = SubHallConnection.objects.filter(sub_hallA=sub_hall).count()
            if count_connections == 20:
                continue
            else:
                print "SubHall " + sub_hall.name
                print count_connections

        # contents
        content1_1 = ContentSubHall.objects.create(sub_hall=sub_hall1, media="image", url="https://www.continente.pt/stores/continente/PublishingImages/Images/PageView/assinatura/imagem-porco.jpg")
        content1_2 = ContentSubHall.objects.create(sub_hall=sub_hall1, media="image", url="https://campanha.continente.pt/images/971x389.jpg")
        content1_3 = ContentSubHall.objects.create(sub_hall=sub_hall1, media="image", url="http://c3.quickcachr.fotos.sapo.pt/i/o1213706d/15171764_cG9c8.jpeg")
        content1_4 = ContentSubHall.objects.create(sub_hall=sub_hall1, media="video", url="https://www.youtube.com/watch?v=cn0cyshPEgE")

        content2_1 = ContentSubHall.objects.create(sub_hall=sub_hall2, media="image", url="https://static.noticiasaominuto.com/stockimages/1370x587/naom_51424ad93b6bd.jpg")
        content2_2 = ContentSubHall.objects.create(sub_hall=sub_hall2, media="image", url="http://www.promocoesedescontos.com/wp-content/uploads/2016/07/Captura-de-ecra%CC%83-2016-07-25-a%CC%80s-21.32.15.png")
        content2_3 = ContentSubHall.objects.create(sub_hall=sub_hall2, media="image", url="https://i.ytimg.com/vi/rC4YuHlTEUM/maxresdefault.jpg")
        content2_4 = ContentSubHall.objects.create(sub_hall=sub_hall2, media="video", url="https://www.youtube.com/watch?v=aADwoFu2fWs")

        content3_1 = ContentSubHall.objects.create(sub_hall=sub_hall3, media="image", url="http://6.fotos.web.sapo.io/i/o8d148530/18278804_4Tn31.jpeg")
        content3_2 = ContentSubHall.objects.create(sub_hall=sub_hall3, media="image", url="http://5.fotos.web.sapo.io/i/G361150e3/17830920_L9zAc.jpeg")
        content3_3 = ContentSubHall.objects.create(sub_hall=sub_hall3, media="image", url="http://6.fotos.web.sapo.io/i/G2c11967d/17966185_hCtKw.jpeg")
        content3_4 = ContentSubHall.objects.create(sub_hall=sub_hall3, media="video", url="https://www.youtube.com/watch?v=du1_Mn9a8IU")

        content4_1 = ContentSubHall.objects.create(sub_hall=sub_hall4, media="image", url="http://www.promocoesedescontos.com/wp-content/uploads/2016/07/Captura-de-ecra%CC%83-2016-06-27-a%CC%80s-21.44.56.png")
        content4_2 = ContentSubHall.objects.create(sub_hall=sub_hall4, media="image", url="http://globodicas.com.br/wp-content/uploads/2011/11/promocoes.jpg")
        content4_3 = ContentSubHall.objects.create(sub_hall=sub_hall4, media="image", url="http://thumbs.web.sapo.io/?Q=70&H=1610&W=1899&epic=gYnYmiSzhM+iVZRYVwVtQnQPKL0AAGLF+KxkqhpDZg4IDsqJB769LSb3qQXJRd6cfVBLxeo5dLYIB573BOasaqYdEUkTy+qoF0kyYzNBMXnmXhQ=")
        content4_4 = ContentSubHall.objects.create(sub_hall=sub_hall4, media="video", url="https://www.youtube.com/watch?v=ctAQwBK_Vzw")
