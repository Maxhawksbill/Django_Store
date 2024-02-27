from products.models import Store
from rest_framework import serializers
from .product import ProductSerializer, ProductForStoreSerializer
from .store_inventory import StoreInventorySerializer

class StoreReadOnlySerializer(serializers.ModelSerializer):
    inventory = serializers.SerializerMethodField()
    inventory_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Store
        fields = ('id', 'name', 'country', 'city', 'address', 'square', 'employees_num', 'inventory', 'inventory_amount', 'notes', 'opened_date')

    def get_inventory(self, obj):
        inventory_data = []
        for store_inventory in obj.store_inventory.all():
            inventory_data.append({
                'product': ProductForStoreSerializer(store_inventory.inventory).data,
                'quantity': store_inventory.quantity,
                'amount': store_inventory.amount()
            })
        return inventory_data
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'country', 'city', 'address', 'square', 'employees_num', 'inventory', 'inventory_amount', 'notes', 'opened_date')
