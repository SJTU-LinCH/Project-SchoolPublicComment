#_*_coding:utf-8_*_
from models import Entertainment
#导入表结构
#导入rest_framework的serializers方法
from rest_framework import serializers

#继承serializers.HyperlinkedModelSerializer超链接方法，看页面都是用链接操作的
class EntertainmentSerializer(serializers.HyperlinkedModelSerializer):
    #实际这里也对数据进行了验证，但这个认证是由MerchantProfile表结构来完成。api中没有定义这个验证
    class Meta:
        #选择对应的表
        model = Entertainment
        #定义处理User表中的字段。序列化这些字段。这里只处理Merchant表的数据，如果传递来的是其它表数据那么对不起 这里会报错
        fields = ( 'entertainmentname','entertainmentaddress','service')
