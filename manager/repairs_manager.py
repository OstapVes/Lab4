from manager.sort_order import SortOrder


class RepairsManager:

    def __init__(self, repairs=list):
        self.repairs = repairs

    def sort_by_price(self, order: SortOrder):
        out = list()
        self.repairs.sort(key=lambda x: x.price, reverse=bool(order.value))
        out = self.repairs
        return out

    def sort_by_brand(self, order: SortOrder):
        out = list()
        self.repairs.sort(key=lambda x: x.brand, reverse=bool(order.value))
        out = self.repairs
        return out

    def print_repairs(self):
        for repair in self.repairs:
            print(type(repair))
            print(str(repair))

            #lambda x: x+10