import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORTA = 1883
TOPICO = "pedido/criado"

def ao_receber_evento(cliente, userdata, mensagem):

    evento = json.loads(mensagem.payload.decode())

    print("\n[ NOTIFICAÇÃO ]")
    print(f"Cliente: {evento['cliente']}")
    print(f"Pedido: {evento['pedido_id']}")
    print("Enviando confirmação ao cliente...")


cliente = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="servico-notificacao"
)

cliente.on_message = ao_receber_evento

cliente.connect(BROKER, PORTA, 60)

cliente.subscribe(TOPICO, qos=1)

print("Serviço de notificação aguardando eventos...")

cliente.loop_forever()