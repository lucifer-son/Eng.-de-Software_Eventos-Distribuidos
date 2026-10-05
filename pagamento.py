import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORTA = 1883
TOPICO = "pedido/criado"

def ao_receber_evento(cliente, userdata, mensagem):

    evento = json.loads(mensagem.payload.decode())

    print("\n[ PAGAMENTO ]")
    print(f"Processando pagamento do pedido {evento['pedido_id']}")
    print(f"Valor: R$ {evento['valor']:.2f}")
    print("Pagamento aprovado!")


cliente = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="servico-pagamento"
)

cliente.on_message = ao_receber_evento

cliente.connect(BROKER, PORTA, 60)

cliente.subscribe(TOPICO, qos=1)

print("Serviço de pagamento aguardando eventos...")

cliente.loop_forever()