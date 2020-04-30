from agent.base import BaseAgent
from base.protocol import OfferRequest, DealRequest, RoundResult


class MyAgent(BaseAgent):

    def get_my_name(self) -> str:
        return '<first_name.second_name_>'

    def offer_action(self, m: OfferRequest) -> int:
        return 1

    def deal_action(self, m: DealRequest) -> bool:
        return True

    def round_result_action(self, data: RoundResult):
        pass

