import unittest
from src.log_config import main_logger
from src.calc.calculate_phase_base import BY_ZERO_BALANCE
from src.calc.calculate_phaseZeroBalance import CalculatePhaseZeroBalance
from src.model import reward_log
from src.model.reward_log import RewardLog


class TestCalculatePhaseZeroBalance(unittest.TestCase):
    def setUp(self):
        self.logger = main_logger
        self.calculator = CalculatePhaseZeroBalance()
        self.reactivate_zeroed = False
        self.reward_logs = [
            RewardLog(
                address="mv1ECyK9zWCEaS7NnRMCM6pKWwvLHL4hWjHq",
                type=reward_log.TYPE_DELEGATOR,
                delegating_balance=5500000,
                current_balance=0,
                originaladdress="mv1ECyK9zWCEaS7NnRMCM6pKWwvLHL4hWjHq",
            ),
            RewardLog(
                address="mv1NMKxCyYAKvPoSrdcKmuqu95YaSBqQwyGP",
                type=reward_log.TYPE_OWNER,
                delegating_balance=5500000,
                current_balance=233,
                originaladdress="mv1ECyK9zWCEaS7NnRMCM6pKWwvLHL4hWjHq",
            ),
        ]

    def test_calculate(self):
        result = self.calculator.calculate(self.reward_logs, self.reactivate_zeroed)
        self.assertEqual(result[0].desc, BY_ZERO_BALANCE)
        self.assertEqual(result[0].skipped, True)
        self.assertEqual(result[0].needs_activation, False)
        self.assertEqual(result[1].desc, "")
        self.assertEqual(result[1].skipped, False)
        self.assertEqual(result[1].needs_activation, False)

    def test_calculate_with_reactivate_zeroed(self):
        self.reactivate_zeroed = True
        result = self.calculator.calculate(self.reward_logs, self.reactivate_zeroed)
        self.assertEqual(result[0].skipped, False)
        self.assertEqual(result[0].needs_activation, True)
        self.assertEqual(result[1].desc, "")
        self.assertEqual(result[1].skipped, False)
        self.assertEqual(result[1].needs_activation, False)
