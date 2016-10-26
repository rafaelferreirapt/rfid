# coding=utf-8
# -*- coding: utf-8 -*-
from django.test import TestCase
from rest_framework.test import APIClient
from halls.models import Hall, SubHall, ContentSubHall, SubHallTag


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

        # contents
        self.content1_1 = ContentSubHall.objects.create(sub_hall=self.sub_hall1, media="image", url="https://www.continente.pt/stores/continente/PublishingImages/Images/PageView/assinatura/imagem-porco.jpg")
        self.content1_2 = ContentSubHall.objects.create(sub_hall=self.sub_hall1, media="image", url="https://campanha.continente.pt/images/971x389.jpg")
        self.content1_3 = ContentSubHall.objects.create(sub_hall=self.sub_hall1, media="image", url="http://c3.quickcachr.fotos.sapo.pt/i/o1213706d/15171764_cG9c8.jpeg")
        self.content1_4 = ContentSubHall.objects.create(sub_hall=self.sub_hall1, media="video", url="https://www.youtube.com/watch?v=cn0cyshPEgE")

        self.content2_1 = ContentSubHall.objects.create(sub_hall=self.sub_hall2, media="image", url="https://static.noticiasaominuto.com/stockimages/1370x587/naom_51424ad93b6bd.jpg")
        self.content2_2 = ContentSubHall.objects.create(sub_hall=self.sub_hall2, media="image", url="http://www.promocoesedescontos.com/wp-content/uploads/2016/07/Captura-de-ecra%CC%83-2016-07-25-a%CC%80s-21.32.15.png")
        self.content2_3 = ContentSubHall.objects.create(sub_hall=self.sub_hall2, media="image", url="https://i.ytimg.com/vi/rC4YuHlTEUM/maxresdefault.jpg")
        self.content2_4 = ContentSubHall.objects.create(sub_hall=self.sub_hall2, media="video", url="https://www.youtube.com/watch?v=aADwoFu2fWs")

        self.content3_1 = ContentSubHall.objects.create(sub_hall=self.sub_hall3, media="image", url="http://6.fotos.web.sapo.io/i/o8d148530/18278804_4Tn31.jpeg")
        self.content3_2 = ContentSubHall.objects.create(sub_hall=self.sub_hall3, media="image", url="http://5.fotos.web.sapo.io/i/G361150e3/17830920_L9zAc.jpeg")
        self.content3_3 = ContentSubHall.objects.create(sub_hall=self.sub_hall3, media="image", url="http://6.fotos.web.sapo.io/i/G2c11967d/17966185_hCtKw.jpeg")
        self.content3_4 = ContentSubHall.objects.create(sub_hall=self.sub_hall3, media="video", url="https://www.youtube.com/watch?v=du1_Mn9a8IU")

        self.content4_1 = ContentSubHall.objects.create(sub_hall=self.sub_hall4, media="image", url="http://www.promocoesedescontos.com/wp-content/uploads/2016/07/Captura-de-ecra%CC%83-2016-06-27-a%CC%80s-21.44.56.png")
        self.content4_2 = ContentSubHall.objects.create(sub_hall=self.sub_hall4, media="image", url="http://globodicas.com.br/wp-content/uploads/2011/11/promocoes.jpg")
        self.content4_3 = ContentSubHall.objects.create(sub_hall=self.sub_hall4, media="image", url="http://thumbs.web.sapo.io/?Q=70&H=1610&W=1899&epic=gYnYmiSzhM+iVZRYVwVtQnQPKL0AAGLF+KxkqhpDZg4IDsqJB769LSb3qQXJRd6cfVBLxeo5dLYIB573BOasaqYdEUkTy+qoF0kyYzNBMXnmXhQ=")
        self.content4_4 = ContentSubHall.objects.create(sub_hall=self.sub_hall4, media="video", url="https://www.youtube.com/watch?v=ctAQwBK_Vzw")

    def test_objects(self):
        client = APIClient()

        url = "/api/v1/halls/details/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 11)

        url = "/api/v1/halls/details/" + self.hall1.name + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.hall1.id))

        url = "/api/v1/halls/sub_halls/details/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 20)

        url = "/api/v1/halls/sub_halls/details/" + self.sub_hall1.name + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.sub_hall1.id))

        url = "/api/v1/halls/sub_halls/contents/" + self.sub_hall1.name + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
