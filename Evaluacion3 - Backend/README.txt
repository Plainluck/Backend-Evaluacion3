El nombre del directorio de proyecto sigue siendo Evaluación 2 para evitar problemas con las rutas o con la configuración en general. Aún así, esta entrega corresponde a la Evaluación numero 3 de Programación Backend

##cmd##
python manage.py loaddata PokeTCG/fixtures/expansion.json
python manage.py loaddata PokeTCG/fixtures/elements.json
python manage.py loaddata PokeTCG/fixtures/pokemon.json

##shell##
LOAD MODELS
from <Aplicacion>.models import <Model>
ej: from PokeTCG.models import Pokemon

QUERY MODELS
Card.objects.all()

print(Card.objects.all().values())
