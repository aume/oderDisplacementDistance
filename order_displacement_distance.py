
def order_displacement_dist(a, b):
    """
    Measures the distance of displacements of common items in list B relative to list A.
    The resulting value is normalized between 0 (no difference) and 1 (maximum displacement).
    It also identifies and prints the most displaced common items.

    Args:
        a (list): The reference list.
        b (list): The list to compare against.

    Returns:
        float: A normalized displacement value between 0 and 1.
    """
    # Create a dictionary for O(1) average time complexity lookups of items in list b.
    # This maps each item in b to its first occurrence index.
    pos_b = {item: index for index, item in enumerate(b)}

    current_displacement_sum = 0
    common_items_indices_in_a = [] # Stores original indices of common items in list 'a'
    common_items_indices_in_b = [] # Stores original indices of common items in list 'b'
    individual_displacements = []  # To store (item, absolute_displacement) for analysis

    # Iterate through list 'a' to find common elements and calculate their displacement.
    # Also collect their original indices for calculating d_max later.
    for i, item_a in enumerate(a):
        if item_a in pos_b:
            j = pos_b[item_a] # Get the index of the common item in list 'b'
            displacement = abs(i - j)
            current_displacement_sum += displacement
            common_items_indices_in_a.append(i)
            common_items_indices_in_b.append(j)
            individual_displacements.append((item_a, displacement))

    num_common_items = len(common_items_indices_in_a)

    # If there are no common items, the displacement is 0.
    if num_common_items == 0:
        print("No common items found between the lists.")
        return 0.0

    # Calculate the maximum possible displacement (d_max) for normalization.
    # This is achieved by sorting the indices of common items from both lists
    # and then pairing the smallest index from one list's set of common items
    # with the largest from the other's, and so on, to maximize the sum of absolute differences.
    sorted_a_indices_of_common = sorted(common_items_indices_in_a)
    sorted_b_indices_of_common = sorted(common_items_indices_in_b)

    max_possible_displacement_sum = 0
    for k in range(num_common_items):
        # Pair the k-th smallest index from 'a' with the (N_common - 1 - k)-th
        # smallest index from 'b' (which is effectively the k-th largest)
        max_possible_displacement_sum += abs(
            sorted_a_indices_of_common[k] - sorted_b_indices_of_common[num_common_items - 1 - k]
        )

    # Handle the case where max_possible_displacement_sum is zero (e.g., a single common item
    # that is perfectly aligned, or lists of length 1 that match).
    if max_possible_displacement_sum == 0:
        print("All common items are perfectly aligned or maximum displacement is zero.")
        # If there are common items but no displacement, it's still 0.
        # This handles cases like a=['a'], b=['a'] where d_current and d_max are both 0.
        # It also implicitly covers the single item case like a=['a','b'], b=['c','a']
        # where the only common item 'a' is perfectly aligned in its relative subset.
        print("Most displaced items (none due to perfect alignment): N/A")
        return 0.0

    # Normalize the calculated displacement sum by the maximum possible sum.
    normalized_displacement = current_displacement_sum / max_possible_displacement_sum

    # Sort individual_displacements to find the most displaced items
    # Sort in descending order based on the displacement value (the second element of the tuple)
    individual_displacements.sort(key=lambda x: x[1], reverse=True)

    print("\n--- Displacement Analysis ---")
    print(f"Total Current Displacement Sum: {current_displacement_sum}")
    print(f"Maximum Possible Displacement Sum: {max_possible_displacement_sum}")
    print(f"Common Items: {num_common_items}")
    print("\nMost Displaced Items (Item, Absolute Displacement):")
    for item, disp in individual_displacements:
        print(f"  - {item}: {disp}")
    print("---------------------------\n")


    return normalized_displacement