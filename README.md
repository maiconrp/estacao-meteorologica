# Estação Meteorológica IoT para Irrigação

![Badge em Análise](https://img.shields.io/badge/Status-Análise%20e%20Pesquisa-darkgreen?logoColor=7834cd&labelColor=white&style=for-the-badge)
![stars](https://img.shields.io/github/stars/maiconrp/Estacao-Meterorologic.svg?labelColor=white&color=darkgreen&style=for-the-badge)
![Issues](https://img.shields.io/github/issues/maiconrp/Estacao-Meterorologic?labelColor=white&color=darkgreen&style=for-the-badge)
![Pull Requests](https://img.shields.io/github/issues-pr/maiconrp/Estacao-Meterorologic?labelColor=white&color=darkgreen&style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/maiconrp/Estacao-Meterorologic?display_timestamp=committer&labelColor=white&color=darkgreen&style=for-the-badge)

Este projeto visa desenvolver um sistema de monitoramento de irrigação via estação meteorológica conectada à internet (IoT). Os valores coletados pela estação, enviados para um banco de dados, são utilizados na mensuraração da necessidade hídrica da plantação, que por sua vez, é exibido em uma aplicação (PWA)  e esses dados serem enviados para o servidor para possibilitar a visualização do seu histórico. Para informações mais detalhadas, veja a [documentação][docs]

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

* `WiFi.h`: Biblioteca para conectar o ESP32 com WiFi.
* `IOXhop_FirebaseESP32.h`: Biblioteca para comunicação do ESP32 com o Firebase.
* `ArduinoJson.h`: Biblioteca para manipulação de informações no formato JSON, utilizado no Firebase. Versão 5.13.3 é recomendada.
* `DHT.h`: Biblioteca para o sensor DHT22, versão 1.2.3.

### Aplicação
A interface é construida em python, para isso, ela utiliza algumas bibliotecas que permitem o seu desenvolvimento, nas quais incluem:

* `flet`: Biblioteca para construção da interface
* `pyrebase4`: Biblioteca para comunicação com o Firebase

## Modo de Funcionamento 

Considerando um usuário autenticado e com sua produção cadastrada, o modo de funcionamento geral do sistema é:

1. Funcionando continuamente, onde os sensores realizam medições dos parâmetros necessários;
2. Os dados são enviados para um servidor (Firebase) com um intervalo programado;
3. Faz-se uso dos dados para mensurar a necessidade hídrica da plantação;
4. Com base na necessidade hidrica, o sistema calcula o tempo necessário para irrigação naquele dia;
5. A PWA tem acesso ao Firebase, onde os dados são exibidos

Para mais, veja os [Casos de Uso][casos de uso]

## Contribuir
Para saber como contribuir veja o [nosso guia][guia]

## Equipe
> [![Icone de check](https://img.shields.io/badge/✔️-white?style=for-the-badge&logoColor=blue)
![Bruno](https://img.shields.io/badge/Bruno%20Reis-darkgreen?style=for-the-badge&logo=clipboard-list&logoColor=white)](https://github.com/brunoreisx)
[![Icone de check](https://img.shields.io/badge/✔️-white?style=for-the-badge&logoColor=blue)
![Maicon](https://img.shields.io/badge/Maicon%20Robert-darkgreen?style=for-the-badge&logo=clipboard-list&logoColor=white)](https://github.com/maiconrp)
[![Icone de check](https://img.shields.io/badge/✔️-white?style=for-the-badge&logoColor=blue)
![Paulo](https://img.shields.io/badge/Paulo%20César-darkgreen?style=for-the-badge&logo=clipboard-list&logoColor=white)](https://github.com/Soneca-Zzz)
[![Icone de check](https://img.shields.io/badge/✔️-white?style=for-the-badge&logoColor=blue)
![Victor](https://img.shields.io/badge/Victor%20Fonteles-darkgreen?style=for-the-badge&logo=clipboard-list&logoColor=white)](https://github.com/Voctor-367)


[docs]: https://github.com/maiconrp/estacao-meteorologica/tree/master/docs
[casos de uso]: https://github.com/maiconrp/estacao-meteorologica/blob/master/docs/Doc%20de%20visao/Doc%20de%20Vis%C3%A3o%20-%20Esta%C3%A7%C3%A3o%20Meteorol%C3%B3gica.pdf
[guia]: https://github.com/maiconrp/estacao-meteorologica/tree/master/guia#readme

