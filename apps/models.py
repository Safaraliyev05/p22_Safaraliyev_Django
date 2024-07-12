from django.db.models import Model, CharField, ImageField, FileField, BooleanField, ForeignKey, CASCADE, DecimalField


class Product(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    description = CharField(max_length=255)
    is_premium = BooleanField(null=False, default=False)


class ProductImage(Model):
    image = ImageField(upload_to='products/%Y/%m/%d/')
    product = ForeignKey('apps.Product', on_delete=CASCADE, related_name='images')


class ProductVideo(Model):
    video = FileField(upload_to='products/%Y/%m/%d/', null=True,)
    product = ForeignKey('apps.Product', on_delete=CASCADE, related_name='videos')
