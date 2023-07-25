system = "You are an innovative cullinary expert that specializes in creative and comprehensive meal suggestions for competet home chefs that value healthy, fresh, and fast meals of global variety"
user = """
"As a resident of northern California, I prefer seasonally appropriate, diverse, and creative meals. My diet is influenced by two main parameters: the cuisine type and the diet focus.  With these parameters in mind, generate 20 meal ideas for me. These meals should ideally be suitable for preparation in an Instant Pot, roasting, dutch oven, or cooking in a cast iron skillet, with the possibility of using a frying pan on the stove. We don't grill. Since we practice intermittent fasting, we typically have two substantial meals a day that don't conform to traditional lunch or dinner structures. Sides that complement the meal are welcome. We do not consume pork and, as we have young children, the meals should avoid spiciness. I value clear, concise, and direct communication. For each meal idea, provide a brief description, keeping in mind the seasonality of ingredients.  Please prefix each recipe with the cooking instrument.

remember: sugar, tomatoes and acid do not belong in a cast iron!

cuisine_type: {{ cuisine_type }}
diet_focus: {{ diet }}
"""
