import graphene

from graphene_django import DjangoObjectType

from card_management.models import Card, CardUnit


class CardUnitType(DjangoObjectType):

    class Meta:
        model = CardUnit
        fields = ('id', 'card', 'variant', 'quatity',
                  'price', 'data')
        interfaces = (graphene.relay.Node, )


class CardUnitConnection(graphene.relay.Connection):

    class Meta:
        node = CardUnitType


class CardType(DjangoObjectType):

    class Meta:
        model = Card
        fields = ('id', 'total_quantity', 'total_price',
                  'last_status_change', 'updated_at', 'created_at',
                  'created_by', 'status', 'cardunit_set')
        interfaces = (graphene.relay.Node, )

    cardunit_set = graphene.relay.ConnectionField(CardUnitConnection)

    def resolve_cardunit_set(root, info, **kwargs):
        return root.cardunit_set.all()


class CardConnection(graphene.relay.Connection):

    class Meta:
        node = CardType
