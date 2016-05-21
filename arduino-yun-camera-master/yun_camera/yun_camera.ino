// Esboço para fazer upload de fotos para Dropbox quando detecta movimento
#include <Bridge.h>
#include <Process.h>

// Processa imagem
Process picture;

// Nome do Arquivo
String filename;

// Pin
int pir_pin = 8;

// Caminho
String path = "/mnt/sda1/";

void setup() {
  
  // Inicia a Bridge
  Bridge.begin();
  
  // Aciona o modo pin
  pinMode(pir_pin,INPUT);
}

void loop(void) 
{
  
  if (digitalRead(pir_pin) == true) {
    
    // Gera o nome do  arquivo com timestamp (data e hora)
    filename = "";
    picture.runShellCommand("date +%s");
    while(picture.running());

    while (picture.available()>0) {
      char c = picture.read();
      filename += c;
    } 
    filename.trim();
    filename += ".png";
 
    // Tira a foto
    picture.runShellCommand("fswebcam " + path + filename + " -r 1280x720");
    while(picture.running());
    
    // Enviar para Dropbox
    picture.runShellCommand("python " + path + "upload_picture.py " + path + filename);
    while(picture.running());
  }
}
