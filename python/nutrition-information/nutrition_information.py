#Author: Antonio Olivares Ramirez

class FoodItem:
    """Simple nutrition model: name + macros per serving; can print info and compute calories."""
    def __init__(self, name: str = 'None', fat: float = 0.0, carbs: float = 0.0, protein: float = 0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
       
    def get_calories(self, num_servings: float) -> float:
        #formula to calculate item calories
        #calories = 9*fat + 4*carbs + 4*protein, per serving -> scaled by num_servings
        return ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        
       
    def print_info(self) -> None:
        print(f'Nutritional information per serving of {self.name}:')
        print(f'   Fat: {self.fat:.2f} g')
        print(f'   Carbohydrates: {self.carbs:.2f} g')
        print(f'   Protein: {self.protein:.2f} g')

if __name__ == "__main__":
    
    food_item1 = FoodItem()
   
    item_name = "M&M's"  #input()
    amount_fat = 10.0 #float(input())
    amount_carbs = 34.0 #float(input())
    amount_protein = 2.0  #float(input())
    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
      
    num_servings = 1.0 #float(input())
      
    food_item1.print_info()
    #print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,food_item1.get_calories(num_servings)))
    print(f'Number of calories for {num_servings:.2f} serving(s): {food_item1.get_calories(num_servings):.2f}')

                           
    print()
                           
    food_item2.print_info()
    #print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,food_item2.get_calories(num_servings)))
    print(f'Number of calories for {num_servings:.2f} serving(s): {food_item2.get_calories(num_servings):.2f}')