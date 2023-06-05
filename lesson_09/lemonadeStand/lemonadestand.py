class InvalidSalesItem(Exception):
    pass 

class MenuItem:
    def __init__(self, item_name, item_wholesale_cost, item_selling_price):
        self._item_name = item_name 
        self._item_wholesale_cost = item_wholesale_cost
        self._item_selling_price = item_selling_price
    
    def get_item_name(self):
        return self._item_name
    
    def get_item_wholesale_cost(self):
        return self._item_wholesale_cost
    
    def get_item_selling_price(self):
        return self._item_selling_price


class SalesForDay:
    def __init__(self, days_open, dict_items_sold):
        self._days_open = days_open 
        self._dict_items_sold = dict_items_sold 
    
    #get day and get sales dict
    def get_days(self):
        return self._days_open

    def get_dict_items_sold(self):
        return self._dict_items_sold 


class LemonadeStand:
    def __init__(self, name):
        self._name = name 
        self._current_day = 0
        self._menu_item_object = {}
        self._sales_history = [] 
    
    def get_name(self):
        return self._name 
    
    def add_menu_item(self, menu_object):
        self._menu_item_object.update({menu_object.get_item_name(): menu_object})
    
    def enter_sales_history(self, sales_dict):
        items_sold_today = list(sales_dict.keys())
        try:
            for item_name in items_sold_today:
                if item_name not in self._menu_item_object:
                    raise Exception('The item you sold today is not on your menu, where did you get it?')
            sales_for_day_object = SalesForDay(self._current_day, sales_dict)
            self._sales_history.append(sales_for_day_object)
            self._current_day += 1
        except:
            raise InvalidSalesItem('No information for that day')

    def sales_of_menu_item_for_day(self, day, menu_item_name):
        for sales_object in self._sales_history:
            sales_object_day = sales_object.get_days()

            if sales_object_day == day:
                sales_object_dict = sales_object.get_sales_dict() 
                sales_for_menu_item_today = sales_object_dict.get(menu_item_name, "None of that item was sold on this day")
                return sales_for_menu_item_today
        return "No information found for this day"
    
    def total_sales_for_menu_item(self, menu_item_name):
        total = 0
        for sales_object in self._sales_history:
            if sales_object == menu_item_name:
                day = sales_object.get_days() 
                total += self.sales_of_menu_item_for_day(day, menu_item_name)
    
        return total 
    
    def total_profit_for_menu_items(self, menu_item_name):
        total_items = 0 

        total_items += self.total_sales_for_menu_item(menu_item_name)

        cost_of_item_sales = total_items * self._menu_item_object[menu_item_name].get_item_selling_price()
        print(cost_of_item_sales)
    
        cost_of_item_wholesale = total_items * self._menu_item_object[menu_item_name].get_item_wholesale_cost() 
        print(total_items)
        return cost_of_item_sales - cost_of_item_wholesale
    
    def total_profit_for_stand(self):
        total_historical_profit = 0

        for menu_item_object in self._menu_item_object:
            total_historical_profit += self.total_profit_for_menu_items(menu_item_object)
            print(total_historical_profit)
        return total_historical_profit
    

    # stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand callled 'Lemons R Us'
    # item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
    # stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
    # item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
    # stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
    # item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
    # stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'


    # day_0_sales = {
    #     'lemonade' : 5,
    #     'cookie'   : 2
    # }
    # stand.enter_sales_history(day_0_sales)
    # print(f"lemonade profit = {stand.total_profit_for_menu_items('lemonade')}")  # print the total profit for lemonade so far
stand = LemonadeStand('LemonHead')
item1 = MenuItem('lemonade', 1.75, 3.50)
item2 = MenuItem('cupcake', .60, 1.50)
stand.add_menu_item(item1)
stand.add_menu_item(item2)
day_0 = {
    'lemonade' : 3,
    'cupcake' : 5
    }
day_1 = {
    'cupcake' : 2
    }
day_2 = {
    'lemonade' : 5
    }
stand.enter_sales_history(day_0)
stand.enter_sales_history(day_1)
stand.enter_sales_history(day_2)
total_profit = stand.total_profit_for_stand()
print(total_profit)
#self.assertEqual(total_profit, 20.30)

# if __name__ == "__main__":
#     main() 