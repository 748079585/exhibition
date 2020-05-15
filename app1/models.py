from django.db import models


# Create your models here.


class Art(models.Model):
    name = models.CharField(max_length=255, null=True)
    date = models.CharField(max_length=255, null=True)
    curator = models.CharField(max_length=255, null=True)

    class Meta:
        abstract = True


class ArtItem(Art):
    exhibition = models.CharField(max_length=255, null=True)
    artist = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'artlinkart'  # 通过db_table自定义数据表名


class Art2Item(Art):
    time = models.CharField(max_length=255, null=True)
    exhibition = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'artron'  # 通过db_table自定义数据表名


class Art3Item(Art):
    time = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = '99ys'  # 通过db_table自定义数据表名
