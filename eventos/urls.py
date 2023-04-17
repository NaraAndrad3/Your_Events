from django.urls import path
from . import views

urlpatterns = [
    path('new_event/',views.new_event,name = "new_event"),
    path('gerenciar_evento/', views.gerenciar_evento, name="gerenciar_evento"),
    path('inscrever_evento/<int:id>/', views.inscrever_evento, name="inscrever_evento"),
    path('participantes_evento/<int:id>/', views.participantes_evento, name="participantes_evento"),
    path('gerar_csv/<int:id>/', views.gerar_csv, name="gerar_csv"), 
    path('certificados_evento/<int:id>/', views.certificados_evento, name="certificados_evento"),
    path('gerar_certificado/<int:id>/', views.gerar_certificado, name="gerar_certificado"),
    path('procurar_certificado/<int:id>/', views.procurar_certificado, name="procurar_certificado")
] 