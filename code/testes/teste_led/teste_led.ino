/*
  ESP 32 Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
  The ESP32 has an internal blue LED at D2 (GPIO 02)
*/
#include <WiFi.h>
#include <Firebase_ESP_Client.h>          // firebase library

//Provide the token generation process info.
#include "addons/TokenHelper.h"
//Provide the RTDB payload printing info and other helper functions.
#include "addons/RTDBHelper.h"

//Define Firebase Data object
FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;

bool signupOK = false;

#define WIFI_SSID "nome"
#define WIFI_PASSWORD "senha"

#define API_KEY "key"
#define DATABASE_URL "https://estacao-meteorologic-default-rtdb.firebaseio.com/"

#define LED_BUILTIN 2

void set_wifi() {
    Serial.begin(115200);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    Serial.print("Connecting to Wi-Fi");
    while (WiFi.status() != WL_CONNECTED){
      Serial.print(".");
      delay(300);
    }
    Serial.println();
    Serial.print("Connected to ");
    Serial.println(WIFI_SSID);
    Serial.print("Connected ao IP: ");
    Serial.println(WiFi.localIP());
    Serial.println();
}
void set_firebase(){
    /* Assign the api key (required) */
  config.api_key = API_KEY;

  /* Assign the RTDB URL (required) */
  config.database_url = DATABASE_URL;

  /* Sign up */
  if (Firebase.signUp(&config, &auth, "", "")){
    Serial.println("ok");
    signupOK = true;
  }
  else{
    Serial.printf("%s\n", config.signer.signupError.message.c_str());
  }

  /* Assign the callback function for the long running token generation task */
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h
  
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);
}

void setup() 
{
  // Initialise serial communication for local diagnostics
  Serial.begin(115200);

  set_wifi();
  set_firebase();

  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() 
{
  int firebaseStatus = Firebase.RTDB.getInt(&fbdo, "led");
  if (firebaseStatus == 1){
    Serial.println("Led ligado");
    digitalWrite(LED_BUILTIN, HIGH);    // turn the LED off by making the voltage HIGH
  }else if (firebaseStatus == 0){
    Serial.println("Led desligado");
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  }else{
    Serial.println("Credencial errada! Por favor, envie ON/OFF");
  };
}
