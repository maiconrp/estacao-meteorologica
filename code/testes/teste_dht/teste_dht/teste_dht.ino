
/*
Board: Esp32 Dev Module
ArduinoID v2.0.3
*/

//importando bibliotecas
#include <DHT.h>                   //importa biblioteca para o sensor dht22, v1.2.3

float temperatura, umidade;
DHT dht(13, DHT22);

void pegar_dados(){
  dht.begin();
  temperatura = dht.readTemperature();
  umidade = dht.readHumidity();
};

void setup() {
  //inicia comunicação serial
  Serial.begin(115200);   
}

void loop() {
  pegar_dados();
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println();
  Serial.print("Humidade:" );
  Serial.print(umidade);
  delay(1000);
 
}
