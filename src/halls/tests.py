# coding=utf-8
from django.test import TestCase
from rest_framework.test import APIClient
from halls.models import Hall, ContentHall


class ObjectsTestCase(TestCase):
    def setUp(self):
        self.hall1 = Hall.objects.create(tag="1A253")  # top
        self.hall2 = Hall.objects.create(tag="1A254")  # middle
        self.hall3 = Hall.objects.create(tag="1A255")  # bottom
        self.hall4 = Hall.objects.create(tag="1A256")  # left
        self.hall5 = Hall.objects.create(tag="1A257")  # right

        self.content1_1 = ContentHall.objects.create(hall=self.hall1, url="https://www.continente.pt/stores/continente/PublishingImages/Images/PageView/assinatura/imagem-porco.jpg")
        self.content1_2 = ContentHall.objects.create(hall=self.hall1, url="https://campanha.continente.pt/images/971x389.jpg")
        self.content1_3 = ContentHall.objects.create(hall=self.hall1, url="http://c3.quickcachr.fotos.sapo.pt/i/o1213706d/15171764_cG9c8.jpeg")
        self.content1_4 = ContentHall.objects.create(hall=self.hall1, url="https://www.youtube.com/watch?v=cn0cyshPEgE")

        self.content2_1 = ContentHall.objects.create(hall=self.hall2, url="https://static.noticiasaominuto.com/stockimages/1370x587/naom_51424ad93b6bd.jpg")
        self.content2_2 = ContentHall.objects.create(hall=self.hall2, url="http://www.promocoesedescontos.com/wp-content/uploads/2016/07/Captura-de-ecra%CC%83-2016-07-25-a%CC%80s-21.32.15.png")
        self.content2_3 = ContentHall.objects.create(hall=self.hall2, url="https://i.ytimg.com/vi/rC4YuHlTEUM/maxresdefault.jpg")
        self.content2_4 = ContentHall.objects.create(hall=self.hall2, url="https://www.youtube.com/watch?v=aADwoFu2fWs")

        self.content3_1 = ContentHall.objects.create(hall=self.hall3, url="http://6.fotos.web.sapo.io/i/o8d148530/18278804_4Tn31.jpeg")
        self.content3_2 = ContentHall.objects.create(hall=self.hall3, url="http://5.fotos.web.sapo.io/i/G361150e3/17830920_L9zAc.jpeg")
        self.content3_3 = ContentHall.objects.create(hall=self.hall3, url="http://6.fotos.web.sapo.io/i/G2c11967d/17966185_hCtKw.jpeg")
        self.content3_4 = ContentHall.objects.create(hall=self.hall3, url="https://www.youtube.com/watch?v=du1_Mn9a8IU")

        self.content4_1 = ContentHall.objects.create(hall=self.hall4, url="http://www.promocoesedescontos.com/wp-content/uploads/2016/07/Captura-de-ecra%CC%83-2016-06-27-a%CC%80s-21.44.56.png")
        self.content4_2 = ContentHall.objects.create(hall=self.hall4, url="http://globodicas.com.br/wp-content/uploads/2011/11/promocoes.jpg")
        self.content4_3 = ContentHall.objects.create(hall=self.hall4, url="http://thumbs.web.sapo.io/?Q=70&H=1610&W=1899&epic=gYnYmiSzhM+iVZRYVwVtQnQPKL0AAGLF+KxkqhpDZg4IDsqJB769LSb3qQXJRd6cfVBLxeo5dLYIB573BOasaqYdEUkTy+qoF0kyYzNBMXnmXhQ=")
        self.content4_4 = ContentHall.objects.create(hall=self.hall4, url="https://www.youtube.com/watch?v=ctAQwBK_Vzw")

    def test_objects(self):
        client = APIClient()

        url = "/api/v1/halls/details/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)

        url = "/api/v1/halls/details/" + self.hall1.tag + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.hall1.id))

        url = "/api/v1/halls/contents/" + self.hall1.tag + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
