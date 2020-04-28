import sys
import uuid

from agent.base import BaseAgent
from base.protocol import OfferRequest, OfferResponse, RoundResult, DealRequest, DealResponse


def init_ai_agent(class_path) -> BaseAgent:
    print(f"Create agent from {class_path}")
    split_result = class_path.rsplit('.', 1)
    class_name = split_result[1]
    module_path = split_result[0]
    mod = __import__(module_path, fromlist=[class_name])
    klass = getattr(mod, class_name)
    instance = klass()
    return instance


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Specify agent module path. Example: 'agent.dummy.DummyAgent'")
        sys.exit(0)
    agent = init_ai_agent(sys.argv[1])
    agent.agent_id = str(uuid.uuid4())
    # test offer_action
    target_agent_uid = str(uuid.uuid4())
    offer = agent.offer_action(OfferRequest(
        round_id=1,
        target_agent_uid=target_agent_uid,
        total_amount=100
    ))
    error = OfferResponse(offer).find_error()
    if error:
        print(error)
        sys.exit(0)
    # test round_result_action success
    agent.round_result_action(RoundResult(
        round_id=1,
        win=True,
        agent_gain={
            agent.agent_id: offer,
            target_agent_uid: 100 - offer
        }
    ))
    # test deal_action
    accepted = agent.deal_action(DealRequest(
        round_id=2,
        from_agent_uid=target_agent_uid,
        total_amount=100,
        offer=1
    ))
    DealResponse(accepted).find_error()
    if error:
        print(error)
        sys.exit(0)
    # test round_result_action disconnection_failure
    agent.round_result_action(RoundResult(
        round_id=2,
        win=False,
        agent_gain={
            agent.agent_id: 0,
            target_agent_uid: 0
        },
        disconnection_failure=True
    ))
    print("Base test successfully completed!")
