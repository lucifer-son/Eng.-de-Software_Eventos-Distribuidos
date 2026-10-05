import json
import time
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORTA = 1883
TOPICO = "pedido/criado"

cliente = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="produtor"
)

cliente.connect(BROKER, PORTA, 60)

evento = {
    "tipo": "PedidoCriado",
    "pedido_id": 123,
    "cliente": "Rafael",
    "produto": "Notebook",
    "valor": 3500.00
}

print("Publicando evento...")
print(json.dumps(evento, indent=4, ensure_ascii=False))

resultado = cliente.publish(
    TOPICO,
    json.dumps(evento),
    qos=1
)

resultado.wait_for_publish()

print("\nEvento publicado com sucesso!")

cliente.disconnect()