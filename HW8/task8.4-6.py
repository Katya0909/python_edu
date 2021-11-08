class Warehouse:
    equipment_count = {}

    @classmethod
    def add_to_warehouse(cls, item_type, item_name, item_count):
        cls.equipment_count[item_type][item_name]['count'] += item_count

    @classmethod
    def remove_from_warehouse(cls, item_type, item_name, item_count):
        cls.equipment_count[item_type][item_name]['count'] -= item_count

    @staticmethod
    def get_all_equipment():
        for k, v in Warehouse.equipment_count.items():
            print(k, v)


warehouse = Warehouse()
print(warehouse)
