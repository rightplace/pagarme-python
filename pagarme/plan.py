from pagarme.resources import handler_request
from pagarme.resources.routes import plan_routes

def create(params):
    return handler_request.post(plan_routes.BASE_URL, params)


def find_all():
    return handler_request.get(plan_routes.GET_ALL_PLANS)


def find_by(plan_id):
    return handler_request.get(plan_routes.GET_PLAN_BY_ID.format(plan_id))


def update(plan_id, dictionary):
    return handler_request.put(plan_routes.UPDATE_PLAN.format(plan_id), dictionary)
