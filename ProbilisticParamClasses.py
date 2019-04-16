from ParameterClasses import *  # import everything from the ParameterClass module
import InputData as Data
import SimPy.RandomVariantGenerators as RVGs
import SimPy.FittingProbDist_MM as MM
import math
import scipy.stats as stat


class Parameters:

    def __init__(self, therapy):

        self.therapy = therapy              # selected therapy
        self.initialHealthState = HealthStates.CD4_200to500     # initial health state
        self.annualTreatmentCost = 0        # annual treatment cost
        self.rateMatrix = []                # transition probability matrix of the selected therapy
        self.annualStateCosts = []          # annual state costs
        self.annualStateUtilities = []      # annual state utilities
        self.discountRate = Data.DISCOUNT   # discount rate


class ParameterGenerator:

    def __init__(self, therapy):

        self.therapy = therapy
        self.probMatrixRVG = []     # list of dirichlet distributions for transition probabilities
        self.lnRelativeRiskRVG = None  # normal distribution for the natural log of the treatment relative risk
        self.annualStateCostRVG = []  # list of gamma distributions for the annual cost of states
        self.annualStateUtilityRVG = []  # list of beta distributions for the annual utility of states

        # create Dirichlet distributions for transition probabilities


        # treatment relative risk
        rr_ci = [0.365, 0.71]   # confidence interval of the treatment relative risk

        # find the mean and st_dev of the normal distribution assumed for ln(RR)
        # sample mean ln(RR)

        # sample standard deviation of ln(RR)

        # create a normal distribution for ln(RR)


        # create gamma distributions for annual state cost


        # create beta distributions for annual state utility


    def get_new_parameters(self, rng):
        """
        :param rng: random number generator
        :return: a new parameter set
        """

        # create a parameter set
        param = Parameters(therapy=self.therapy)

        # calculate transition probabilities


        # sampled relative risk


        # calculate transition probabilities between hiv states
        if self.therapy == Therapies.MONO:
            # calculate transition probability matrix for the mono therapy
            param.rateMatrix = get_rate_matrix_mono(trans_prob_matrix=prob_matrix)

        elif self.therapy == Therapies.COMBO:
            # calculate transition probability matrix for the combination therapy
            param.rateMatrix = get_rate_matrix_combo(
                rate_matrix_mono=get_rate_matrix_mono(trans_prob_matrix=prob_matrix),
                combo_rr=rr)

        # sample from gamma distributions that are assumed for annual state costs


        # sample from beta distributions that are assumed for annual state utilities


        # return the parameter set
        return param
