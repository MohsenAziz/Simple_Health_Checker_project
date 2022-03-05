from all_functions import welcome_message
from all_functions import getting_data
from all_functions import weight
from all_functions import general_tips_questionnaire
from all_functions import general_healthy_tips
from all_functions import food_tips_questionnaire
from all_functions import food_concerning_tips
from all_functions import conclude









welcome_message()
print('\n')
weight(*getting_data())
print('\n')
general_healthy_tips(general_tips_questionnaire())
print('\n')
food_concerning_tips(food_tips_questionnaire())
print('\n')
conclude()
