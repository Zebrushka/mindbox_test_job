import random
import plotext as plt


def generate_random_number(length: int):
    """
    Random number generator of a given length
    """
    return int(''.join([str(random.randint(0,9)) for _ in range(length)]))


def visualize_abtest_group_distribution(data: dict):
    """
    Help function to draw barplot
    This function use termplotlib, who draw plot in terminal
    """

    x = [int(i) for i in data.values()]
    y = [int(i) for i in data.keys()]
    
    plt.bar(data.keys(), data.values())
    plt.title("check that we got a normal distribution")
    
    return plt.show()


def count_customers(n_customers: int, n_first_id: int = 0):

    """
    A function that counts the number of customers in each group if the ID numbering 
    is continuous and starts from 0. The function receives an integer n_customers 
    (the number of customers) as input.
    """

    ab_test_group_dict = {}

    # check that a non-decreasing sequence is given
    if (n_customers - n_first_id) > 0:
        for i in range(n_first_id, n_customers):
            ab_test_group = sum(map(int, str(i)))
            ab_test_group_dict[ab_test_group] = ab_test_group_dict.get(ab_test_group, 0) + 1

    return ab_test_group_dict




if __name__ == "__main__":
    
    # Genereate sample 
    n_customers = generate_random_number(7)
    n_first_id = generate_random_number(5)
    print('n_customers: ', n_customers, 'n_first_id: ', n_first_id)

    # function work with single parameter
    print(count_customers(n_customers))

    # function work with two paramaters
    print(count_customers(n_customers, n_first_id))

    # Let's see how the groups are distributed
    visualize_abtest_group_distribution(count_customers(n_customers, n_first_id))


    

