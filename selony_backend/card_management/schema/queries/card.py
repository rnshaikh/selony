import graphene

from card_management.models import Card, CardUnit
from card_management.schema.types.card import CardConnection, CardUnitConnection

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated


class CardQueries(graphene.ObjectType):

    cards = graphene.relay.ConnectionField(CardConnection)
    card_units = graphene.relay.ConnectionField(CardUnitConnection)

    @permission_required(is_authenticated)
    def resolve_cards(root, info, **kwargs):
        return Card.objects.filter(created_by=info.context.user)

    @permission_required(is_authenticated)
    def resolve_card_units(root, info, **kwargs):
        return CardUnit.objects.filter(card__created_by=info.context.user)
