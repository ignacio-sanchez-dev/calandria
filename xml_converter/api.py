from http.client import HTTPException
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import APIException

from .convert import xml_to_dict


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]
    

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        response_data = xml_to_dict(request.FILES['file'])
        if response_data:
            return Response(response_data, content_type='application/json')
        else:
            raise APIException("Error parsing xml file.")
