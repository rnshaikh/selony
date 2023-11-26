import graphene

from graphql_relay import from_global_id

from django.shortcuts import get_object_or_404

from product_management.models import ProductReview
from product_management.schema.types.product import (ProductReviewType,
                                                     ProductReviewInputType,
                                                     ProductReviewConnection)
from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated


class CreateReview(graphene.relay.ClientIDMutation):

    class Input:
        product_review = ProductReviewInputType(required=True)

    ok = graphene.Boolean()
    product_review = graphene.Field(ProductReviewType)

    @permission_required(is_authenticated)
    def mutate_and_get_payload(root, info, **kwargs):

        if info.context.user.is_superuser:
            raise Exception("Admin Cant Review Product")

        product_review = kwargs.get('product_review', None)

        product_review_obj = ProductReview(**product_review,
                                           created_by=info.context.user)

        return CreateReview.Field(ok=True,
                                  product_review=product_review_obj)


class UpdateReview(graphene.relay.ClientIDMutation):

    class Input:
        id = graphene.ID(required=True)
        product_review = ProductReviewInputType(required=True)

    ok = graphene.Boolean()
    product_review = graphene.Field(ProductReviewType)

    @permission_required(is_authenticated)
    def mutate_and_get_payload(root, info, **kwargs):

        if info.context.user.is_superuser:
            raise Exception("Admin Cant Review Product")

        id = kwargs.get('id', None)
        id = from_global_id(id)[1]

        rev_obj = get_object_or_404(ProductReview, id=id)

        if rev_obj.created_by != info.context.user:
            raise Exception("Not Authorized")

        rev_obj.rating = kwargs.get('rating', rev_obj.rating)
        rev_obj.review = kwargs.get('review', rev_obj.review)
        rev_obj.updated_by = info.context.user
        rev_obj.save()
        return UpdateReview.Field(ok=True, product_review=rev_obj)


class DeleteReview(graphene.relay.ClientIDMutation):

    class Input:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @permission_required(is_authenticated)
    def mutate_and_get_payload(root, info, kwargs):

        if info.context.user.is_superuser:
            raise Exception("Admin Cant Review Product")

        id = kwargs.get('id', None)
        id = from_global_id(id)[1]
        rev_obj = get_object_or_404(ProductReview, id=id)

        if rev_obj.created_by != info.context.user:
            raise Exception("Not Authorized")

        rev_obj.delete()
        return DeleteReview.Field(ok=True)


class ReviewMutation(graphene.ObjectType):

    create_review = CreateReview.Field()
    update_review = UpdateReview.Field()
    delete_review = DeleteReview.Field()

