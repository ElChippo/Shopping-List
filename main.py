import streamlit as st

# Meal categories, meals, and ingredients
meals_by_category = {
    "Breakfasts": ["Shakshuka", "Breakfast Quesadilla", "Microwave Meal", "Sausage Rolls", "Chicken Flatbreads"],
    "Pasta Meals": ["Bolognese"],
    "Rice Meals": ["Chicken Curry", "Beef and Rice", "Korean Chicken and Rice"],
    "Noodle Meals": ["Thai Sriracha Noodles"],
    "Wraps/Pitta Meals": ["Kebab", "Tacos"],
    "Junk Food": ["Hot Dogs", "Burgers", "Pizza"],
    "Other Food Items": ["Yoghurts", "Kiwis", "Oil"],
    "Extra": ["Toilet Paper", "Toothpaste", "Bodywash", "Kitchen Roll", "Cat Treats", "Air Freshener"],
}

ingredients_by_meal = {
    "Shakshuka": ["Onion", "Pasata", "Eggs", "Paprika", "Cumin"],
    "Breakfast Quesadilla": ["Tortilla", "Eggs", "Cheese", "Bacon Lardons"],
    "Microwave Meal": ["Microwave Meal"],
    "Sausage Rolls": ["Sausage Rolls"],
    "Chicken Flatbreads": ["Flatbread", "Chicken Skewers", "Cheese"],
    "Bolognese": ["Mince Beef", "Pasta", "Pasta Sauce", "Cheese"],
    "Chicken Curry": ["Chicken", "Rice", "Curry Sauce", "Pepper"],
    "Beef and Rice": ["Beef Cut", "Rice", "Taco Seasoning", "Sugar Snap Peas"],
    "Korean Chicken and Rice": ["Frozen Chicken", "Rice", "Miso Paste"],
    "Thai Sriracha Noodles": ["Ready Cooked Noodles", "Sriracha", "Chicken"],
    "Kebab": ["Kebab Bread", "Kebab Meat", "Chips"],
    "Tacos": ["Taco Bread", "Mince Beef", "Cheese", "Lettuce", "Taco Sauce", "Chips"],
    "Hot Dogs": ["Hot Dog Buns", "Hot Dogs", "Onion", "Chips"],
    "Burgers": ["Burger Buns", "Burger Patties", "Cheese", "Onion", "Chips"],
    "Pizza": ["Pizza", "Chips"],
    "Toilet Paper": ["Toilet Paper"],
    "Toothpaste": ["Toothpaste"],
    "Bodywash": ["Bodywash"],
    "Kitchen Roll": ["Kitchen Roll"],
    "Cat Treats": ["Cat Treats"],
    "Kiwis": ["Kiwis"],
    "Yoghurts": ["Yoghurts"],
    "Air Freshener": ["Air Freshener"],
    "Oil": ["Oil"],
}

ingredients_order = [
    #Fruit and Veg Isle
    "Sugar Snap Peas", "Ready Cooked Noodles", "Mushrooms", "Kiwis",

    #Meat And Dairy Isle
    "Chicken", "Beef Cut", "Mince Beef", "Bacon Lardons", "Cheese", "Yoghurts", "Burger Patties", "Sausage Rolls", "Pizza", "Microwave Meal", "Kebab Meat", "Hot Dogs",
    
    #Bread Isle
    "Tortilla", "Kebab Bread", "Burger Buns", "Hot Dog Buns", "Eggs", "Oil", "Pepper", "Flatbread", "Taco Bread",

    #Canned Isle
    "Pasata", "Pasta Sauce", "Curry Sauce", "Miso Paste", "Pasta", "Rice", "Sriracha", "Taco Seasoning", "Paprika", "Cumin", "Salt", "Pepper", "Onion", "Taco Sauce", "Lettuce",

    #Snack Isle
    "Peanuts", "Walnuts",

    #Frozen Isle
    "Frozen Chicken", "Chips", "Chicken Skewers",

    #Other Isles
    "Toothpaste", "Bodywash", "Toilet Paper", "Kitchen Roll", "Cat Treats", "Air Freshener",
]


# Initialize session state for selected meals
if "selected_meals" not in st.session_state:
    st.session_state.selected_meals = []

if "selected_ingredients" not in st.session_state:
    st.session_state.selected_ingredients = []

ordered_ingredients = st.session_state.ordered_ingridients = []

# Step 1: Select meal category
selected_category = st.selectbox("Select Meal Category", list(meals_by_category.keys()))

# Step 2: Show meals for the selected category
meals = meals_by_category[selected_category]
selected_meal = st.selectbox("Select Meal", meals)


# Button to add the selected meal
if st.button("Add Meal"):
    st.session_state.selected_meals.append(selected_meal)
    for ingredient in ingredients_by_meal[selected_meal]:
        st.session_state.selected_ingredients.append(ingredient)

new_ingredient = st.text_input("Add a new ingredient")
if st.button("Add Ingredient"):
    # Only add if not empty and not already in the list
    if new_ingredient.strip():
        st.session_state.selected_ingredients.append(new_ingredient.strip())
        st.rerun()


    # Display all selected meals with their ingredients
if st.session_state.selected_meals:
    st.write("## Selected Items")
    for meal in st.session_state.selected_meals:
        st.write(f"- {meal}")
    st.write("### Shopping List")

if st.session_state.selected_ingredients: 
    ordered_ingredients = sorted(
    st.session_state.selected_ingredients,
    key=lambda x: ingredients_order.index(x) if x in ingredients_order else float('inf')
)
    unduplicated_ingredients = list(dict.fromkeys(ordered_ingredients))
    combined_ingredients = {}
    for ingredient in unduplicated_ingredients:
        count = ordered_ingredients.count(ingredient)
        if count > 1:
            combined_ingredients[ingredient] = (f"{ingredient} x{count}")
        else:                           
            combined_ingredients[ingredient] = (ingredient)
    
    with st.container():
        for ingredient, label in combined_ingredients.items():
            if st.button(label, key=label):
                st.session_state.selected_ingredients.remove(ingredient)
                st.rerun()
    
    st.write("### Shopping List Without Buttons")

    with st.container():
        for ingredient in combined_ingredients.values():
                st.write(f"- {ingredient}")


    
