from otree.api import *



doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class C(BaseConstants):
    NAME_IN_URL = 'cat_mbti'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.IntegerField(label="You peep out the window and see a group of cats.",
                             widget=widgets.RadioSelect,
                             choices=[[1,"Go outside and meet the new cats"],
                                      [-1,"Stay inside and take a mini power nap"]])
    q2 = models.IntegerField(label="You’re walking around and accidentally bumped into a door.",
                             widget=widgets.RadioSelect,
                             choices=[[1, "Look for someone to help you with the pain"],
                                      [-1, "Deal with the pain by yourself"]])
    q3 = models.IntegerField(label="What type of cat would you be?",
                             widget=widgets.RadioSelect,
                             choices=[[1, "The friendly and energetic type"],
                                      [-1, "The reserved and down-to-earth type"]])
    q4 = models.IntegerField(label="You’re deep in your thoughts. What are you thinking?",
                             widget=widgets.RadioSelect,
                             choices=[[1, "What should I do right now?"],
                                      [-1, "What will happen tomorrow?"]])
    q5 = models.IntegerField(label="You took a nap and had a dream. What was it about?",
                             widget=widgets.RadioSelect,
                             choices=[[1, "Your everyday life"],
                                      [-1, "A fantasy where you entered a fairytale"]])
    q6 = models.IntegerField(label="You’re on your daily walk and suddenly face a big ledge.",
                             widget=widgets.RadioSelect,
                             choices=[[1, "Take your regular path"],
                                      [-1, "Try to make the leap"]])
    q7 = models.IntegerField(label="You finally get your food! But you see a different cat eyeing your food",
                             widget=widgets.RadioSelect,
                             choices=[[1, "Offer them your food"],
                                      [-1,"Don’t think much of it and dig into your food"]])
    q8 = models.IntegerField(label="A fellow cat tries to jump onto the couch but falls instead",
                             widget=widgets.RadioSelect,
                             choices=[[1, "Are they okay?"],
                                      [-1, "That must have hurt!"]])
    q9 = models.IntegerField(label="You hear a kitten cry.",
                             widget=widgets.RadioSelect,
                             choices=[[1, "Check up on them"],
                                      [-1, "Someone else will check up on them"]])
    q10 = models.IntegerField(label="You approach the toy box that you organized. Is it…",
                              widget=widgets.RadioSelect,
                              choices=[[1, "Neat and clear where each toy is"],
                                       [-1, "Messy, where you usually grab the first toy you see"]])
    q11 = models.IntegerField(label="Would you rather…",
                              widget=widgets.RadioSelect,
                              choices=[[1, "Schedule walks around the neighborhood"],
                                       [-1, "Randomly go out whenever you feel like it"]])
    q12 = models.IntegerField(label="The couch seems very scratchable. Do you…",
                              widget=widgets.RadioSelect,
                              choices=[[1, "Withstand the urge and play with a toy instead"],
                                       [-1, "Scratch away"]])
    e_or_i = models.IntegerField()
    s_or_n = models.IntegerField()
    t_or_f = models.IntegerField()
    j_or_p = models.IntegerField()
    final_mbti = models.StringField()
    e_or_i_result = models.StringField()
    s_or_n_result = models.StringField()
    t_or_f_result = models.StringField()
    j_or_p_result = models.StringField()
    true_or_not = models.CharField()


def set_payoffs(player: Player):
    if player.true_or_not == "Same":
        player.payoff += cu(10)


# FUNCTIONS
# PAGES
class Mbti(Page):
    form_model = 'player'
    form_fields = ['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.e_or_i = player.q1 + player.q2 + player.q3
        if player.e_or_i > 0:
            player.e_or_i_result = "E"
        else:
            player.e_or_i_result = "I"
        player.s_or_n = player.q4 + player.q5 + player.q6
        if player.s_or_n > 0:
            player.s_or_n_result = "S"
        else:
            player.s_or_n_result = "N"
        player.t_or_f = player.q7 + player.q8 + player.q9
        if player.t_or_f > 0:
            player.t_or_f_result = "F"
        else:
            player.t_or_f_result = "T"
        player.j_or_p = player.q10 + player.q11 + player.q12
        if player.j_or_p > 0:
            player.j_or_p_result = "J"
        else:
            player.j_or_p_result = "P"
        player.final_mbti = str(player.e_or_i_result + player.s_or_n_result + player.t_or_f_result + player.j_or_p_result)


class Questions(Page):
    form_model = 'player'
    form_fields = ['true_or_not']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_payoffs(player)


class Results(Page):
    pass


page_sequence = [Mbti, Questions, Results]
