from django.test import TestCase
from halls.models import Hall, ProductHalls, Product
from rest_framework.test import APIClient


class ObjectsTestCase(TestCase):
    def setUp(self):
        self.hall1 = Hall.objects.create(tag="1A253")
        self.hall2 = Hall.objects.create(tag="1A254")
        self.hall3 = Hall.objects.create(tag="1A255")
        self.hall4 = Hall.objects.create(tag="1A256")

        self.product1 = Product.objects.create(name="Apagador Quadro Branco", description="Artigo com 2 anos de garantia.",
                                               brand="note", price=3.49)
        self.product2 = Product.objects.create(name="Fita Corretora Fun 5mm x 8mm", description="Artigo com 2 anos de garantia.",
                                               brand="note", price=1.69)
        self.product3 = Product.objects.create(name="Azeite Virgem Extra Reserva",
                                               description="Azeites obtidos a partir do fruto da oliveira unicamente por processos mecanicos ou outros processos fisicos,...",
                                               brand="Gallo", price=3.49)
        self.product4 = Product.objects.create(name="Flor de Viseu Branco DOC Dao Selection",
                                               description="Vinho Branco DOC Dao Selection Flor de Viseu garrafa 75 cl ",
                                               brand="Flor de Viseu", price=2.89)

        self.productHall1 = ProductHalls.objects.create(product=self.product1,
                                                        hall=self.hall1)
        self.productHall2 = ProductHalls.objects.create(product=self.product2,
                                                        hall=self.hall2)
        self.productHall3 = ProductHalls.objects.create(product=self.product3,
                                                        hall=self.hall3)
        self.productHall4 = ProductHalls.objects.create(product=self.product4,
                                                        hall=self.hall4)

    def test_products(self):
        client = APIClient()

        url = "/api/v1/product/details/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

        url = "/api/v1/product/details/" + str(self.product1.id) + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.product1.id))

        url = "/api/v1/product/hall/" + self.hall1.tag + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
