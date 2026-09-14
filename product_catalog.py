from product_data import products

# Step 1 - Print the first few products to see the data
print("First few products:")
print(products[:5])


# Step 2 - Collect customer preferences
customer_preferences = []

response = ""

while response != "N":
    print("\nInput a preference:")
    preference = input().strip().lower()

    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()


# Step 3 - Convert customer preferences to a set to remove duplicates
customer_preferences = set(customer_preferences)


# Step 4 - Convert product tags to sets for faster comparisons
converted_products = []

for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }

    converted_products.append(converted_product)


# Step 5 - Count matching tags
def count_matches(product_tags, customer_preferences):
    matches = product_tags.intersection(customer_preferences)
    return len(matches)


# Step 6 - Recommend products
def recommend_products(products, customer_preferences):
    recommendations = []

    for product in products:
        match_count = count_matches(
            product["tags"],
            customer_preferences
        )

        if match_count > 0:
            recommendations.append({
                "name": product["name"],
                "matches": match_count
            })

    recommendations.sort(
        key=lambda product: product["matches"],
        reverse=True
    )

    return recommendations


# Run the recommendation function
recommendations = recommend_products(
    converted_products,
    customer_preferences
)

print("\nRecommended Products:")

for product in recommendations:
    print(
        "-",
        product["name"],
        "(" + str(product["matches"]) + " match(es))"
    )


# ============================================================
# DESIGN MEMO
# ============================================================
#
# I built this recommendation tool using lists, sets, loops, dictionaries,
# and functions. The customer preferences are first stored in a list because
# the program collects them one at a time from user input. I then convert the
# list into a set, which removes duplicate preferences and makes it easier to
# compare the customer's preferences with product tags. I also convert each
# product's tags into a set. The main comparison uses set intersection to find
# the tags that appear in both the customer's preferences and the product's
# tags. The length of the intersection tells the program how many matches
# there are. A for loop checks each product in the catalog, and products with
# at least one matching tag are placed into a recommendation list. The list
# is then sorted so products with the most matches appear first.
#
# If the catalog contained more than 1,000 products, this basic approach
# would still work, but it would become less efficient because the program
# checks every product each time a recommendation is requested. For a larger
# system, I would consider organizing products by tag using a dictionary or
# another type of index. For example, each tag could point directly to the
# products that contain that tag. This would reduce the number of products
# the program has to search. A larger application could also store product
# information in a database instead of keeping everything in a Python list.
# More advanced recommendation systems could also consider customer history,
# product ratings, purchases, and how strongly different preferences should
# affect the final recommendation.

