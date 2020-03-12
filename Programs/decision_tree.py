
# Models are decision tree
# Batandwa Mgutsi
# 12/03/2020


class DecisionCase:
    """A Decision case has a sentence and a set of two other decision cases to execute on yes and on no"""
    """answers by the user in case the DecisonCase requires input"""

    sentence = None
    requiresAnswer = True
    yesCase = None
    noCase = None

    def __init__(self, sentence, requiresAnswer=True, yesCase=None, noCase=None):
        self.sentence = sentence
        self.yesCase = yesCase
        self.noCase = noCase
        self.requiresAnswer = requiresAnswer


def executeDecisionCase(decisionCase):
    print(decisionCase.sentence)
    if(decisionCase.requiresAnswer):
        answer = input()
        if(answer == 'yes' and decisionCase.yesCase != None):
            executeDecisionCase(decisionCase.yesCase)
        elif(answer == 'no' and decisionCase.noCase != None):
            executeDecisionCase(decisionCase.noCase)
        else:
            print("Please enter a 'yes' or a 'no'")
            executeDecisionCase(decisionCase)


# These are all the decison that have to be made

isBoy = DecisionCase(
    sentence='Are you a boy?',
    requiresAnswer=True,
    yesCase=DecisionCase(
        sentence='You are a boy!',
        requiresAnswer=False,
    ),
    noCase=DecisionCase(
        sentence='MMM!! Are you a girl?',
        requiresAnswer=True,
        yesCase=DecisionCase(
            sentence='You are a girl!',
            requiresAnswer=False,
        ),
        noCase=DecisionCase(
            sentence='MMM! i am so confused right now!',
            requiresAnswer=False
        )
    )
)

executeDecisionCase(isBoy)
