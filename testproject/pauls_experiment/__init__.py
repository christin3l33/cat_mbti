from otree.api import *

doc = """
Students will get their Python codes graded
"""
author = 'leeevm@bc.edu'


class C(BaseConstants):
    NAME_IN_URL = 'css'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.LongStringField(label="Write a Python function called my_sort that takes a list of integers as the\
    input and returns a list of the same integers in increasing order.")
    q2 = models.LongStringField(label="Write a Python function called my_length that takes a list of integers and \
    returns the length of a list.")
    q3 = models.LongStringField(label="Write a Python function called my_max that takes a list of integers and returns \
    the maximum number.")
    correct = models.IntegerField()
    correct_q1 = models.IntegerField()
    correct_q2 = models.IntegerField()
    correct_q3 = models.IntegerField()
    cheated = models.IntegerField()
    cheated_q1 = models.IntegerField()
    cheated_q2 = models.IntegerField()
    cheated_q3 = models.IntegerField()
    rebuttal_q1 = models.LongStringField()
    rebuttal_q2 = models.LongStringField()
    rebuttal_q3 = models.LongStringField()


class Question1(Page):
    form_model = 'player'
    form_fields = ['q1']
    timeout_seconds = 5 * 60

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        with open('../user_q1.py', 'w') as file:
            file.write(player.q1)

        user_list = [5,6,1,2]
        correct_list = [1,2,5,6]

        with open('../user_q1.py', 'r') as file:
            from testproject.user_q1 import my_sort

            answer_list = my_sort(user_list)
            if answer_list == correct_list:
                player.correct_q1 = 1
            else:
                player.correct_q1 = 0
            word = ".sort("
            content = file.read()

            if word in content:
                player.cheated_q1 = 1
            else:
                player.cheated_q1 = 0


class Question2(Page):
    form_model = 'player'
    form_fields = ['q2']
    timeout_seconds = 5 * 60

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        with open('../user_q2.py', 'w') as file:
            file.write(player.q2)

        user_list = [5,6,1,2]
        correct_length = 4

        with open('../user_q2.py', 'r') as file:
            from testproject.user_q2 import my_length

            answer_length = my_length(user_list)
            if answer_length == correct_length:
                player.correct_q2 = 2
            else:
                player.correct_q2 += 0
            word = ".len("
            content = file.read()

            if word in content:
                player.cheated_q2 = 2
            else:
                player.cheated_q2 = 0


class Question3(Page):
    form_model = 'player'
    form_fields = ['q3']
    timeout_seconds = 5 * 60

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        with open('user_q3.py', 'w') as file:
            file.write(player.q3)

        user_list = [5,6,1,2]
        correct_max = 6

        with open('user_q3.py', 'r') as file:
            from user_q3 import my_max

            answer_max = my_max(user_list)
            if answer_max == correct_max:
                player.correct_q3 = 4
            else:
                player.correct_q3 += 0
            word = ".max("
            content = file.read()

            if word in content:
                player.cheated_q3 = 4
            else:
                player.cheated_q3 = 0

        player.correct = player.correct_q1 + player.correct_q2 + player.correct_q3
        player.cheated = player.cheated_q1 + player.cheated_q2 + player.cheated_q3


class GradePage(Page):
    form_model = 'player'
    form_fields = ['rebuttal_q1', 'rebuttal_q2', 'rebuttal_q3']


class Result(Page):
    pass


page_sequence = [
    Question1, Question2, Question3, GradePage, Result
    ]