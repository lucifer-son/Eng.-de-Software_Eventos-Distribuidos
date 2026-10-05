import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORTA = 1883
TOPICO = "pedido/criado"

def ao_receber_evento(cliente, userdata, mensagem):

    evento = json.loads(mensagem.payload.decode())

    print("\n[ ESTOQUE ]")
    print(f"Pedido recebido: {evento['pedido_id']}")
    print(f"Produto: {evento['produto']}")
    print("Estoque atualizado!")


cliente = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="servico-estoque"
)

cliente.on_message = ao_receber_evento

cliente.connect(BROKER, PORTA, 60)

cliente.subscribe(TOPICO, qos=1)

print("Serviço de estoque aguardando eventos...")

cliente.loop_forever()