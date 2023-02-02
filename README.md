# Estação Meteorológica IoT para Irrigação

![Badge em Análise](https://img.shields.io/badge/Status-Prototipagem-darkgreen?logoColor=7834cd&labelColor=white&style=for-the-badge)
![stars](https://img.shields.io/github/stars/maiconrp/Estacao-Meterorologic.svg?labelColor=white&color=darkgreen&style=for-the-badge)
![Issues](https://img.shields.io/github/issues/maiconrp/Estacao-Meterorologic?labelColor=white&color=darkgreen&style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/maiconrp/Estacao-Meterorologic?display_timestamp=committer&labelColor=white&color=darkgreen&style=for-the-badge)

Este projeto visa desenvolver um sistema de monitoramento de irrigação via estação meteorológica conectada à internet (IoT). Os valores coletados pela estação, enviados para um banco de dados, são utilizados na mensuraração da necessidade hídrica da plantação, que por sua vez, é exibido em uma aplicação (PWA)  e esses dados serem enviados para o servidor para possibilitar a visualização do seu histórico. Para informações mais detalhadas, veja a [documentação][docs]

## Funcionalidades:
* [ ] Cadastro e Autenticação de produtor
* [ ] Gerenciamento de cultura;
* [ ] Controlde e monitoramento da estação;
* [ ] Envio dos dados coletados pela estação para banco de dados.
* [ ] Notificação de mal funcionamento de sensores ou coleta de dados.
* [ ] Cálculo da Evapotranspiração de Referência e Diária da Cultura.
* [ ] Visualização dos dados climatológicos e do tempo de irrigação ativo
* [ ] Calculo de conomia de consumo de água.


O projeto possui diversas melhorias, implementando cada vez mais novos recursos. 

## Componentes Utilizados

* ESP32 NODEMCU
* Módulo Sensor Temperatura e Umidade DHT22
* Módulo Sensor de Luminosidade TEMT600
* Sensor de Pressão, Temperatura e altitude BMP280
* Reed Switch

## Software 
### Estação Meteorológica

O firmware é compilado usando o Arduino IDE e os softwares de envio de dados são desenvolvidos utilizando C/C++, no qual se faz uso das bibliotecas abaixo listadas: 

* `WiFi.h`: Conexão do ESP32 com WiFi.
* `IOXhop_FirebaseESP32.h`: Comunicação do ESP32 com o Firebase;
* `ArduinoJson.h`: Manipulação de informações no formato JSON (v5.13.3);
* `DHT.h`: Manipulação do sensor DHT22 (v1.2.3)

### Aplicação
A interface é construida em python, para isso, ela utiliza algumas bibliotecas que permitem o seu desenvolvimento, nas quais incluem:

* `flet`: Construção da interface
* `pyrebase4`: Comunicação com o Firebase

## Modo de Funcionamento 

Considerando um usuário autenticado e com produção cadastrada, o modo de funcionamento geral do sistema é:

1. Funcionando continuamente, onde os sensores realizam medições dos parâmetros necessários;
2. Os dados são enviados para um servidor (Firebase) com um intervalo programado;
3. Faz-se uso dos dados para mensurar a necessidade hídrica da plantação;
4. Com base na necessidade hidrica, o sistema calcula o tempo necessário para irrigação naquele dia;
5. A PWA tem acesso ao Firebase, onde os dados são exibidos

Para mais, veja os [Casos de Uso][casos de uso]

## Contribuir
Para contribuir veja o [nosso guia][guia]

## Equipe
[![Bruno](https://img.shields.io/badge/Bruno%20Reis-darkgreen?style=for-the-badge&logo=clipboard-list&logoColor=white)](https://github.com/brunoreisx)
[![Maicon](https://img.shields.io/badge/Maicon%20Robert-darkgreen?style=for-the-badge&logo=clipboard-list&logoColor=white)](https://github.com/maiconrp)
[![Paulo](https://img.shields.io/badge/Paulo%20César-darkgreen?style=for-the-badge&logo=clipboard-list&logoColor=white)](https://github.com/Soneca-Zzz)
[![Victor](https://img.shields.io/badge/Victor%20Fonteles-darkgreen?style=for-the-badge&logo=clipboard-list&logoColor=white)](https://github.com/Voctor-367)

[docs]: https://github.com/maiconrp/estacao-meteorologica/tree/master/docs
[casos de uso]: https://github.com/maiconrp/estacao-meteorologica/blob/master/docs/Doc%20de%20visao/Doc%20de%20Vis%C3%A3o%20-%20Esta%C3%A7%C3%A3o%20Meteorol%C3%B3gica.pdf
[guia]: https://github.com/maiconrp/estacao-meteorologica/tree/master/guia#readme

