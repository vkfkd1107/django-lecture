from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action, renderer_classes
from rest_framework.viewsets import ModelViewSet
from instagram.serializers import PostSerializer
from instagram.models import Post
from rest_framework import mixins
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        author = self.request.user
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author=author ,ip=ip)

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'post_detail.html'

    def get(self, request, *args, **kwargs):
        return Response({
            'post': self.get_object(),
        })


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def static_html_view(request):
    return Response('<html><body><h1>Hello world...!</h1></body></html>')


@api_view(['GET'])
def hello(request, format=None):
    return Response([])
