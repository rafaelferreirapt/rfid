# coding=utf-8
from django.core.management.base import BaseCommand
from halls.models import Hall, CategoryHalls, Category, HallConnection, ContentHall


class Command(BaseCommand):
    help = 'This script inserts the scripts for you'

    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **options):
        """
        Assumimos então que:
        O Hall 1 tem os seguintes sub-halls:
        - 1 (Início)
            tags:
            -
            -
            -
        - 2
            tags:
            -
            -
            -
        - 3
            tags:
            -
            -
            -
        - 4
            tags:
            -
            -
            -
        O Hall 2 tem os seguintes sub-halls:
        - 5
            tags:
            -
            -
            -
        - 6
            tags:
            -
            -
            -
        - 7
            tags:
            -
            -
            -
        - 8
            tags:
            -
            -
            -
        O Hall 3 tem os seguintes sub-halls:
        - 9
            tags:
            -
            -
            -
        - 10
            tags:
            -
            -
            -
        - 11
            tags:
            -
            -
            -
        - 12
            tags:
            -
            -
            -
        O Hall 4 tem os seguintes sub-halls:
        - 13
            tags:
            -
            -
            -
        O Hall 5 tem os seguintes sub-halls:
        - 14
            tags:
            -
            -
            -
        O Hall 6 tem os seguintes sub-halls:
        - 15
            tags:
            -
            -
            -
        O Hall 7 tem os seguintes sub-halls:
        - 16
            tags:
            -
            -
            -
        O Hall 8 tem os seguintes sub-halls:
        - 17
            tags:
            -
            -
            -
        O Hall 9 tem os seguintes sub-halls:
        - 18
            tags:
            -
            -
            -
        O Hall 10 tem os seguintes sub-halls:
        - 19
            tags:
            -
            -
            -
        O Hall 11 tem os seguintes sub-halls:
        - 20
            tags:
            -
            -
            -

        """


        hall1 = Hall.objects.create(tag="1A253")  # top
        hall2 = Hall.objects.create(tag="1A254")  # middle
        hall3 = Hall.objects.create(tag="1A255")  # bottom
        hall6 = Hall.objects.create(tag="1A256")  # left
        hall7 = Hall.objects.create(tag="1A257")  # right

        content1_1 = ContentHall.objects.create(hall=hall1, media="image", url="https://www.continente.pt/stores/continente/PublishingImages/Images/PageView/assinatura/imagem-porco.jpg")
        content1_2 = ContentHall.objects.create(hall=hall1, media="image", url="https://campanha.continente.pt/images/971x389.jpg")
        content1_3 = ContentHall.objects.create(hall=hall1, media="image", url="http://c3.quickcachr.fotos.sapo.pt/i/o1213706d/15171764_cG9c8.jpeg")
        content1_4 = ContentHall.objects.create(hall=hall1, media="video", url="/static/video1.mp4")

        content2_1 = ContentHall.objects.create(hall=hall2, media="image", url="https://static.noticiasaominuto.com/stockimages/1370x587/naom_51424ad93b6bd.jpg")
        content2_2 = ContentHall.objects.create(hall=hall2, media="image", url="http://www.promocoesedescontos.com/wp-content/uploads/2016/07/Captura-de-ecra%CC%83-2016-07-25-a%CC%80s-21.32.15.png")
        content2_3 = ContentHall.objects.create(hall=hall2, media="image", url="https://i.ytimg.com/vi/rC4YuHlTEUM/maxresdefault.jpg")
        content2_4 = ContentHall.objects.create(hall=hall2, media="video", url="/static/video2.mp4")

        content3_1 = ContentHall.objects.create(hall=hall3, media="image", url="http://6.fotos.web.sapo.io/i/o8d148530/18278804_4Tn31.jpeg")
        content3_2 = ContentHall.objects.create(hall=hall3, media="image", url="http://5.fotos.web.sapo.io/i/G361150e3/17830920_L9zAc.jpeg")
        content3_3 = ContentHall.objects.create(hall=hall3, media="image", url="http://6.fotos.web.sapo.io/i/G2c11967d/17966185_hCtKw.jpeg")
        content3_4 = ContentHall.objects.create(hall=hall3, media="video", url="/static/video3.mp4")

        content4_1 = ContentHall.objects.create(hall=hall6, media="image", url="http://www.promocoesedescontos.com/wp-content/uploads/2016/07/Captura-de-ecra%CC%83-2016-06-27-a%CC%80s-21.44.56.png")
        content4_2 = ContentHall.objects.create(hall=hall6, media="image", url="http://globodicas.com.br/wp-content/uploads/2011/11/promocoes.jpg")
        content4_3 = ContentHall.objects.create(hall=hall6, media="image", url="http://thumbs.web.sapo.io/?Q=70&H=1610&W=1899&epic=gYnYmiSzhM+iVZRYVwVtQnQPKL0AAGLF+KxkqhpDZg4IDsqJB769LSb3qQXJRd6cfVBLxeo5dLYIB573BOasaqYdEUkTy+qoF0kyYzNBMXnmXhQ=")
        content4_4 = ContentHall.objects.create(hall=hall6, media="video", url="/static/video4.mp4")

        category1 = Category.objects.create(name="Massas", description="Massas para cozinha.")
        category2 = Category.objects.create(name="Águas", description="Águas.")
        category3 = Category.objects.create(name="Vinhos", description="Vinhos portugueses")
        category6 = Category.objects.create(name="Congelados", description="Gelados")
        category7 = Category.objects.create(name="Carnes", description="Carnes congeladas")
        
        """
        CATEGORY HALLS
        """
        CategoryHalls.objects.create(category=category1,
                                     hall=hall1)
        CategoryHalls.objects.create(category=category2,
                                     hall=hall2)
        CategoryHalls.objects.create(category=category3,
                                     hall=hall3)
        CategoryHalls.objects.create(category=category6,
                                     hall=hall6)
        CategoryHalls.objects.create(category=category7,
                                     hall=hall7)
        
        """
        CONNECTIONS
        """
        HallConnection.objects.create(hallA=hall1, hallB=hall1, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall1, hallB=hall6, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall1, hallB=hall7, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall1, hallB=hall2, connected=False, distance=1)
        HallConnection.objects.create(hallA=hall1, hallB=hall3, connected=False, distance=1)
        
        HallConnection.objects.create(hallA=hall6, hallB=hall6, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall6, hallB=hall1, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall6, hallB=hall2, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall6, hallB=hall3, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall6, hallB=hall7, connected=False, distance=1)
        
        HallConnection.objects.create(hallA=hall7, hallB=hall7, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall7, hallB=hall1, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall7, hallB=hall2, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall7, hallB=hall3, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall7, hallB=hall6, connected=False, distance=1)
        
        HallConnection.objects.create(hallA=hall2, hallB=hall2, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall2, hallB=hall6, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall2, hallB=hall7, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall2, hallB=hall1, connected=False, distance=1)
        HallConnection.objects.create(hallA=hall2, hallB=hall3, connected=False, distance=1)
        
        HallConnection.objects.create(hallA=hall3, hallB=hall3, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall3, hallB=hall6, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall3, hallB=hall7, connected=True, distance=0)
        HallConnection.objects.create(hallA=hall3, hallB=hall1, connected=False, distance=1)
        HallConnection.objects.create(hallA=hall3, hallB=hall2, connected=False, distance=1)
